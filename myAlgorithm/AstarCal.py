'''
# this file contains priority search code 
# finished by Ethan Lyu at 2019-10-16
# CopyRight Proteced  
'''
import sys 
import copy 
from queue import PriorityQueue as PQ

from PyQt5 import QtCore, QtGui , QtWidgets
from PyQt5.QtCore import QThread , pyqtSignal

class AStarCal():
    def __init__(self,mode=0): 
        self.mode = mode # 0 means 1 match , 1 means 2 match 
        self.openTable = PQ()
        self.tableIndex = 0 
        self.closeTable = [] 
        
        self.calPointNum = 0 
 
    def setMode(self,mode=0):
        self.mode = mode
       
    def judge(self,point): 
        num1 = self.getNum(point[0:14])
        num2 = self.getNum(point[14:28])
        num3 = self.getNum(point[28:49])
        
        if num1 == None or num2 == None or num3 == None: 
            return False # not a num 
        
        if point[49] == 0 : # '-'
            if (num1 - num2) == num3: 
                return True
            else: 
                return False
        elif point[49] ==1 : # '+'
            if (num1 + num2) == num3: 
                return True
            else: 
                return False
        elif point[49] == 2 : # '*' 
            if (num1 * num2) == num3 : 
                return True
            else: 
                return False 
        else: 
            print("Error:point[49] wrong num: " + point[49])
    def f(self,point):
        return self.g(point) + self.h(point) 
    def g(self,point): 
        return 0
    def h(self,point): 
        return self.mode + 1 - point[50]
        # if BFS , only need to set g = point[50], h = 0 
    
    def addAllClosePoints(self,point): 
        if point[50] > self.mode:
            # reach step limit 
            pass 
        else:
            if point[49]==2 and (self.mode-1) >= point[50]: 
                newPoint = copy.deepcopy(point)
                newPoint[49]=1
                newPoint[50] = newPoint[50] + 2     # here need to fix !!! if you have good hn and gn
                if not newPoint[:-1] in self.closeTable: 
                    self.openTable.put((self.f(newPoint),self.tableIndex,newPoint))
                    self.tableIndex = self.tableIndex + 1 
            
            if point[49]==1 and (self.mode-1) >= point[50]: 
                newPoint = copy.deepcopy(point)
                newPoint[49]=2
                newPoint[50] = newPoint[50] + 1 
                if not newPoint[:-1] in self.closeTable: 
                    self.openTable.put((self.f(newPoint),self.tableIndex,newPoint))
                    self.tableIndex = self.tableIndex + 1 
            
                             
            for i in range(50): 
                if point[i] == 1: 
                    for j in range(50): 
                        if point[j] == 0: 
                            newPoint = copy.deepcopy(point)
                            newPoint[i] = 0 
                            newPoint[j] = 1 
                            newPoint[50] = newPoint[50] + 1 
                            if not newPoint[:-1] in self.closeTable: 
                                self.openTable.put((self.f(newPoint),
                                                    self.tableIndex,
                                                    newPoint))  
                                self.tableIndex = self.tableIndex + 1  
                            # else: 
                            #     print("there is some point excluced")
                            #     print(newPoint)
    def getNum(self,numList): 
        if len(numList) == 14: 
            result = ''
            for i in range(7):
                result = result + str(numList[i]) 
                
            if result ==  "1111110": num1 = 0
            elif result == "0110000" : num1 = 1 
            elif result == "1101101" : num1 = 2 
            elif result == "1111001" : num1 = 3 
            elif result == "0110011" : num1 = 4 
            elif result == "1011011" : num1 = 5 
            elif result == "1011111" : num1 = 6 
            elif result == "1110000" : num1 = 7 
            elif result == "1111111" : num1 = 8 
            elif result == "1111011" : num1 = 9 
            elif result == "0000000" : num1 = 0    
            elif result == "0000001" : num1 = -1  # negative 
            else: # not recognizeable 
                return None
            
            result = ""
            for i in range(7,14): 
                result = result + str(numList[i])
                
            if result ==  "1111110": num2 = 0
            elif result == "0110000" : num2 = 1 
            elif result == "1101101" : num2 = 2 
            elif result == "1111001" : num2 = 3 
            elif result == "0110011" : num2 = 4 
            elif result == "1011011" : num2 = 5 
            elif result == "1011111" : num2 = 6 
            elif result == "1110000" : num2 = 7 
            elif result == "1111111" : num2 = 8 
            elif result == "1111011" : num2 = 9 
            else:  # not recognizeable 
                return None
            
            if num1 < 0: 
                num = -1 * num2
            else: 
                num = num1*10 + num2   
                
            return num  
    
        elif len(numList) == 21: 
            result = ""
            for i in range(7): 
                result = result + str(numList[i])
                
            if result ==  "1111110": num1 = 0
            elif result == "0110000" : num1 = 1 
            elif result == "1101101" : num1 = 2 
            elif result == "1111001" : num1 = 3 
            elif result == "0110011" : num1 = 4 
            elif result == "1011011" : num1 = 5 
            elif result == "1011111" : num1 = 6 
            elif result == "1110000" : num1 = 7 
            elif result == "1111111" : num1 = 8 
            elif result == "1111011" : num1 = 9 
            elif result == "0000000" : num1 = 0    
            elif result == "0000001" : num1 = -1  # negative 
            else: # not recognizeable 
                return None 
            
            result = ""
            for i in range(7,14): 
                result = result + str(numList[i])
                
            if result ==  "1111110": num2 = 0
            elif result == "0110000" : num2 = 1 
            elif result == "1101101" : num2 = 2 
            elif result == "1111001" : num2 = 3 
            elif result == "0110011" : num2 = 4 
            elif result == "1011011" : num2 = 5 
            elif result == "1011111" : num2 = 6 
            elif result == "1110000" : num2 = 7 
            elif result == "1111111" : num2 = 8 
            elif result == "1111011" : num2 = 9 
            elif result == "0000000" : num2 = 0    
            elif result == "0000001" : num2 = -1  # negative 
            else: # not recognizeable 
                return None 
            
            result = ""
            for i in range(14,21): 
                result = result + str(numList[i])
                
            if result ==  "1111110": num3 = 0
            elif result == "0110000" : num3 = 1 
            elif result == "1101101" : num3 = 2 
            elif result == "1111001" : num3 = 3 
            elif result == "0110011" : num3 = 4 
            elif result == "1011011" : num3 = 5 
            elif result == "1011111" : num3 = 6 
            elif result == "1110000" : num3 = 7 
            elif result == "1111111" : num3 = 8 
            elif result == "1111011" : num3 = 9    
            else: # not recognizeable 
                return None 
            
            if num1 < 0 :
                num = -1 *(num2*10 + num3)
            elif num2 < 0:
                num = -1 * num3 ; 
            else: 
                num = num1*100 + num2*10 + num3
                
            return num  
    def getAnswer(self,num1=0,num2=0,num3=0,symbol='+'):
        initstr = ""
        if num1 > 0:
            num1Digit1 = int(num1/10)
            num1Digit2 = num1 % 10 
             
            if num1Digit1 == 0: 
                initstr = initstr +  "0000000"
            elif num1Digit1 == 1 : 
                initstr = initstr +  "0110000"
            elif num1Digit1 == 2 : 
                initstr = initstr +  "1101101"
            elif num1Digit1 == 3 : 
                initstr = initstr +  "1111001"
            elif num1Digit1 == 4 : 
                initstr = initstr +  "0110011"
            elif num1Digit1 == 5 :
                initstr = initstr +  "1011011"
            elif num1Digit1 == 6 : 
                initstr = initstr +  "1011111"
            elif num1Digit1 == 7 : 
                initstr = initstr +  "1110000"
            elif num1Digit1 == 8 : 
                initstr = initstr +  "1111111"
            elif num1Digit1 == 9 : 
                initstr = initstr +  "1111011"   
                
            if num1Digit2 == 0: 
                initstr = initstr +  "1111110"
            elif num1Digit2 == 1 : 
                initstr = initstr +  "0110000"
            elif num1Digit2 == 2 : 
                initstr = initstr +  "1101101"
            elif num1Digit2 == 3 : 
                initstr = initstr +  "1111001"
            elif num1Digit2 == 4 : 
                initstr = initstr +  "0110011"
            elif num1Digit2 == 5 :
                initstr = initstr +  "1011011"
            elif num1Digit2 == 6 : 
                initstr = initstr +  "1011111"
            elif num1Digit2 == 7 : 
                initstr = initstr +  "1110000"
            elif num1Digit2 == 8 : 
                initstr = initstr +  "1111111"
            elif num1Digit2 == 9 : 
                initstr = initstr +  "1111011"   
        else: 
            initstr = initstr + "0000001"
            
            num1Digit1 = abs(num1)
            if num1Digit1 == 0: 
                initstr = initstr +  "1111110"
            elif num1Digit1 == 1 : 
                initstr = initstr +  "0110000"
            elif num1Digit1 == 2 : 
                initstr = initstr +  "1101101"
            elif num1Digit1 == 3 : 
                initstr = initstr +  "1111001"
            elif num1Digit1 == 4 : 
                initstr = initstr +  "0110011"
            elif num1Digit1 == 5 :
                initstr = initstr +  "1011011"
            elif num1Digit1 == 6 : 
                initstr = initstr +  "1011111"
            elif num1Digit1 == 7 : 
                initstr = initstr +  "1110000"
            elif num1Digit1 == 8 : 
                initstr = initstr +  "1111111"
            elif num1Digit1 == 9 : 
                initstr = initstr +  "1111011"      
    
        if num2 > 0:
            num2Digit1 = int(num2/10)
            num2Digit2 = num2 % 10 
             
            if num2Digit1 == 0: 
                initstr = initstr +  "0000000"
            elif num2Digit1 == 1 : 
                initstr = initstr +  "0110000"
            elif num2Digit1 == 2 : 
                initstr = initstr +  "1101101"
            elif num2Digit1 == 3 : 
                initstr = initstr +  "1111001"
            elif num2Digit1 == 4 : 
                initstr = initstr +  "0110011"
            elif num2Digit1 == 5 :
                initstr = initstr +  "1011011"
            elif num2Digit1 == 6 : 
                initstr = initstr +  "1011111"
            elif num2Digit1 == 7 : 
                initstr = initstr +  "1110000"
            elif num2Digit1 == 8 : 
                initstr = initstr +  "1111111"
            elif num2Digit1 == 9 : 
                initstr = initstr +  "1111011"   
                
            if num2Digit2 == 0: 
                initstr = initstr +  "1111110"
            elif num2Digit2 == 1 : 
                initstr = initstr +  "0110000"
            elif num2Digit2 == 2 : 
                initstr = initstr +  "1101101"
            elif num2Digit2 == 3 : 
                initstr = initstr +  "1111001"
            elif num2Digit2 == 4 : 
                initstr = initstr +  "0110011"
            elif num2Digit2 == 5 :
                initstr = initstr +  "1011011"
            elif num2Digit2 == 6 : 
                initstr = initstr +  "1011111"
            elif num2Digit2 == 7 : 
                initstr = initstr +  "1110000"
            elif num2Digit2 == 8 : 
                initstr = initstr +  "1111111"
            elif num2Digit2 == 9 : 
                initstr = initstr +  "1111011"   
        else: 
            initstr = initstr + "0000001"
            
            num2Digit1 = abs(num2)
            if num2Digit1 == 0: 
                initstr = initstr +  "1111110"
            elif num2Digit1 == 1 : 
                initstr = initstr +  "0110000"
            elif num2Digit1 == 2 : 
                initstr = initstr +  "1101101"
            elif num2Digit1 == 3 : 
                initstr = initstr +  "1111001"
            elif num2Digit1 == 4 : 
                initstr = initstr +  "0110011"
            elif num2Digit1 == 5 :
                initstr = initstr +  "1011011"
            elif num2Digit1 == 6 : 
                initstr = initstr +  "1011111"
            elif num2Digit1 == 7 : 
                initstr = initstr +  "1110000"
            elif num2Digit1 == 8 : 
                initstr = initstr +  "1111111"
            elif num2Digit1 == 9 : 
                initstr = initstr +  "1111011"      
    
        if num3 > 0: 
            num3Digit1 = int(num3/100)
            num3Digit2 = int((num3%100)/10)
            num3Digit3 = num3%10 
            
            if num3Digit1 == 0: 
                initstr = initstr +  "0000000"
            elif num3Digit1 == 1 : 
                initstr = initstr +  "0110000"
            elif num3Digit1 == 2 : 
                initstr = initstr +  "1101101"
            elif num3Digit1 == 3 : 
                initstr = initstr +  "1111001"
            elif num3Digit1 == 4 : 
                initstr = initstr +  "0110011"
            elif num3Digit1 == 5 :
                initstr = initstr +  "1011011"
            elif num3Digit1 == 6 : 
                initstr = initstr +  "1011111"
            elif num3Digit1 == 7 : 
                initstr = initstr +  "1110000"
            elif num3Digit1 == 8 : 
                initstr = initstr +  "1111111"
            elif num3Digit1 == 9 : 
                initstr = initstr +  "1111011" 
            
            if num3Digit2 == 0: 
                if num3Digit1 == 0: 
                    initstr = initstr +  "0000000"
                else: 
                    initstr = initstr + "1111110"
            elif num3Digit2 == 1 : 
                initstr = initstr +  "0110000"
            elif num3Digit2 == 2 : 
                initstr = initstr +  "1101101"
            elif num3Digit2 == 3 : 
                initstr = initstr +  "1111001"
            elif num3Digit2 == 4 : 
                initstr = initstr +  "0110011"
            elif num3Digit2 == 5 :
                initstr = initstr +  "1011011"
            elif num3Digit2 == 6 : 
                initstr = initstr +  "1011111"
            elif num3Digit2 == 7 : 
                initstr = initstr +  "1110000"
            elif num3Digit2 == 8 : 
                initstr = initstr +  "1111111"
            elif num3Digit2 == 9 : 
                initstr = initstr +  "1111011"    
            
            if num3Digit3 == 0: 
                initstr = initstr +  "1111110"
            elif num3Digit3 == 1 : 
                initstr = initstr +  "0110000"
            elif num3Digit3 == 2 : 
                initstr = initstr +  "1101101"
            elif num3Digit3 == 3 : 
                initstr = initstr +  "1111001"
            elif num3Digit3 == 4 : 
                initstr = initstr +  "0110011"
            elif num3Digit3 == 5 :
                initstr = initstr +  "1011011"
            elif num3Digit3 == 6 : 
                initstr = initstr +  "1011111"
            elif num3Digit3 == 7 : 
                initstr = initstr +  "1110000"
            elif num3Digit3 == 8 : 
                initstr = initstr +  "1111111"
            elif num3Digit3 == 9 : 
                initstr = initstr +  "1111011"        
        else: 
            if num3 <= -10:
                initstr = initstr + "0000001"
                num3Digit2 = int(abs(num3)/10)
                num3Digit3 = abs(num3) % 10 
            
                if num3Digit2 == 0: 
                    initstr = initstr + "1111110"
                elif num3Digit2 == 1 : 
                    initstr = initstr +  "0110000"
                elif num3Digit2 == 2 : 
                    initstr = initstr +  "1101101"
                elif num3Digit2 == 3 : 
                    initstr = initstr +  "1111001"
                elif num3Digit2 == 4 : 
                    initstr = initstr +  "0110011"
                elif num3Digit2 == 5 :
                    initstr = initstr +  "1011011"
                elif num3Digit2 == 6 : 
                    initstr = initstr +  "1011111"
                elif num3Digit2 == 7 : 
                    initstr = initstr +  "1110000"
                elif num3Digit2 == 8 : 
                    initstr = initstr +  "1111111"
                elif num3Digit2 == 9 : 
                    initstr = initstr +  "1111011"    
            
                if num3Digit3 == 0: 
                    initstr = initstr +  "1111110"
                elif num3Digit3 == 1 : 
                    initstr = initstr +  "0110000"
                elif num3Digit3 == 2 : 
                    initstr = initstr +  "1101101"
                elif num3Digit3 == 3 : 
                    initstr = initstr +  "1111001"
                elif num3Digit3 == 4 : 
                    initstr = initstr +  "0110011"
                elif num3Digit3 == 5 :
                    initstr = initstr +  "1011011"
                elif num3Digit3 == 6 : 
                    initstr = initstr +  "1011111"
                elif num3Digit3 == 7 : 
                    initstr = initstr +  "1110000"
                elif num3Digit3 == 8 : 
                    initstr = initstr +  "1111111"
                elif num3Digit3 == 9 : 
                    initstr = initstr +  "1111011"  
            
            else: 
                initstr = initstr + "0000000"
                initstr = initstr + "0000001"
                
                num3Digit3 = abs(num3)
                if num3Digit3 == 0: 
                    initstr = initstr +  "1111110"
                elif num3Digit3 == 1 : 
                    initstr = initstr +  "0110000"
                elif num3Digit3 == 2 : 
                    initstr = initstr +  "1101101"
                elif num3Digit3 == 3 : 
                    initstr = initstr +  "1111001"
                elif num3Digit3 == 4 : 
                    initstr = initstr +  "0110011"
                elif num3Digit3 == 5 :
                    initstr = initstr +  "1011011"
                elif num3Digit3 == 6 : 
                    initstr = initstr +  "1011111"
                elif num3Digit3 == 7 : 
                    initstr = initstr +  "1110000"
                elif num3Digit3 == 8 : 
                    initstr = initstr +  "1111111"
                elif num3Digit3 == 9 : 
                    initstr = initstr +  "1111011"  
        
        initPoint = []
        for s in initstr: 
            initPoint.append(int(s))
            
        if symbol == '+':
            initPoint.append(1)
        elif symbol == '-':
            initPoint.append(0)
        elif symbol == '*': 
            initPoint.append(2)
        
        initPoint.append(0)        
        
        if len(initPoint) != 51: 
            print("Error: len of init point: " + str(len(initPoint)))
            print(initPoint)
        
        resultPoint = self.solve(initPoint)
        return resultPoint               
    def solve(self,initPoint): 
        self.openTable.put((0,self.tableIndex,initPoint))
        self.tableIndex = self.tableIndex + 1 
        
        while not self.openTable.empty(): 
            point = self.openTable.get()[2]
            if self.judge(point) == True: 
                print("find the answer!")
                self.openTable=PQ()
                self.calPointNum = self.tableIndex
                self.tableIndex = 0 
                self.closeTable=[]
                return point
            else: 
                self.closeTable.append(point[:-1])
                self.addAllClosePoints(point) 
                        
        print("no answer")
        self.openTable = PQ()
        self.calPointNum = self.tableIndex
        self.tableIndex = 0 
        self.closeTable = [] 
        return None 
    
