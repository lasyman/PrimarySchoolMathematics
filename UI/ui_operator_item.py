# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'operator_item.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_opSelect(object):
    def setupUi(self, opSelect):
        opSelect.setObjectName("opSelect")
        opSelect.resize(400, 52)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(opSelect)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gbx = QtWidgets.QGroupBox(opSelect)
        self.gbx.setObjectName("gbx")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gbx)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ckbAdd = QtWidgets.QCheckBox(self.gbx)
        self.ckbAdd.setObjectName("ckbAdd")
        self.horizontalLayout.addWidget(self.ckbAdd)
        self.ckbSub = QtWidgets.QCheckBox(self.gbx)
        self.ckbSub.setObjectName("ckbSub")
        self.horizontalLayout.addWidget(self.ckbSub)
        self.ckbMult = QtWidgets.QCheckBox(self.gbx)
        self.ckbMult.setObjectName("ckbMult")
        self.horizontalLayout.addWidget(self.ckbMult)
        self.ckbDiv = QtWidgets.QCheckBox(self.gbx)
        self.ckbDiv.setObjectName("ckbDiv")
        self.horizontalLayout.addWidget(self.ckbDiv)
        self.horizontalLayout_2.addWidget(self.gbx)

        self.retranslateUi(opSelect)
        QtCore.QMetaObject.connectSlotsByName(opSelect)

    def retranslateUi(self, opSelect):
        _translate = QtCore.QCoreApplication.translate
        opSelect.setWindowTitle(_translate("opSelect", "Form"))
        self.gbx.setTitle(_translate("opSelect", "第?处运算符号选择"))
        self.ckbAdd.setText(_translate("opSelect", "+（加法）"))
        self.ckbSub.setText(_translate("opSelect", "-（减法）"))
        self.ckbMult.setText(_translate("opSelect", "x（乘法）"))
        self.ckbDiv.setText(_translate("opSelect", "÷（除法）"))

