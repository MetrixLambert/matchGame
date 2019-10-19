# -*- coding: utf-8 -*-

'''
# Loading Dialog 
# Usage: for loading process 
# Note: need to connect cancelTrigger first 
# Made by Ethan Lyu on 2019-10-18
# Copyright Protected
'''

import sys 
import os 

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtGui import QMovie


## return basic info UI need 
def basicInfo(): 
    picPath = os.path.abspath('.') + "\\myUI\\image\\"
    return [picPath] 


class Ui_loadingDialog(QtWidgets.QDialog):
    cancelTrigger = pyqtSignal()   # used for cancel cal 
    
    def __init__(self):
        super().__init__()
        
        self.initUi()
        self.connectAllSlots()
              
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
        
        # items in up layout 
        self.loadingLabel = QtWidgets.QLabel()
        self.loadingLabel.setFixedSize(280,210)
        
        self.titleLabel = QtWidgets.QLabel()
        self.titleLabel.setText("loading...")
        self.titleLabel.setObjectName("upLabel2")
        
        # add item in up layout 
        self.upLayout.addWidget(self.loadingLabel,0,0,1,2)
        self.upLayout.addWidget(self.titleLabel,0,1,1,1)
        
        # items in down layout 
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
            QLabel#upLabel2{
                color:white;
                border:none;
                font-size:24px;
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
                padding: 1px 2px 1px 2px; 
                font-size:20px;
                font-weight:400;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QComboBox::drop-down{
                color:black; 
                background:black; 
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left-width: 1px;
                border-left-color: darkgray;
                border-left-style: solid; 
                border-top-right-radius: 3px;
                border-bottom-right-radius: 3px;
            }
            QComboBox::down-arrow{
                image: url(/image/drop-down.png);
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
    
        # laod img 
        self.addLoadingGif()
        
    def addLoadingGif(self): 
        [picPath] = basicInfo()
        loadingPath = picPath + "loading.gif"
        loadingGif = QMovie(loadingPath)
        
        self.loadingLabel.setMovie(loadingGif)
        self.loadingLabel.setScaledContents(True)

        loadingGif.start()
    
    def connectAllSlots(self): 
        self.okayButton.clicked.connect(self.slotOkay)
        self.cancelButton.clicked.connect(self.slotCancel) 
    
    def slotOkay(self): 
        self.close()
                
    def slotCancel(self): 
        self.close() 
        self.cancelTrigger.emit()
    
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
    gui = Ui_loadingDialog()
    gui.show()
    sys.exit(app.exec_())
        
        
        
    
    