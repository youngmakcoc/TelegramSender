import json, telebot, requests


bot = telebot.TeleBot("5092500763:AAFP_xoeiMwFMECkZVInlJiyWB-qLYU-PcA") #токен бота

def getAnek():
    response=requests.get("http://rzhunemogu.ru/RandJSON.aspx?CType=1",headers={"Content-Type":"application/json; charset=windows-1251"}).content.decode("cp1251") # запрос анекдота
    anek=json.loads(response, strict=False)["content"]
    print(anek)
    return anek

@bot.message_handler(content_types=["text"])
def getMessage(message):
    if message.text.lower()=="дай анекдот":
        try:
            bot.send_message(chat_id=message.from_user.id, text=getAnek())
        except:
            getAnek()
    else:
        bot.send_message(chat_id=message.from_user.id, text="Напиши 'дай анекдот'")



bot.polling(none_stop=True, interval=0)

