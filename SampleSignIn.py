# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SampleSignIn.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sqlite3 as sq

from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QMessageBox 
from SampleSignUp import Ui_SignUp
import os

import sys
import bgi
        
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
        self.SignInSignIn.setStyleSheet("background-color: pink;")
        self.SignInUsername.setStyleSheet("background-color: pink;")
        self.SignInPassword.setStyleSheet("background-color: pink;")
        self.SignInSignUp.setStyleSheet("background-color: pink;")
        LogIn.setStyleSheet("background-color: blue;")
        
        self.SignUp = QtWidgets.QWidget()
        self.uiSignUp = Ui_SignUp()
        self.uiSignUp.setupUi(self.SignUp)

        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)

    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "Log In"))
        self.SignInSignIn.setText(_translate("LogIn", "Sign In"))
        self.label.setText(_translate("LogIn", "Username :"))
        self.label_2.setText(_translate("LogIn", "Password : "))
        self.label_3.setText(_translate("LogIn", "   Welcome User!"))
        self.label_4.setText(_translate("LogIn", "No account yet? click sign up : "))
        self.SignInSignUp.setText(_translate("LogIn", "Sign Up"))
        self.SignInSignIn.clicked.connect(self.logIn)
        self.SignInSignUp.clicked.connect(self.NewAccount)
        
    def logIn(self):
        Username = self.SignInUsername.text().strip()
        Password = self.SignInPassword.text().strip()
        value = False
        
        if Username == 0 or Password == 0:
            value = False
            '''  mess = QMessageBox()
            mess.setIcon(QMessageBox.Information)
            
            mess.setText("Cannot accept blank inputs")
            mess.setWindowTitle("Input error")
            mess.setStandardButtons(QMessageBox.Ok)
            mess.exec()'''
        else:
            connection = sq.connect("acc.db")
            con = connection.cursor()
            con.execute("SELECT accountid,fname,lname FROM accounts WHERE username = ? and password = ?",(Username,Password))
            userdata = con.fetchone()
            connection.close()
            if userdata is None:
                 '''
                 mess = QMessageBox()
                 mess.setIcon(QMessageBox.Critical)
                 mess.setText("You failed to login! Wrong Username/Password")
                 mess.setWindowTitle("Error")
                 mess.setStandardButtons(QMessageBox.Ok)
                 mess.exec()
                 '''
                 value = False
            else:
                value = True
        if value is True: 
            mess = QMessageBox()
            mess.setIcon(QMessageBox.Information) 
            mess.setText("Log In Successful!")
            mess.setWindowTitle("LogIn")
            mess.setStandardButtons(QMessageBox.Ok)
            mess.exec()     
            os.system('python objectdetectionimagewebcam.py')
            self.close()
        
        else:
            mess = QMessageBox()
            mess.setIcon(QMessageBox.Information)
            mess.setText("Username or Password not found")
            mess.setWindowTitle("Input error")
            mess.setStandardButtons(QMessageBox.Ok)
            mess.exec()
            self.SignInUsername.clear()
            self.SignInPassword.clear()
        
    def NewAccount(self):
        self.SignUp.show()
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QWidget()
    ui = Ui_LogIn()
    ui.setupUi(LogIn)
    LogIn.show()
    sys.exit(app.exec_())
