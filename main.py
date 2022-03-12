from asyncio.windows_events import NULL
from gettext import NullTranslations
import numpy as np
import cv2
import pyautogui
import discord
import json
from tkinter import *
window = Tk()
window.title("Fortnite")
send = NULL
def screenshot():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
    cv2.imwrite("./output/code.png", image)


def start():
    print('not working')
def display():
    if(sendtodiscord.get()==1):
        print(1)
    else:
        print(0)
def locatecode():
        seecode = pyautogui.locateOnScreen('./input/portuguese/inicialcode.png', confidence=.7)
        if seecode == None:
            print(seecode)
        else:
            print(seecode)
            print('Found')
            screenshot()
            code2 = False
            global send
            send = False
        
def sendtodiscord():
    @bot.event
    async def on_ready():
        global send
        if send == False:
            channel = bot.get_channel()
            await channel.send(file = discord.File("./output/code.png"))
        
def config():
    def submit():
        token = entrytoken.get()
        channel1 = channel.get()
        entrytoken.config(state=DISABLED)
        channel.config(state=DISABLED)
        if token is None:
            print('f')
        if channel1 is None:
            print('f32424')
        tokenchanneltoput = {"token": token,"channel": channel1}
        jsonString = json.dumps(tokenchanneltoput)
        jsonFile = open("data/data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        window_config.destroy()
    window_config = Tk()
    entrytoken = Entry(window_config,
              font=("Arial",15),
              fg="#000000",
              show="*"
              )

    entrytoken.pack(side=LEFT)
    channel = Entry(window_config,
              font=("Arial",15),
              fg="#000000",
              show="*"
              )
    channel.pack(side=LEFT)
    submit_button = Button(window_config,text="submit",command=submit)
    submit_button.pack(side=RIGHT)


sendtodiscord = IntVar()
Button(window,text="config",command=config).pack()

start = Button(window,text="start",command=locatecode)
start.pack()

check_button = Checkbutton(window,
                           text="Send to discord",
                           variable=sendtodiscord,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial',12),
                           compound='left')
check_button.pack()

bot = discord.Client()
f = open ('data/data.json', "r+")
datas = json.loads(f.read())
token1 = datas["token"]
token = token1
channel1 = datas["channel"]
channel = channel1
#bot.run(token)
window.mainloop()