class CalThread(QThread,AStarCal): 
    trigger = pyqtSignal()
    
    def __init__(self,num1=0,num2=0,num3=0,symbol='+', parent=None):
        super().__init__(parent=parent)
        self.threadNums = [num1,num2,num3]
        self.threadSymbol = symbol 
        self.threadResultPoint = []
        
    def __del__(self): 
        self.wait()
        
    def run(self): 
        self.threadResultPoint = self.getAnswer(self.threadNums[0],
                                self.threadNums[1],self.threadNums[2],self.threadSymbol)
        print(self.threadResultPoint)
        self.trigger.emit()  

# program for test algorithm         
# if __name__ == "__main__":
#     ai = AStarCal() 
#     ai.setMode(1)
    
#     resultPoint = ai.getAnswer(18,24,981,'*')
    
#     if resultPoint != None: 
#         num1 = ai.getNum(resultPoint[0:14])
#         num2 = ai.getNum(resultPoint[14:28])
#         num3 = ai.getNum(resultPoint[28:49])
        
#         if resultPoint[49] == 0:
#             symbol = '-'
#         elif resultPoint[49] == 1: 
#             symbol = '+'
#         elif resultPoint[49] == 2: 
#             symbol = '*'
            
#         print(str(num1)+symbol+str(num2)+"="+str(num3))
#     else: 
#         print("no answer")

# program for test thread usage 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    ai = AStarCal()
    resultPoint = ai.getAnswer(3,49,142,'+')
    ai.setMode(0)
        
    #th = CalThread(num1= 25, num2= -70,num3= -1,symbol='-')
    #th.isRunning()
    # th.mode = 1 
    # th.start() 
    # sys.exit(app.exec_())