from PyQt5.QtWidgets import QDialog

from UI.ui_operator_set import Ui_Dialog
from widgets.operator_item import OperatorItem


class OperatorSetWgt(QDialog):
    """
    运算符设置界面
    """
    def __init__(self, param, parent=None):
        QDialog.__init__(self, parent=parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.param = param
        self.init_data()
        self.ui.btnOK.clicked.connect(self.on_btn_ok_clicked)
        self.ui.btnCancel.clicked.connect(self.on_btn_cancel_clicked)

    def init_data(self):
        for i in range(0, self.param.step):
            item = OperatorItem(i+1, self.param.symbols)
            self.ui.wgtContent.layout().addWidget(item)

    def on_btn_ok_clicked(self):
        self.accept()

    def on_btn_cancel_clicked(self):
        self.reject()

    def operator_data(self):
        symbols = self.param.symbols
        i = 0
        for item in self.findChildren(OperatorItem):
            symbols[i] = item.o_data()
            i += 1
        return symbols
