# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\lvgr2\Desktop\sticks\myUI\inputDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys 

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_inEqualDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.initUi()
        
        self.connectAllSlots()
        
        self.confirmInput = False
        self.finished = False
        self.inputNums=[0,0,0]
        self.inputsymbol = '+'
        
    def initUi(self):
        self.resize(600,270) 
        self.mainLayout = QtWidgets.QGridLayout()
        self.setLayout(self.mainLayout)
        
        self.upWidget = QtWidgets.QWidget()
        self.upWidget.setObjectName("upWidget")
        self.upLayout = QtWidgets.QGridLayout()
        self.upWidget.setLayout(self.upLayout)
        
        self.downWidget = QtWidgets.QWidget()
        self.downWidget.setObjectName("downWidget")
        self.downLayout = QtWidgets.QGridLayout()
        self.downWidget.setLayout(self.downLayout)
        
        self.mainLayout.addWidget(self.upWidget,0,0,4,1)
        self.mainLayout.addWidget(self.downWidget,4,0,1,1)
        
        self.upInputLabel = QtWidgets.QPushButton("Your input")
        self.upInputLabel.setObjectName("upLabel")
        
        self.num1SpinBox = QtWidgets.QSpinBox()
        self.num1SpinBox.setObjectName("upSpinBox")
        self.num1SpinBox.setMinimum(-9)
        self.num1SpinBox.setMaximum(99)
        self.num1SpinBox.setAlignment(Qt.AlignCenter)
        self.num2SpinBox = QtWidgets.QSpinBox()
        self.num2SpinBox.setObjectName("upSpinBox")
        self.num2SpinBox.setMinimum(-9)
        self.num2SpinBox.setMaximum(99)
        self.num2SpinBox.setAlignment(Qt.AlignCenter)
        self.num3SpinBox = QtWidgets.QSpinBox()
        self.num3SpinBox.setObjectName("upSpinBox")
        self.num3SpinBox.setMinimum(-99)
        self.num3SpinBox.setMaximum(999)
        self.num3SpinBox.setAlignment(Qt.AlignCenter)
        
        self.symbolComboBox = QtWidgets.QComboBox()
        self.symbolComboBox.setObjectName("upComboBox")
        self.symbolComboBox.setEditable(True)
        self.symbolComboBox.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.symbolComboBox.addItems('+ - x'.split())
        
        self.equalLabel = QtWidgets.QPushButton("=")
        self.equalLabel.setObjectName("upLabel2")
        
        # add item in up layout 
        self.upLayout.addWidget(self.upInputLabel,0,0,1,2)
        self.upLayout.addWidget(self.num1SpinBox,1,0,1,1)
        self.upLayout.addWidget(self.symbolComboBox,1,1,1,1)
        self.upLayout.addWidget(self.num2SpinBox,1,2,1,1)
        self.upLayout.addWidget(self.equalLabel,1,3,1,1)
        self.upLayout.addWidget(self.num3SpinBox,1,4,1,1)
        
        self.okayButton = QtWidgets.QPushButton("")
        self.okayButton.setObjectName("downButton")
        self.cancelButton = QtWidgets.QPushButton("")
        self.cancelButton.setObjectName("downButton")
        
        #add itme in down layout 
        self.downLayout.addWidget(self.okayButton,0,0,1,1)
        self.downLayout.addWidget(self.cancelButton,0,1,1,1)
        
        
        #begin beautify 
        self.okayButton.setFixedSize(25,25)
        self.cancelButton.setFixedSize(25,25)
        self.okayButton.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.cancelButton.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        
        self.upWidget.setStyleSheet(
           '''
            QWidget#upWidget{
                background:black;
                border-top:1px solid black;
                border-bottom:1px solid black;
                border-right:1px solid black;
                border-left:1px solid black;
            }
            QPushButton{
                border:none;
                color:white;
            }
            QPushButton#upLabel2{
                border:none;
                font-size:20px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#upLabel{
                border:none;
                font-size:30px;
                font-weight:700;
                font-family: Arial,'Microsoft YaHei',"Helvetica Neue", Helvetica, sans-serif;
            }
            QComboBox#upComboBox{
                color:white;
                background:black;
                border:none;
                border-bottom:1px solid white;
                font-size:20px;
                font-weight:400;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QComboBox::drop-down{
                color:black; 
                background:black; 
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 0px;
            }
            QComboBox::down-arrow{
                border-left-width: 0px;
                border-left-color: black;
                border-left-style: solid; /* just a single line */
                border-top-right-radius: 3px; /* same radius as the QComboBox */
            }
            QSpinBox#upSpinBox{
                color:white;
                background:black;
                border: none;
                border-bottom:1px solid white;
                font-size: 20px; 
                font-weight:400; 
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QSpinBox#upSpinBox::up-button{
                width: 0px;
            }
            QSpinBox#upSpinBox::down-button{
                width: 0px;
            }
            QComboBox::item  
            {
                color:white; 
                background:black;
                border:none; 
            } 
            '''       
        )
        
        self.downWidget.setStyleSheet(
            '''
            QWidget#downWidget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-left:1px solid darkGray;
            }
            '''
        )
        
        self.setWindowOpacity(0.9)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.mainLayout.setSpacing(0)
    
    def connectAllSlots(self): 
        self.okayButton.clicked.connect(self.slotOkay)
        self.cancelButton.clicked.connect(self.slotCancel) 
    
    def slotOkay(self): 
        self.close()
        
        self.confirmInput = True 
        self.inputNums[0] = self.num1SpinBox.value()
        self.inputNums[1] = self.num2SpinBox.value()
        self.inputNums[2] = self.num3SpinBox.value()
         
        self.inputsymbol = self.symbolComboBox.currentText()
        
        if self.inputsymbol == 'x': 
            self.inputsymbol = '*'
        elif self.inputsymbol == '+': 
            pass 
        elif self.inputsymbol == '-' : 
            pass 
        elif self.inputsymbol == '*': 
            pass 
        else: 
            self.inputsymbol = '+'
                
    def slotCancel(self): 
        self.confirmInput = False 
        self.close() 
    
    def resizeEvent(self,event):
        pass    
    
    def debug(self): 
        print("input num:") 
        for num in self.inputNums: 
            print(num)
            
        print("input symbol")
        print(self.inputsymbol)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Ui_inEqualDialog()
    gui.show()
    sys.exit(app.exec_())
        
        
        
    
    