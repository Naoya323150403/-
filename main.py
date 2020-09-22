import json
import urllib.request
from flask import Flask,request,abort
from linebot import LineBotApi,WebhookHandler 
from linebot.models import MessageEvent,TextMessage,TextSendMessage
from linebot.exceptions import InvalidSignatureError

#ぐるなび
eat_url = "***************************"
eat_key = "***************************"

#LINE
LINE_USER_ID = "***************************"
YOUR_CHANNEL_SECRET = "***********************"
line_bot_api = LineBotApi("***********************")
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

list_name = []
shop_name = input()
#ぐるなび
def Get_Eat(shop_name):
    params = urllib.parse.urlencode(
        {
            'keyid': eat_key,
            'name':shop_name 
        })
    response = urllib.request.urlopen(eat_url + "?" + params)
    return response.read()

#jsonを辞書型に変換
Shop_Data = Get_Eat(shop_name)
Read_Data = json.loads(Shop_Data)["rest"]

def change_dic(Read_Data):
    for dic in Read_Data:
        list_name.append(dic.get("name"))
        
def Message():
    change_dic(Read_Data)    
    print(list_name)
    
Message()



