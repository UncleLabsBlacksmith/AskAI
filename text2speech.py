import requests
import pygame
import time
import os

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
        with open('test.wav', 'wb') as a:
            a.write(resp.content)
            print('Downloaded: ')
    else:
        print(resp.reason)

generatesound('ข้าวผัดไก่')