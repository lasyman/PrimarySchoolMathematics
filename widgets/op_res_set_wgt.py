from PyQt5.QtWidgets import QDialog
from params import Params
from UI.ui_op_res_set import Ui_Dialog
from widgets.operand_item import OperandItem


class OperandResDlg(QDialog):
    """
    运算项和结果设置界面
    """
    def __init__(self, param: Params, parent=None):
        QDialog.__init__(self, parent=parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.param = param
        self.init_data()

        self.ui.btnOK.clicked.connect(self.on_btn_ok_clicked)
        self.ui.btnCancel.clicked.connect(self.on_btn_cancel_clicked)

    def init_data(self):
        for i in range(0, self.param.step + 1):
            item = OperandItem(i+1, self.param)
            self.ui.wgtItems.layout().addWidget(item)
        self.ui.spbResStart.setValue(self.param.multistep[len(self.param.multistep) - 1][0])
        self.ui.spbResEnd.setValue(self.param.multistep[len(self.param.multistep) - 1][1])

    def on_btn_ok_clicked(self):
        self.accept()

    def on_btn_cancel_clicked(self):
        self.reject()

    def operand_data(self):
        i = 0
        multistep = self.param.multistep
        for item in self.findChildren(OperandItem):
            multistep[i] = item.o_data()
            i += 1
        res = list()
        res.append(self.ui.spbResStart.value())
        res.append(self.ui.spbResEnd.value())
        multistep[len(multistep) - 1] = res
        return multistep
