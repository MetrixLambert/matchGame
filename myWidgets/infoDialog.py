# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\lvgr2\Desktop\sticks\myUI\inputDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys 

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_infoDialog(QtWidgets.QDialog):
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
        
        self.upTitleLabel = QtWidgets.QPushButton("")
        self.upTitleLabel.setObjectName("upTitleLabel")
                
        self.upInfoLabel = QtWidgets.QPushButton("")
        self.upInfoLabel.setObjectName("upInfoLabel")
        
        # add item in up layout 
        self.upLayout.addWidget(self.upTitleLabel,0,0,2,2)
        self.upLayout.addWidget(self.upInfoLabel,2,0,2,5)
        self.vSpace1 = QtWidgets.QPushButton("")
        self.vSpace1.setObjectName("upInfoLabel")
        self.upLayout.addWidget(self.vSpace1,4,0,1,5)
        #self.vSpace1 = QtWidgets.QSpacerItem(20,20,
        #                                     QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        #self.upLayout.addItem(self.vSpace1,4,0,1,1)
        
        # down widgets 
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
            QPushButton#upInfoLabel{
                border:none;
                font-size:22px;
                font-weight:700;
                font-family: Arial, Helvetica, sans-serif;
            }
            QPushButton#upTitleLabel{
                border:none;
                border-bottom: 1px solid white; 
                font-size:32px;
                font-weight:700;
                font-family: sans-serif,Arial, Helvetica;
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
    
    def connectAllSlots(self): 
        self.okayButton.clicked.connect(self.slotOkay)
        self.cancelButton.clicked.connect(self.slotCancel) 
    
    def slotOkay(self): 
        self.close()
        self.debug()
                
    def slotCancel(self): 
        self.close() 
        self.debug()
    
    def resizeEvent(self,event):
        pass    
    
    def setTitle(self,title = ""): 
        self.upTitleLabel.setText(title)
    
    def setInfo(self, info = ""): 
        self.upInfoLabel.setText(info)
    
    def debug(self): 
        pass 
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Ui_infoDialog()
    gui.setTitle("Information")
    gui.setInfo("This is a try.")
    gui.show()
    sys.exit(app.exec_())
        
        
        
    
    