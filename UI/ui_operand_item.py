# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'operand_item.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(409, 32)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout.addWidget(self.label_1)
        self.spbStart = QtWidgets.QSpinBox(Form)
        self.spbStart.setMinimumSize(QtCore.QSize(0, 22))
        self.spbStart.setObjectName("spbStart")
        self.horizontalLayout.addWidget(self.spbStart)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spbEnd = QtWidgets.QSpinBox(Form)
        self.spbEnd.setMinimumSize(QtCore.QSize(0, 22))
        self.spbEnd.setObjectName("spbEnd")
        self.horizontalLayout.addWidget(self.spbEnd)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_1.setText(_translate("Form", "第?个运算项取值范围："))
        self.label_2.setText(_translate("Form", "到"))

