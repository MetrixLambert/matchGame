'''
# this is the file for transfer correct equation 
# finished by Ethan Lyu on 2019-10-17
# CopyRight Protected 
'''
import sys 
import copy 
import random 

from queue import PriorityQueue as PQ 
from PyQt5.QtCore import QThread , pyqtSignal
from PyQt5 import QtGui, QtCore, QtWidgets

class transEquation(): 
    def __init__(self, mode = 0 ):
        self.mode = mode
        self.openTable = PQ()
        self.openTableIndex = 0 
        self.closeTable = []
        
    def setMode(self, mode = 0 ): 
        self.mode = mode 
        
    def judge(self,initPoint, point): 
        if point[50] != self.mode + 1 : 
            return False
        # only miss one point 
        diff = self.diff(initPoint,point)
        if diff!=(self.mode + 1):
            return False 
        
        # check if high digit is 0 
        num1 = self.getNum(point[0:14])
        num2 = self.getNum(point[14:28])
        num3 = self.getNum(point[28:49])
        
        if num1 != None and num2 != None and num3 != None: 
            if self.getInitPoint(num1,num2,num3,symbol='+')[0:49] != point[0:49]:
                # check if high digit is zero 
                return False
            else: 
                return True
        else: 
            return False 
    
    def diff(self,point1,point2):
        result = 0 
        for i in range(49): 
            if point1[i] != point2[i]: 
                result = result + 1 
        
        if point1[50] != point2[50]:        
            if point1[50] == 2 and point2[50] == 1: 
                result = result + 4
            elif point1[50] == 1 and point2[50] ==2: 
                result = result + 4 
            else:     
                result = result + 1 
                
        result = int(result/2)
        
        return result 
        
    def getInitPoint(self,num1,num2,num3,symbol): 
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
           
        if symbol == '+' or symbol == 1:
            initPoint.append(1)
        elif symbol == '-' or symbol == 0 :
            initPoint.append(0)
        elif symbol == '*' or symbol == 2: 
            initPoint.append(2)
        
        initPoint.append(0) 
        
        # check 
        if len(initPoint) !=51: 
            print("init Point Len error!: ")
            print(len(initPoint))
            print(initPoint)
            print("num")
            print(num1,num2,num3)
            print("symbol")
            print(symbol)
        
        return initPoint 
    
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
 
    def transfer(self, num1,num2,num3,symbol): 
        initPoint = self.getInitPoint(num1,num2,num3,symbol)
        print("Transfer Init: ", num1,num2,symbol,"=",num3)
        resultPoint = self.solve(initPoint)
        if resultPoint == None: 
            return None
        else: 
            num1 = self.getNum(resultPoint[0:14])
            num2 = self.getNum(resultPoint[14:28])
            num3 = self.getNum(resultPoint[28:49])
            
            if resultPoint[49] == 0: 
                symbol = '-'
            elif resultPoint[49] == 1: 
                symbol = '+'
            elif resultPoint[49] == 2: 
                symbol = '*'

            print("Transfer result: ",num1,num2,symbol,"=",num3)
            return [num1,num2,num3,symbol] 
    
    def solve(self, initPoint): 
        self.openTable.put((0,self.openTableIndex,initPoint))
        self.openTableIndex = self.openTableIndex + 1 
        
        while not self.openTable.empty(): 
            point = self.openTable.get()[2]
            if self.judge(initPoint,point) == True: 
                self.openTable = PQ()
                self.openTableIndex = 0  
                self.closeTable = [] 
                return point 
            else: 
                self.closeTable.append(point[:-1])
                self.addAllClosePoint(point)

        self.openTable = PQ() 
        self.openTableIndex = 0 
        self.closeTable = [] 
        return None
        
    def addAllClosePoint(self,point): 
        if point[50] > self.mode: 
            # reach step limit 
            pass 
        else: 
            if point[49] == 2 and self.mode - point[50] >= 1 : 
                newPoint = copy.deepcopy(point)
                newPoint[49] = 1 
                newPoint[50] = newPoint[50] + 2 
                if not newPoint[:-1] in self.closeTable: 
                    self.openTable.put((self.f(newPoint),self.openTableIndex,newPoint))
                    self.openTableIndex = self.openTableIndex + 1 
            
            if point[49] == 1 and self.mode - point[50] >= 1 : 
                newPoint = copy.deepcopy(point)
                newPoint[49] = 2 
                newPoint[50] = newPoint[50] + 2 
                if not newPoint[:-1] in self.closeTable: 
                    self.openTable.put((self.f(newPoint),self.openTableIndex,newPoint))
                    self.openTableIndex = self.openTableIndex + 1 
                    
            for i in range(50): 
                if point[i] == 1 : 
                    for j in range(50): 
                        if point[j] == 0 :
                            newPoint = copy.deepcopy(point)
                            newPoint[i] = 0 
                            newPoint[j] = 1 
                            newPoint[50] = newPoint[50] + 1

                            if not newPoint[:-1] in self.closeTable: 
                                self.openTable.put((self.f(newPoint),
                                                    self.openTableIndex,newPoint)) 
                                self.openTableIndex = self.openTableIndex + 1        
            
    def f(self,point): 
        return self.g(point) + self.h(point) 
    
    def g(self, point): 
        return 0
    
    def h(self,point): 
        # for DFS 
        #return self.mode + 1 - point[50]
        # for random search 
        return random.randint(0,10000)

class transThread(QThread,transEquation): 
    trigger = pyqtSignal()
    
    def __init__(self, mode=0, num1=0, num2=0, num3=0, symbol='+',parent=None):
        super().__init__(parent = parent)
        
        self.threadNums = [num1,num2,num3] 
        self.threadSymbol = symbol 
        self.threadResult = [] 
        
    def __del__(self): 
        self.wait() 
        
    def run(self): 
        self.threadResult = self.transfer(self.threadNums[0],
                                self.threadNums[1],self.threadNums[2],
                                self.threadSymbol)
        print(self.threadResult)
        self.trigger.emit()

    
if __name__ == '__main__':
    t = transEquation() 
    result = t.transfer(93,49,142,'+')
    print(result)
    
    