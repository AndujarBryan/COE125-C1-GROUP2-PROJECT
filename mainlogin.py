from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox 

#from reglay import registerUi
from MainAuth import Account
from MainAuth import loginProcess 
from MainAuth import registerAcc
import os
#from selectpy import selectUi

import bgi
import sys

class loginUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(loginUi,self).__init__()
        uic.loadUi("loginGui.ui",self)
        
        self.loginButton = self.findChild(QtWidgets.QPushButton,'loginButton')
        self.registerButton = self.findChild(QtWidgets.QPushButton,'registerButton')
        self.usernameLine = self.findChild(QtWidgets.QLineEdit,'userLine')
        self.passwordLine = self.findChild(QtWidgets.QLineEdit,'passLine')
        
        
        self.loginButton.clicked.connect(self.login)
        self.registerButton.clicked.connect(self.reg)
        
        self.show()
         
    def login(self):
        logacc = Account()
        logacc.setUsername(self.usernameLine.text())
        logacc.setPassword(self.passwordLine.text())
        value = loginProcess(self,logacc)
        if value is True: 
            os.system('python objectdetectionimagewebcam.py')
            self.close()
        
        else:
            self.usernameLine.clear()
            self.passwordLine.clear()
            
            
    def reg(self):
        self.regui = registerUi()
        self.regui.show()
#CLASS FOR THE REGISTER UI
class registerUi(QtWidgets.QWidget):
    def __init__(self):
        super(registerUi,self).__init__()
        uic.loadUi("registerGui.ui",self)
        
        self.newuserline = self.findChild(QtWidgets.QLineEdit,'userLine')
        self.newpassline = self.findChild(QtWidgets.QLineEdit,'passLine')
        self.newfnameline = self.findChild(QtWidgets.QLineEdit,'fnameLine')
        self.newlnameline = self.findChild(QtWidgets.QLineEdit,'lnameLine')
        
        self.regButton = self.findChild(QtWidgets.QPushButton,'registerButton')
        self.canButton = self.findChild(QtWidgets.QPushButton,'cancelButton')
        
        self.regButton.clicked.connect(self.reg)
        self.canButton.clicked.connect(self.can)
        
        self.show()
        
    def can(self):
        self.close()
        
    def reg(self):
        acc = Account()
        acc.setUsername(self.newuserline.text())
        acc.setPassword(self.newpassline.text())
        acc.setfName(self.newfnameline.text())
        acc.setlName(self.newlnameline.text())
        
        if acc.username.__len__() <= 0 or acc.username == " " or acc.password.__len__() <= 0 or acc.password == " " or acc.fname.__len__() <= 0 or acc.fname == " " or acc.lname.__len__() <= 0 or acc.lname == " " :
            mess = QMessageBox()
            mess.setIcon(QMessageBox.Information)
            
            mess.setText("Cannot accept blank inputs")
            mess.setWindowTitle("Input error")
            mess.setStandardButtons(QMessageBox.Ok)
            mess.exec()
        else:
            self.newuserline.clear()
            self.newpassline.clear()
            self.newfnameline.clear()
            self.newlnameline.clear()
            if(registerAcc(self,acc)):
                
                mess = QMessageBox()
                mess.setIcon(QMessageBox.Information)
            
                mess.setText("Registration successful!")
                mess.setWindowTitle("Register")
                mess.setStandardButtons(QMessageBox.Ok)
                mess.exec()     
                
                
                
                self.close()
            else:
                mess = QMessageBox()
                mess.setIcon(QMessageBox.Information)
                mess.setText("Please make sure inputs are correct!")
                mess.setWindowTitle("Input error")
                mess.setStandardButtons(QMessageBox.Ok)
                mess.exec()    
            


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = loginUi()
    window.show()
    sys.exit(app.exec_())