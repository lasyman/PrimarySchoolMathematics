from PyQt5.QtWidgets import QWidget
from params import Params
from UI.ui_operand_item import Ui_Form


class OperandItem(QWidget):
    """
    运算项
    """
    def __init__(self, num, param: Params, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.label_1.setText("第%s个运算项取值范围：" % num)
        self.ui.spbStart.setValue(param.multistep[num - 1][0])
        self.ui.spbEnd.setValue(param.multistep[num - 1][1])

    def o_data(self):
        d = list()
        d.append(self.ui.spbStart.value())
        d.append(self.ui.spbEnd.value())
        return d
