# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/vigenere.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VigenereCipher(object):
    def setupUi(self, VigenereCipher):
        VigenereCipher.setObjectName("VigenereCipher")
        VigenereCipher.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(VigenereCipher)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_Encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Encrypt.setGeometry(QtCore.QRect(190, 460, 75, 23))
        self.btn_Encrypt.setObjectName("btn_Encrypt")
        self.Lable1 = QtWidgets.QLabel(self.centralwidget)
        self.Lable1.setGeometry(QtCore.QRect(260, 20, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Lable1.setFont(font)
        self.Lable1.setObjectName("Lable1")
        self.lable3 = QtWidgets.QLabel(self.centralwidget)
        self.lable3.setGeometry(QtCore.QRect(70, 230, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lable3.setFont(font)
        self.lable3.setObjectName("lable3")
        self.txt_Key = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_Key.setGeometry(QtCore.QRect(250, 230, 381, 41))
        self.txt_Key.setObjectName("txt_Key")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(70, 120, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.lable4 = QtWidgets.QLabel(self.centralwidget)
        self.lable4.setGeometry(QtCore.QRect(70, 350, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lable4.setFont(font)
        self.lable4.setObjectName("lable4")
        self.txt_CipherText = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_CipherText.setGeometry(QtCore.QRect(250, 340, 381, 71))
        self.txt_CipherText.setObjectName("txt_CipherText")
        self.txt_PlainText = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_PlainText.setGeometry(QtCore.QRect(250, 90, 381, 71))
        self.txt_PlainText.setObjectName("txt_PlainText")
        self.btn_Decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Decrypt.setGeometry(QtCore.QRect(470, 460, 75, 23))
        self.btn_Decrypt.setObjectName("btn_Decrypt")
        VigenereCipher.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VigenereCipher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        VigenereCipher.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VigenereCipher)
        self.statusbar.setObjectName("statusbar")
        VigenereCipher.setStatusBar(self.statusbar)

        self.retranslateUi(VigenereCipher)
        QtCore.QMetaObject.connectSlotsByName(VigenereCipher)

    def retranslateUi(self, VigenereCipher):
        _translate = QtCore.QCoreApplication.translate
        VigenereCipher.setWindowTitle(_translate("VigenereCipher", "VigenereCipher"))
        self.btn_Encrypt.setText(_translate("VigenereCipher", "Encrypt"))
        self.Lable1.setText(_translate("VigenereCipher", "VIGENERE CIPHER"))
        self.lable3.setText(_translate("VigenereCipher", "Key:"))
        self.label2.setText(_translate("VigenereCipher", "Plain Text:"))
        self.lable4.setText(_translate("VigenereCipher", "Cipher Text:"))
        self.btn_Decrypt.setText(_translate("VigenereCipher", "Decrypt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VigenereCipher = QtWidgets.QMainWindow()
    ui = Ui_VigenereCipher()
    ui.setupUi(VigenereCipher)
    VigenereCipher.show()
    sys.exit(app.exec_())
