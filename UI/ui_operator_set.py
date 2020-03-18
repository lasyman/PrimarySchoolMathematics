# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'operator_set.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 330)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.wgtContent = QtWidgets.QWidget(Dialog)
        self.wgtContent.setObjectName("wgtContent")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.wgtContent)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addWidget(self.wgtContent)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(303, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.btnOK = QtWidgets.QPushButton(self.widget)
        self.btnOK.setObjectName("btnOK")
        self.horizontalLayout_4.addWidget(self.btnOK)
        self.btnCancel = QtWidgets.QPushButton(self.widget)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout_4.addWidget(self.btnCancel)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "运算符号设置"))
        self.label.setText(_translate("Dialog", "此处为多步运算题符号选择，比如：4+8-5=__，可配置的运算符就是+和-。"))
        self.btnOK.setText(_translate("Dialog", "确定"))
        self.btnCancel.setText(_translate("Dialog", "取消"))

