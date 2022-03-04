import numpy as np
import cv2
import pyautogui
import discord
from config import channeltosend, token
bot = discord.Client()
code = True


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

@bot.event
async def on_ready():
    if send == False:
        channel = bot.get_channel(channeltosend)
        await channel.send(file = discord.File("./output/code.png"))
        

while loading == True:
    loading2 = pyautogui.locateOnScreen('./input/portuguese/loading.png', confidence=.7)
    if seecode is None:
        print('Dont Found')
    else:
        print('Found match')
        loading2 = False
        icy = True
        
while icy == True:
    icyhe = pyautogui.locateOnScreen('./input/portuguese/icyheights.png', confidence=.7)
    if seecode is None:
        print('Dont Found')
    else:
        print('Found match')
        icy = False



bot.run(token)