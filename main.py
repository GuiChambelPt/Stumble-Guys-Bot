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
    cv2.imwrite("code.png", image)

while code == True:
    seecode = pyautogui.locateOnScreen('./input/inicialcode.png', confidence=.7)
    if seecode is None:
        print('Dont Found')
    else:
        print('Found')
        screenshot()
        code = False

@bot.event
async def on_ready():
    if code == False:
        channel = bot.get_channel(channeltosend)
        await channel.send(file = discord.File("./output/code.png"))
        quit()

        
bot.run(token)

