import os 


## return basic info UI need 
def basicInfo(): 
    picPath = os.path.abspath('.') + "\\myUI\\image\\"
    return [picPath] 


if __name__ == "__main__":
    print(basicInfo())