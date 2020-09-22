import json
import urllib.request
from flask import Flask,request,abort
from linebot import LineBotApi,WebhookHandler 
from linebot.models import MessageEvent,TextMessage,TextSendMessage
from linebot.exceptions import InvalidSignatureError

#ぐるなび
eat_url = "https://api.gnavi.co.jp/RestSearchAPI/v3/"
eat_key = "8281ecdda46d063ffea855429f6f080b"

#LINE
LINE_USER_ID = "Ua422def9c79c36afe76f39fae223771b"
YOUR_CHANNEL_SECRET = "78b0cf60301eca8828eeb852fc946b1c"
line_bot_api = LineBotApi("Hwvy0xyDokaKVJ48p5akpPK5xz0NfDgzk/LORYn1jfzs6XyNCWYZw4nvheMjpX3Y/hGGrXI7I+zqPNg0if32UPWokGfDuXxwuIpgaMY9fLA+0grpI13HIJUHLK5UDdtRaMDlPNQPxeBv/ruf8su3ggdB04t89/1O/w1cDnyilFU=")
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



