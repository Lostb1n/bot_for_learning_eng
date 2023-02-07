import telebot
from telebot import types # для указание типов


bot = telebot.TeleBot('6167930771:AAF2LG0RM46zGmVcF8c-9xJV4IjWkcffBTY')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📖 Обучение")
    btn2 = types.KeyboardButton("❓ Задания")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет! Я бот для изучения английского языка.\nНажмите на кнопку '📖 Обучение', чтобы начать изучать английский язык.\nЕсли хотите проверить свой уровень в той или иной теме нажмите на кнопку '❓ Задания'.".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "❓ Задания"):
        bot.send_message(message.chat.id, text="Привеет, задания еще не готовы!)")
    elif(message.text == "📖 Обучение"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("📖 Грамматика")
        btn2 = types.KeyboardButton("💡 Лексика")
        back = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выберите какое направление вам бы хотелось узнать:", reply_markup=markup)
    
    elif(message.text == "📖 Грамматика"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btno1 = types.KeyboardButton("Глагол to be")
        btno2 = types.KeyboardButton("Present Continuous Tense — настоящее длительное время")
        btno3 = types.KeyboardButton("Артикли в английском языке")
        btno4 = types.KeyboardButton("🔜 Следущая страница")
        bacok = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.add(btno1, btno2, btno3, btno4, bacok)
        bot.send_message(message.chat.id, text="Теперь выберите правила которые вам бы хотелось изучить:", reply_markup=markup)
    
    elif message.text == "💡 Лексика":
        bot.send_message(message.chat.id, text="Поздороваться с читателями")

        bot.send_message(message.chat.id, text="Поздороваться с читателями")
    elif (message.text == "🔙 Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("📖 Обучение")
        button2 = types.KeyboardButton("❓ Задания")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif message.text == "Глагол to be":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="<u><b>Глагол to be</b></u>", parse_mode='HTML')
        bot.send_message(message.chat.id, text="В английском предложении всегда есть глагол. И если по-русски мы можем сказать «Я доктор», «Мэри красивая», «Мы в госпитале», то в английском языке это недопустимо: во всех этих случаях после подлежащего должен стоять глагол to be. Поэтому вы можете запомнить простое правило: если в предложении нет обычных глаголов, значит, нужен глагол to be.")
        bot.send_message(message.chat.id, text="<b>У глагола to be есть три формы:</b>", parse_mode='HTML')
        bot.send_message(message.chat.id, text="<u>•Am добавляем к местоимению I, когда мы говорим о себе:</u>", parse_mode='HTML')
        bot.send_message(message.chat.id, text="I am beautiful. — Я красивый.", parse_mode='HTML')
        bot.send_message(message.chat.id, text="<u>•Is ставим после местоимений he, she, it:</u>", parse_mode='HTML')
        bot.send_message(message.chat.id, text="She is beautiful. — Она красивая.", parse_mode='HTML')
        bot.send_message(message.chat.id, text="<u>•Are употребляем после you, we, they:</u>", parse_mode='HTML')
        bot.send_message(message.chat.id, text="You are beautiful. — Ты красивый.", parse_mode='HTML')
        photo = open('picture.jpg','rb')
        bot.send_photo(message.chat.id, photo)
        btnoo4 = types.KeyboardButton("❓ Задания")
        bacook = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.add(btnoo4, bacook)
        bot.send_message(message.chat.id, text="Тема законченна. Теперь пройдите тест по этой теме или вернитесь в меню.", reply_markup=markup)     

    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

    
    
        

bot.polling(none_stop=True)