# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Code\Python\MCSL2\resources\MCSL2_AskDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MCSL2_AskDialog(object):
    def setupUi(self, MCSL2_AskDialog):
        MCSL2_AskDialog.setObjectName("MCSL2_AskDialog")
        MCSL2_AskDialog.resize(413, 242)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/MCSL2_Icon/MCSL2_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/MCSL2_Icon/MCSL2_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/MCSL2_Icon/MCSL2_Icon.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/MCSL2_Icon/MCSL2_Icon.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/MCSL2_Icon/MCSL2_Icon.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/MCSL2_Icon/MCSL2_Icon.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/MCSL2_Icon/MCSL2_Icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/MCSL2_Icon/MCSL2_Icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MCSL2_AskDialog.setWindowIcon(icon)
        self.Dialog_PushButton_Accept = QtWidgets.QPushButton(MCSL2_AskDialog)
        self.Dialog_PushButton_Accept.setGeometry(QtCore.QRect(90, 190, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.Dialog_PushButton_Accept.setFont(font)
        self.Dialog_PushButton_Accept.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Dialog_PushButton_Accept.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(0, 120, 212);\n"
"    border-radius: 7px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(0, 110, 212);\n"
"    border-radius: 7px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(0, 100, 212);\n"
"    border-radius: 7px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.Dialog_PushButton_Accept.setObjectName("Dialog_PushButton_Accept")
        self.Dialog_label = QtWidgets.QLabel(MCSL2_AskDialog)
        self.Dialog_label.setGeometry(QtCore.QRect(30, 20, 351, 151))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.Dialog_label.setFont(font)
        self.Dialog_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px\n"
"}")
        self.Dialog_label.setText("")
        self.Dialog_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Dialog_label.setObjectName("Dialog_label")
        self.Background = QtWidgets.QLabel(MCSL2_AskDialog)
        self.Background.setGeometry(QtCore.QRect(0, 0, 413, 242))
        self.Background.setStyleSheet("QLabel\n"
"{\n"
"    background-color: rgba(247, 247, 247,85%);\n"
"}")
        self.Background.setText("")
        self.Background.setObjectName("Background")
        self.Dialog_PushButton_Cancel = QtWidgets.QPushButton(MCSL2_AskDialog)
        self.Dialog_PushButton_Cancel.setGeometry(QtCore.QRect(230, 190, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.Dialog_PushButton_Cancel.setFont(font)
        self.Dialog_PushButton_Cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Dialog_PushButton_Cancel.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(240, 240, 240);\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(229, 229, 229);\n"
"    border-radius: 7px;\n"
"}")
        self.Dialog_PushButton_Cancel.setObjectName("Dialog_PushButton_Cancel")
        self.Background.raise_()
        self.Dialog_PushButton_Accept.raise_()
        self.Dialog_label.raise_()
        self.Dialog_PushButton_Cancel.raise_()

        self.retranslateUi(MCSL2_AskDialog)
        QtCore.QMetaObject.connectSlotsByName(MCSL2_AskDialog)

    def retranslateUi(self, MCSL2_AskDialog):
        _translate = QtCore.QCoreApplication.translate
        MCSL2_AskDialog.setWindowTitle(_translate("MCSL2_AskDialog", "提示"))
        self.Dialog_PushButton_Accept.setText(_translate("MCSL2_AskDialog", "确定"))
        self.Dialog_PushButton_Cancel.setText(_translate("MCSL2_AskDialog", "取消"))
import MCSL2_Icon_rc