from PyQt5.QtWidgets import QWidget, QCheckBox

from UI.ui_operator_item import Ui_opSelect


class OperatorItem(QWidget):
    """
    运算符选择项
    """
    def __init__(self, num, symbols, parent=None):
        QWidget.__init__(self, parent=parent)
        self.ui = Ui_opSelect()
        self.ui.setupUi(self)
        self.symbols = symbols
        self.ui.gbx.setTitle("第%s处运算符选择" % num)
        symbol = symbols[num - 1]
        index = 0
        for chk in self.findChildren(QCheckBox):
            chk.setChecked(symbol[index] != 0)
            index += 1

    def o_data(self):
        symbol = list()
        i = 0
        for chk in self.findChildren(QCheckBox):
            if chk.isChecked():
                symbol.append(i + 1)
            else:
                symbol.append(0)
            i += 1
        return symbol

