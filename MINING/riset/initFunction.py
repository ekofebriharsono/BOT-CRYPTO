import os
import time

dataMiner = []
dataCoin = []

def addDataCoin(name):
    data = [name]
    dataCoin.append(data)

def generateCommand(coin):
    resultCommand = "nohup python -u public_html/"+coin+"/"+coin+".py &"
    return resultCommand

def startMining(data):
    for coin in data:
        command = generateCommand(coin[0])
        resultCommand = os.system(command)
        if resultCommand == 0 :
            print("Running " + coin[0])
        else :
            print("Failed " + coin[0])
        time.sleep(1)
        print("=======================")
        
def seeMonitor():
    os.system("ps aux")