import sys
from PyQt5.QtWidgets import QApplication

from widgets.main_win import MainWinWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWinWgt = MainWinWidget()
    mainWinWgt.show()
    sys.exit(app.exec_())
