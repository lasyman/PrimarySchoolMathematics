import random
from pathlib import Path
from PyQt5.QtWidgets import QWidget, QMessageBox, QRadioButton, QFileDialog

from UI.ui_mainWin import Ui_MainWin
from widgets.op_res_set_wgt import OperandResDlg
from widgets.operator_set_wgt import OperatorSetWgt
from libs.config_helper import cfg
from libs.psm_generator import Generator
from libs.psm_print import PrintPreview
from params import Params


class MainWinWidget(QWidget):
    """
    主界面
    """
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.parent = parent
        self.ui = Ui_MainWin()
        self.ui.setupUi(self)
        self.setWindowTitle("小学数学计算题生成工具")
        self.cur_param = Params()   # 当前参数
        self.param_list = list()    # 参数列表
        self.psm_list = list()      # 题目列表
        self.init_data()
        for rab in self.ui.gbxOpType.findChildren(QRadioButton):
            rab.toggled.connect(self.on_radio_btn_changed)
        for rab in self.ui.gbxOpStep.findChildren(QRadioButton):
            rab.toggled.connect(self.on_radio_btn_changed)
        for rab in self.ui.gbxSubjectType.findChildren(QRadioButton):
            rab.toggled.connect(self.on_radio_btn_changed)
        for rab in self.ui.gbxAddSet.findChildren(QRadioButton):
            rab.toggled.connect(self.on_radio_btn_changed)
        for rab in self.ui.gbxSubSet.findChildren(QRadioButton):
            rab.toggled.connect(self.on_radio_btn_changed)

        self.ui.btnOpResSet.clicked.connect(self.on_operand_res_set)
        self.ui.btnOperatorSet.clicked.connect(self.on_operator_set)
        self.ui.btnClearSubject.clicked.connect(self.on_clean_subject)
        self.ui.btnAddSubject.clicked.connect(self.on_add_subject)
        self.ui.btnGen.clicked.connect(self.on_gen_subject)
        self.ui.btnBrowse.clicked.connect(self.on_browse_save_path)
        self.ui.ckbBracket.stateChanged.connect(self.on_use_bracket)

    def init_data(self):
        """
        根据配置文件初始化界面
        :return:
        """
        signum = int(cfg.get_cfg("config", "signum"))
        self.cur_param.signum = signum
        self.ui.rabAdd.setChecked(signum == 1)
        self.ui.rabSub.setChecked(signum == 2)
        self.ui.rabMult.setChecked(signum == 3)
        self.ui.rabDiv.setChecked(signum == 4)

        step = int(cfg.get_cfg("config", "step"))
        self.ui.rabOneStep.setChecked(step == 1)
        self.ui.rabTwoStep.setChecked(step == 2)
        self.ui.ranTreeStep.setChecked(step == 3)
        self.cur_param.step = step

        is_result = int(cfg.get_cfg("config", "is_result"))
        self.ui.rabResult.setChecked(is_result == 1)
        self.ui.rabItem.setChecked(is_result == 0)
        self.cur_param.is_result = is_result

        carry = int(cfg.get_cfg("config", "carry"))
        self.cur_param.carry = carry
        self.ui.rabRandCarry.setChecked(carry == 1)
        self.ui.rabAddCarry.setChecked(carry == 2)
        self.ui.rabNoCarry.setChecked(carry == 3)

        abd = int(cfg.get_cfg("config", "abdication"))
        self.cur_param.abdication = abd
        self.ui.rabRandAbdicate.setChecked(abd == 1)
        self.ui.rabSubAbdicate.setChecked(abd == 2)
        self.ui.rabNoAbdicate.setChecked(abd == 3)

        number = int(cfg.get_cfg("config", "number"))
        self.ui.spbSubjectCount.setValue(number)
        self.cur_param.number = number

        juanzishu = int(cfg.get_cfg("config", "juanzishu"))
        self.ui.spbTotal.setValue(juanzishu)
        self.cur_param.juanzishu = juanzishu

        lieshu = int(cfg.get_cfg("config", "lieshu"))
        self.ui.spbColCount.setValue(lieshu)
        self.cur_param.lieshu = lieshu

        jz_title = cfg.get_cfg("config", "jz_title")
        self.ui.lneTitle.setText(jz_title)
        self.cur_param.jz_title = jz_title

        inf_title = cfg.get_cfg("config", "inf_title")
        self.ui.lneSubTitle.setText(inf_title)
        self.cur_param.inf_title = inf_title

        self.cur_param.multistep = eval(cfg.get_cfg("config", "multistep"))
        self.cur_param.symbols = eval(cfg.get_cfg("config", "symbols"))

        out_put = cfg.get_cfg("config", "out_put")
        self.ui.lneOutPath.setText(out_put)
        self.cur_param.out_put = out_put

    def on_operand_res_set(self):
        """
        运算项及结果设置
        :return:
        """
        dlg = OperandResDlg(self.cur_param, self)
        res = dlg.exec_()
        if res == 1:
            self.cur_param.multistep = dlg.operand_data()
        cfg.update_param_to_cfg("config", self.cur_param)

    def on_operator_set(self):
        """
        运算符设置
        :return:
        """
        dlg = OperatorSetWgt(self.cur_param, self)
        res = dlg.exec_()
        if res == 1:
            self.cur_param.symbols = dlg.operator_data()
        cfg.update_param_to_cfg("config", self.cur_param)

    def on_browse_save_path(self):
        path = QFileDialog.getExistingDirectory(self, "打开目录", "/")
        p = Path(path)
        self.cur_param.out_put = str(p.resolve())
        if path is not "":
            self.ui.lneOutPath.setText(self.cur_param.out_put)
        cfg.update_param_to_cfg("config", self.cur_param)

    def on_use_bracket(self, state):
        self.cur_param.is_bracket = 1 if state > 0 else 0
        cfg.update_param_to_cfg("config", self.cur_param)

    def on_add_subject(self):
        step = self.__get_op_step()
        signum = self.__get_op_type()

        if step == 1 and signum == 4:
            if self.multistep[1][0] <= 0:
                QMessageBox.warning(self, '错误提示', "除法时余数不能为0，请修改算数项设置",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                return 0
        # 多步运算时除法余数为零判断
        if step > 1:
            if (4 in self.cur_param.symbols[0] and self.cur_param.multistep[1][0] <= 0) or (
                    4 in self.cur_param.symbols[1] and self.cur_param.multistep[2][0] <= 0) or (
                    4 in self.cur_param.symbols[2] and self.cur_param.multistep[3][0] <= 0):
                QMessageBox.warning(self, "错误提示", "除法时余数不能为0，请修改算数项设置",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        number = self.ui.spbSubjectCount.value()
        # 题库内容提示
        psm_info = ""
        s_type = "求结果"
        if self.cur_param.is_result == 0:
            s_type = "求计算项"
        if step == 1:
            if signum == 1:
                psm_info = "==> 加法计算题 %s 道 (%s) <==" % (str(number), s_type)
            elif signum == 2:
                psm_info = "==> 减法计算题 %s 道 (%s) <==" % (str(number), s_type)
            elif signum == 3:
                psm_info = "==> 乘法计算题 %s 道 (%s) <==" % (str(number), s_type)
            elif signum == 4:
                psm_info = "==> 除法计算题 %s 道 (%s) <==" % (str(number), s_type)
            else:
                raise Exception("没有这个题型哦")
        elif step == 2:
            psm_info = "==> 两步计算计算题 %s 道 (%s) <==" % (str(number), s_type)
        elif step == 3:
            psm_info = "==> 三步计算计算题 %s 道 (%s) <==" % (str(number), s_type)

        self.ui.txbContent.append(psm_info)
        self.param_list.append(self.__get_params())

    def on_clean_subject(self):
        self.psm_list.clear()
        self.param_list.clear()
        self.ui.txbContent.clear()

    def on_radio_btn_changed(self):
        # 运算类型
        signum = self.__get_op_type()
        self.cur_param.signum = signum
        # 运算步数
        step = self.__get_op_step()
        self.cur_param.step = step
        # 题目类型 (计算结果或者运算项)
        is_result = 1 if self.ui.rabResult.isChecked() else 0
        self.cur_param.is_result = is_result
        # 加法设置
        carry = self.__get_add_set()
        self.cur_param.carry = carry
        # 减法设置
        abd = self.__get_sub_set()
        self.cur_param.abdication = abd
        cfg.update_param_to_cfg("config", self.cur_param)

    def on_gen_subject(self):
        """
        生成试题
        :return:
        """
        if len(self.param_list) == 0:
            QMessageBox.warning(self, "提示", "还没添加计算题目", QMessageBox.Ok)
        else:
            cfg.update_param_to_cfg("config", self.__get_params())
            for i in range(self.ui.spbTotal.value()):
                temp_list = list()
                for param in self.param_list:
                    g = Generator(param)
                    temp_list = temp_list + g.generate_data()
                random.shuffle(temp_list)
                self.psm_list.append(temp_list)

            pp = PrintPreview(self.psm_list, self.ui.lneTitle.text(), self.ui.lneSubTitle.text(),
                              self.cur_param.out_put, self.cur_param.lieshu)
            pp.produce()
            self.on_clean_subject()
            QMessageBox.information(self, "提示", "文件生成成功，保存在docx目录下！", QMessageBox.Yes, QMessageBox.Yes)

    def __get_params(self):
        """
        获取当前参数
        :return:
        """
        p = Params()
        p.signum = self.__get_op_type()
        p.step = self.__get_op_step()
        p.is_result = 1 if self.ui.rabResult.isChecked() else 0
        p.is_bracket = 1 if self.ui.ckbBracket.isChecked() else 0
        p.multistep = self.cur_param.multistep
        p.symbols = self.cur_param.symbols
        p.number = self.ui.spbSubjectCount.value()
        p.juanzishu = self.ui.spbTotal.value()
        p.lieshu = self.ui.spbColCount.value()
        p.jz_title = self.ui.lneTitle.text()
        p.inf_title = self.ui.lneSubTitle.text()
        p.out_put = self.ui.lneOutPath.text()
        p.carry = self.__get_add_set()
        p.abdication = self.__get_sub_set()
        return p

    def __get_op_type(self):
        """
        获取运算类型 (加减乘除)
        :return:
        """
        if self.ui.rabAdd.isChecked():
            signum = 1
        elif self.ui.rabSub.isChecked():
            signum = 2
        elif self.ui.rabMult.isChecked():
            signum = 3
        else:
            signum = 4
        return signum

    def __get_op_step(self):
        """
        获取运算步数
        :return:
        """
        if self.ui.rabOneStep.isChecked():
            step = 1
        elif self.ui.rabTwoStep.isChecked():
            step = 2
        else:
            step = 3
        return step

    def __get_add_set(self):
        """
        获取加法进位设置
        :return:
        """
        if self.ui.rabRandCarry.isChecked():
            carry = 1
        elif self.ui.rabAddCarry.isChecked():
            carry = 2
        else:
            carry = 3
        return carry

    def __get_sub_set(self):
        """
        获取减法退位设置
        :return:
        """
        if self.ui.rabRandAbdicate.isChecked():
            abd = 1
        elif self.ui.rabSubAbdicate.isChecked():
            abd = 2
        else:
            abd = 3
        return abd
