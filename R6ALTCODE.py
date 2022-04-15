from distutils import command
import subprocess
import pyautogui, time
from tkinter import *

root = Tk()
root.title('R6')
root.geometry("600x400")

def getChoices(lines,count):
    display = []
    i = 0
    while(i<(count)):
        display.append(lines[i])
        i+=4
    return display

def selection(lines,count):
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

    start = "C:\\Users\\Arnaud Cabello\\OneDrive\\Documents\\My Games\\Rainbow Six - Siege\\"

    end = "\\GameSettings.ini"

    subString = accinfo[2][0:36]

    temp = start + subString + end
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
                gameSettings[i] = dataCenter
        textFile.write(gameSettings[i])
        i+=1
    textFile.close()
    subprocess.Popen([r'C:\Program Files (x86)\Ubisoft\Ubisoft Game Launcher\UbisoftConnect.exe'])
    time.sleep(10)
    pyautogui.write(accinfo[0]) 
    pyautogui.moveTo(1000, 550) 
    pyautogui.click()
    pyautogui.write(accinfo[1])
    pyautogui.moveTo(1250, 710) 
    pyautogui.click()
    return accinfo


lines = []
with open(r'C:\Users\Arnaud Cabello\OneDrive\Desktop\R6 ALT\username.txt') as f:
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


button_1 = Button(root,text="Select", padx = 50, pady = 20, command=lambda: selection(lines,count))
button_1.place(x=250, y = 320)
root.mainloop()