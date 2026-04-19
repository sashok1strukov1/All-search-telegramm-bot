import  telebot
lanabot = telebot.TeleBot("Ваш токен")
@lanabot.message_handler(commands=["start"])
def start_bot(msg):
    kd = telebot.types.InlineKeyboardMarkup()
    kd.row(telebot.types.InlineKeyboardButton("yandex", url="https://ya.ru/"))
    kd.row(telebot.types.InlineKeyboardButton("google", "https://www.google.ru/"))
    kd.row(telebot.types.InlineKeyboardButton("mail ru ", url="https://mail.ru/"))
    kd.row(telebot.types.InlineKeyboardButton("rambler", url="https://www.rambler.ru/"))
    kd.row(telebot.types.InlineKeyboardButton("bing microsoft", "https://www.bing.com/")) #
    kd.row(telebot.types.InlineKeyboardButton("duckduckgo", url="https://duckduckgo.com/"))
    kd.row(telebot.types.InlineKeyboardButton("baidu", url="https://www.baidu.com/"))
    kd.row(telebot.types.InlineKeyboardButton("yahooo", "https://www.yahoo.com/"))  #
    kd.row(telebot.types.InlineKeyboardButton("startpage", url="https://www.startpage.com/"))
    kd.row(telebot.types.InlineKeyboardButton("yacy", url="https://yacy.net/"))
    kd.row(telebot.types.InlineKeyboardButton("you", "https://you.com/ "))  #
    kd.row(telebot.types.InlineKeyboardButton("ask", url="https://www.ask.com/"))
    lanabot.send_message(msg.chat.id, "select a search engine", reply_markup=kd)


lanabot.infinity_polling()
