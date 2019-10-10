# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SampleSignIn.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from SampleSignUp import Ui_SignUp

import sys


class Ui_LogIn(object):
    def setupUi(self, LogIn):
        LogIn.setObjectName("LogIn")
        LogIn.resize(421, 442)
        self.SignInSignIn = QtWidgets.QPushButton(LogIn)
        self.SignInSignIn.setGeometry(QtCore.QRect(160, 270, 93, 28))
        self.SignInSignIn.setObjectName("SignInSignIn")
        self.label = QtWidgets.QLabel(LogIn)
        self.label.setGeometry(QtCore.QRect(40, 150, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(LogIn)
        self.label_2.setGeometry(QtCore.QRect(40, 210, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(LogIn)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 391, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(LogIn)
        self.label_4.setGeometry(QtCore.QRect(70, 330, 181, 16))
        self.label_4.setObjectName("label_4")
        self.SignInSignUp = QtWidgets.QPushButton(LogIn)
        self.SignInSignUp.setGeometry(QtCore.QRect(250, 320, 93, 28))
        self.SignInSignUp.setObjectName("SignInSignUp")
        self.SignInUsername = QtWidgets.QLineEdit(LogIn)
        self.SignInUsername.setGeometry(QtCore.QRect(120, 150, 241, 31))
        self.SignInUsername.setObjectName("SignInUsername")
        self.SignInPassword = QtWidgets.QLineEdit(LogIn)
        self.SignInPassword.setGeometry(QtCore.QRect(120, 200, 241, 31))
        self.SignInPassword.setObjectName("SignInPassword")
        self.SignInPassword.setEchoMode(QtWidgets.QLineEdit.Password)

        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)

    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "Sample Log In"))
        self.SignInSignIn.setText(_translate("LogIn", "Sign In"))
        self.label.setText(_translate("LogIn", "Username :"))
        self.label_2.setText(_translate("LogIn", "Password : "))
        self.label_3.setText(_translate("LogIn", "   Sample Log In"))
        self.label_4.setText(_translate("LogIn", "No account yet? click sign up : "))
        self.SignInSignUp.setText(_translate("LogIn", "Sign Up"))
        self.SignInSignIn.clicked.connect(self.logIn)
        self.SignInSignUp.clicked.connect(self.NewAccount)
        
    def logIn(self):
        Username = self.SignInUsername.text().strip()
        Password = self.SignInPassword.text().strip()
        
    def NewAccount(self):
        self.SignUp = QtWidgets.QWidget()
        self.uiSignUp = Ui_SignUp()
        self.uiSignUp.setupUi(self.SignUp)
        self.SignUp.show()
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QWidget()
    ui = Ui_LogIn()
    ui.setupUi(LogIn)
    LogIn.show()
    sys.exit(app.exec_())