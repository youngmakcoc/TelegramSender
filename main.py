import json

import requests

def getAnek():
    response=requests.get("http://rzhunemogu.ru/RandJSON.aspx?CType=1",headers={"Content-Type":"application/json; charset=windows-1251"}).content.decode("cp1251")
    anek=json.loads(response, strict=False)["content"]
    print(anek)
    try:
        message=requests.post("https://api.telegram.org/bot5092500763:AAFP_xoeiMwFMECkZVInlJiyWB-qLYU-PcA/sendMessage",data={"chat_id":-783348924,"text": anek})
    except BaseException:
        getAnek()

getAnek()