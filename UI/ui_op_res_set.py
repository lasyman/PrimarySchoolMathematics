# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'op_res_set.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(562, 334)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.wgtItems = QtWidgets.QWidget(self.groupBox)
        self.wgtItems.setObjectName("wgtItems")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.wgtItems)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addWidget(self.wgtItems)
        self.widget_3 = QtWidgets.QWidget(self.groupBox)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.widget_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.spbResStart = QtWidgets.QSpinBox(self.widget_3)
        self.spbResStart.setObjectName("spbResStart")
        self.horizontalLayout_2.addWidget(self.spbResStart)
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.spbResEnd = QtWidgets.QSpinBox(self.widget_3)
        self.spbResEnd.setObjectName("spbResEnd")
        self.horizontalLayout_2.addWidget(self.spbResEnd)
        self.verticalLayout.addWidget(self.widget_3)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(315, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnOK = QtWidgets.QPushButton(self.widget)
        self.btnOK.setObjectName("btnOK")
        self.horizontalLayout.addWidget(self.btnOK)
        self.btnCancel = QtWidgets.QPushButton(self.widget)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        self.verticalLayout_3.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "运算项设置"))
        self.label.setText(_translate("Dialog", "何为运算项和结果？例如：3+7=10， 3和7是运算项，10为结果。"))
        self.groupBox.setTitle(_translate("Dialog", "算数项及结果取值范围："))
        self.label_11.setText(_translate("Dialog", "结果取值范围："))
        self.label_10.setText(_translate("Dialog", "到"))
        self.btnOK.setText(_translate("Dialog", "确定"))
        self.btnCancel.setText(_translate("Dialog", "取消"))

