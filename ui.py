from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import textwrap
############COPY CODE AI##############
from aift import setting
setting.set_api_key('WKg1RaHAFQdrfFjrsLosdGbBxRSllGVk')
from aift.multimodal import textqa 
###########TEXT TO SPEECH###############
import requests
import pygame
import time
import os
import random
def generatesound(text='ข้าวมันไก่'):

    #ระบุ api key
    Apikey='WKg1RaHAFQdrfFjrsLosdGbBxRSllGVk'
    
    #ระบุเสียงที่ต้องการ
    speaker = "nana"
    
    #สังเคราะห์เสียง
    url = 'https://api.aiforthai.in.th/vaja'
    headers = {'Apikey':Apikey,'Content-Type' : 'application/json'}
    # text = 'ข้าวมันไก่'
    data = {
    "text": text,
    "speaker" : speaker
    }
    response = requests.post(url, json=data, headers=headers)
    print(response.json())
    
    # ดาวน์โหลดไฟล์เสียง
    resp = requests.get(response.json()['audio_url'],headers={'Apikey':Apikey})
    if resp.status_code == 200:
        randomname = str(random.randint(100000,999999))
        randomname = f'{randomname}.wav'
        with open(randomname, 'wb') as a:
            a.write(resp.content)
            print('Downloaded: ')
    else:
        print(resp.reason)
    return randomname

import pygame

def playsound(name):

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

##########################

GUI = Tk()
GUI.title('โปรแกรมช่วยคิดเมนูอาหารวันนี้ by ลุง') # ชื่อโปรแกรม
GUI.geometry('700x600') # ปรับขนาดหน้าจอ
GUI.state('zoomed')
style = ttk.Style() # สร้างสไตล์
style.configure('My.TButton', font=('TH Sarabun New', 24)) # ขนาดฟอนต์

def AIreply():
    print('ai กำลังตอบ')
    result = textqa.generate('กินอะไรดีเที่ยงนี้? ตอบสั้นๆ')
    text = result['content']
    wrapped_text = textwrap.fill(text, width=50)
    v_result.set(wrapped_text)
    
    name = generatesound(text)
    playsound(name)
    

B1 = ttk.Button(GUI, text='วันนี้กินอะไรดี?', style='My.TButton',command=AIreply)
B1.pack(pady=30,ipadx=30, ipady=20)

v_text = StringVar()

E1 = ttk.Entry(GUI, textvariable=v_text, font=(None,30))
E1.pack(pady=20)

def Send():
    textinput = v_text.get()
    print('ai กำลังตอบ')
    result = textqa.generate(textinput)
    text = result['content']
    wrapped_text = textwrap.fill(text, width=50)
    v_result.set(wrapped_text)
    
    name = generatesound(text)
    playsound(name)


B2 = ttk.Button(GUI,text='Submit', style='My.TButton', command=Send)
B2.pack(pady=20)


v_result = StringVar()
v_result.set('-----output-----')
L1 = ttk.Label(GUI,textvariable=v_result,font=(None,40))
L1.pack()

GUI.mainloop()
