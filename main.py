import json, telebot, requests

bot = telebot.TeleBot("5092500763:AAFP_xoeiMwFMECkZVInlJiyWB-qLYU-PcA")  # токен бота


def getAnek():
    i = 0
    while i <= 10:
        try:
            response = requests.get("http://rzhunemogu.ru/RandJSON.aspx?CType=1",
                                    headers={"Content-Type": "application/json; charset=windows-1251"}).content.decode(
                "cp1251")  # запрос анекдота
            anek = json.loads(response, strict=False)["content"]
            return anek

        except Exception:
            i += 1


@bot.message_handler(content_types=["text"])
def rjaka(message):
    if message.chat.type == "private":
        if message.text.lower() == "анекдот":
            anekdot = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            button = telebot.types.KeyboardButton("Анекдот")
            anekdot.add(button)
            try:
                bot.send_message(chat_id=message.from_user.id, text=getAnek(), reply_markup=anekdot)
            except Exception:
                getAnek()
                bot.send_message(chat_id=message.from_user.id, text=getAnek(), reply_markup=anekdot)
        else:
            bot.send_message(chat_id=message.from_user.id, text="Нажми кнопку или напиши 'анекдот'")
    elif message.chat.type == "group" or message.chat.type == "supergroup":
        if message.text.lower() == "анекдот":
            try:
                bot.reply_to(message, text=getAnek())
            except Exception:
                getAnek()
                bot.reply_to(message, text=getAnek())


bot.polling(none_stop=True, interval=0)
