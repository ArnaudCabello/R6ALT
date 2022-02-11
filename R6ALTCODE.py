from asyncio.windows_events import NULL
from cgitb import text
from distutils.command.config import config
from pickle import EMPTY_LIST
import subprocess
from tkinter import filedialog
import pyautogui, time
from tkinter import *
from tkinter import filedialog as fd
import os

root = Tk()
root.title('R6')
root.geometry("600x400")

def save(listPath):
    f = open("R6ALT PATHS", "w")
    f.truncate(0);
    f.seek(0)
    i = 0
    while (i < 3):
        f.write(listPath[i])
        f.write('\n')
        i+=1
    f.close()

def uploadFile(listPath):
    file = fd.askopenfilename()
    listPath.append(file)
    print(listPath)
    

def getChoices(lines,count):
    display = []
    i = 0
    while(i<(count)):
        display.append(lines[i])
        i+=4
    return display

def selection(lines,count,ubiPath,iniPath):
    i = 0;
    accinfo =[]
    while(i < count):
        if(lines[i] == variable.get()):
            accinfo.append(lines[i+1])
            accinfo.append(lines[i+2])
            accinfo.append(lines[i+3])
            break
        i += 1

    gameSettings = []

    dataCenter = "DataCenterHint=playfab/" + serverVar.get() + "\n"

    end = "\\GameSettings.ini"

    subString = accinfo[2][0:36]

    temp = iniPath + subString + end
    print(temp)
    textFile = open(temp, "r+")
    gameSettings = textFile.readlines()
    count = 0
    for line in gameSettings:
        count += 1
    textFile.truncate(0);
    textFile.seek(0)
    i = 0
    while(i < count):
        if(len(gameSettings[i]) > 13):
            if(gameSettings[i][0:15] == "DataCenterHint="):
                print("in the loop")
                gameSettings[i] = dataCenter
        textFile.write(gameSettings[i])
        i+=1
    textFile.close()
    subprocess.Popen([ubiPath])
    time.sleep(10)
    pyautogui.write(accinfo[0]) 
    pyautogui.moveTo(1000, 550) 
    pyautogui.click()
    pyautogui.write(accinfo[1])
    pyautogui.moveTo(1250, 710) 
    pyautogui.click()
    return accinfo

configFile = os.getcwd()
configFile = configFile + "\R6ALT PATHS"
print(configFile)

configLines = []
with open(configFile,"r") as f:
    configLines = f.readlines()
    count = 0
    for configLine in configLines:
         count += 1
if len(configLines) > 0:

    ubiPath = configLines[0]
    ubiPath = ubiPath[0:(len(ubiPath)-1)]
    userInfo = configLines[1]
    userInfo = userInfo[0:(len(userInfo)-1)]
    iniPath = configLines[2]
    iniPath = iniPath[0:(len(iniPath)-54)]

    lines = []
    with open(userInfo,"r") as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            count += 1

    choices = getChoices(lines,count)
    variable = StringVar(root)
    variable.set('Select An Account')

    account = OptionMenu(root, variable, *choices)

    serverOptions = ["eastus" , "westus", "centralus", "southcentralus"]
    serverVar = StringVar(root)
    serverVar.set('Select A Server')

    server = OptionMenu(root, serverVar, *serverOptions)

    account.pack();

    server.pack();


    button_1 = Button(root,text="Select", padx = 50, pady = 20, command=lambda: selection(lines,count,ubiPath,iniPath))
    button_1.place(x=250, y = 320)
else:
    listPath = []
    myFont1 = ('times',12,'bold')
    root.title("Settings")
    l5 = Label(root, text = 'First Time Setup Configure Files',width=30, font = myFont1)
    l5.pack(ipadx= 100, ipady = 10)
    root.geometry("400x400")

    l1 = Label(root, text = 'File path to Ubisoft Connect Launcher',width=30, font = myFont1)
    l1.pack(ipadx= 100, ipady = 10)
    b1 = Button(root,text='File path to Ubisoft Connect Launcher', width=30,command=lambda:uploadFile(listPath)).pack()

    l2 = Label(root, text = 'File path to R6ALT info',width=30, font = myFont1)
    l2.pack(ipadx= 100, ipady = 10)
    b2 = Button(root,text='File path to R6ALT info', width=30,command=lambda:uploadFile(listPath)).pack()

    l3 = Label(root, text = 'File path to game ini file',width=30, font = myFont1)
    l3.pack(ipadx= 100, ipady = 10)
    b3 = Button(root,text='File path to game ini file', width=30,command=lambda:uploadFile(listPath)).pack()

    btnSave = Button(root, text = "Save", command=lambda:save(listPath)).pack()
    btnClose = Button(root, text = "close window", command=root.destroy).pack()
        

root.mainloop()