import telebot
import time
import random

bot = telebot.TeleBot("5121706531:AAEEodFZxJ1in24tyY0QuDPyS9aw62VagTc")

greetings = ["И тебе привет!", "енетьуеуеуеобемубиосас", "ку"]
audios = ["C:/Users/Egork/Desktop/DJ_KASEL_oj_to_est_DJ_arbuz_-_BRUH_(Dydki.info).mp3",
         "C:/Users/Egork/Desktop/MC Dimanche - Шашлычок и лучок (gta) (mp3-2020.com).mp3"]
feelings = ["хорошо","норм",]

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "тест бот запущен!")
   
@bot.message_handler(content_types=['text'])
def text_messages(message):
    message_text = message.text.lower()
    if message_text.find("привет") >= 0 or message_text.find("здравствуй") >=0:
        bot.send_message(message.chat.id, random.choice(greetings))
    elif message_text.find ("как дела") >=0 :
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAED-Z5iEkhwTkjqQJzI9U1VNRfG9lCJ7AACCAQAAuB5UgfdRO4kEJeoxiME")     
    elif message_text.find ("картинк") >=0 :
        bot.send_photo(message.chat.id, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcShWZ0S3x_7Ojxs11uIrNmND401CoNnFWVOuOo6g2m9t-73t30RICHkdfXXcWyQFDK7I_w&usqp=CAU")
    elif message_text.find ("музык") >=0 :
        audio = open(random.choice(audios), 'rb')
        bot.send_audio(message.chat.id, audio)
        audoi.close()
    else:
        bot.send_message(message.chat.id, "я тебя не понимаю:(")
        
while True:
    try:
        bot.polling(none_stop=True, interval=0)    
    except:
        time.sleep(5)
