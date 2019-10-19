import os

matchData1 = [
    ["7","+","7","=","9"],
    ["2","+","18","=","15"],
    ["78","+","11","=","89"],
    ["1","+","1","=","8"],
    ["23","-","11","=","6"],
    ["3","-","14","=","-6"],
    ["15","*","4","=","52"]
]

matchData2 = [
    []
]

## return basic info UI need 
def basicInfo(): 
    picPath = os.path.abspath('.') + "\\myUI\\image\\"
    return [picPath] 