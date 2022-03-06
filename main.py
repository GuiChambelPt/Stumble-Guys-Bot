import numpy as np
import cv2
import pyautogui
import discord
import json
f = open ('data/data.json', "r+")
token2 = json.loads(f.read())
token1 = token2["token"]

from tkinter import *
bot = discord.Client()
code = False


def screenshot():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
    cv2.imwrite("./output/code.png", image)

while code == True:
    group = pyautogui.locateOnScreen('./input/portuguese/group.png', confidence=.6)
    if group == None:
        print('Not found')
    else: 
        pyautogui.moveTo(group, duration=.1)
        pyautogui.click(interval=.3)
        print('Found')
        code = False
        code1 = True
    

while code1 == True:
    create = pyautogui.locateOnScreen('./input/portuguese/create.png', confidence=.6)
    if create == None:
        print('Not Found')
    else: 
        pyautogui.moveTo(create, duration=.1)
        pyautogui.click(interval=.3)
        print('Found')
        code1 = False
        code2 = True

while code2 == True:
    seecode = pyautogui.locateOnScreen('./input/portuguese/inicialcode.png', confidence=.7)
    if seecode is None:
        print('Dont Found')
    else:
        print('Found')
        screenshot()
        code2 = False
        send = False
        loading = True

while loading == True:
    loading2 = pyautogui.locateOnScreen('./input/portuguese/loading.png', confidence=.7)
    if seecode is None:
        print('Dont Found')
    else:
        print('Found match')
        loading2 = False
        icy = True
        
@bot.event
async def on_ready():
    if send == False:
        channel = bot.get_channel(channeltosend)
        await channel.send(file = discord.File("./output/code.png"))
        





window = Tk()
window.title("Fortnite")
mapa = None


def display():
    if(x1.get()==1):
        print(1)
    else:
        print(0)

def submit():
    token = entrytoken.get()
    entrytoken.config(state=DISABLED)
    tokentoput = {"token": token}
    jsonString = json.dumps(tokentoput)
    jsonFile = open("data/data.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
x1 = IntVar()

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x1,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial',20),
                           compound='left')
check_button.pack()



entrytoken = Entry(window,
              font=("Arial",50),
              fg="#00FF00",
              bg="black",
              show="*"
              )

entrytoken.pack(side=LEFT)

submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)

window.mainloop()

bot.run(token1)