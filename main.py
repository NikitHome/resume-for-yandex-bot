import telebot
from settings import TOKEN, CHAT_ID
from telebot import types

token = TOKEN
chat_id = CHAT_ID
bot = telebot.TeleBot(token)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
# создание кнопок
photo_last_selfie_button = types.KeyboardButton("Последнее селфи")
photo_from_high_school_button = types.KeyboardButton("Фото из старшей школы")
about_hobby_button = types.KeyboardButton("Главное увлечение")
voice_what_is_gpt_button = types.KeyboardButton("Что такое GPT?")
voice_sql_and_nosql_button = types.KeyboardButton("Разница между SQL и NoSQL")
voice_love_story_button = types.KeyboardButton("История первой любви")

# добавление кнопок
markup.add(
    photo_last_selfie_button,
    photo_from_high_school_button,
    about_hobby_button,
    voice_what_is_gpt_button,
    voice_sql_and_nosql_button,
    voice_love_story_button,
) 

# реакция на /start (первое сообщение)
@bot.message_handler(commands=['start'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Привет, меня зовут Никита, я расскажу о себе при помощи этого телеграм-бота.")
        bot.send_message(message.from_user.id, "Мне 20 лет. Я живу в Краснодаре, преподаю программирование. Раньше я полтора года работал фуллстек разработчиком. Учился я в Анапском Индустриальном Техникуме.")
        bot.send_message(message.from_user.id, "Для дальнейшего взаимодействия со мной напиши в чат /help.")

# обработка основных команд
@bot.message_handler(content_types=['text', 'voice']) 
def content(message): 
    # обработка команды - /help
    if message.text == '/help':
        bot.send_message(message.from_user.id, "Нажми на одну из кнопок, либо введи одну из следующих команд: ", reply_markup=markup)
        bot.send_message(message.from_user.id, "/start - запускает бота, отправляет первые сообщения", reply_markup=markup)
        bot.send_message(message.from_user.id, "/help - рассказывает о существующих командах", reply_markup=markup)
        bot.send_message(message.from_user.id, "/nextstep - команда для отправки сообщения настоящему Никите", reply_markup=markup)
        bot.send_message(message.from_user.id, "/getsourcecode - получить ссылку на исходный код бота", reply_markup=markup)
       
    # обработка команды - /nextstep
    elif message.text == '/nextstep':
        mesg = bot.send_message(message.from_user.id, 'Введите текст одним сообщением:')
        bot.register_next_step_handler(mesg, forward_message)
        
    # обработка команды - /getsourcecode
    elif message.text == '/getsourcecode':
        bot.send_message(message.from_user.id, "https://github.com/NikitHome/resume-bot-for-yandex", reply_markup=markup)
        
    # обработка команды (кнопки) - Последнее селфи
    elif message.text == 'Последнее селфи':
        selfie_1 = open('photo/selfie1.jpg', 'rb')
        bot.send_photo(message.from_user.id, selfie_1, reply_markup=markup)
        selfie_1.close()
        
    # обработка команды (кнопки) - Фото из старшей школы
    elif message.text == 'Фото из старшей школы':
        selfie_2 = open('photo/selfie2.jpg', 'rb')
        bot.send_photo(message.from_user.id, selfie_2, reply_markup=markup)
        selfie_2.close()
        
    # обработка команды (кнопки) - Главное увлечение
    elif message.text == 'Главное увлечение':
        bot.send_message(message.from_user.id, 'Мое главное увлечение это видеоигры. Я воспринимаю это скорее не как способ "убить время", а как нечто близкое к искусству. Это возможность побывать в таких местах, которых не существует, или места которые так далеко от меня, что не представляется возможным побывать там. Это возможность пережить чью-то историю, чьи-то чувства и эмоции. Игры дарят возможность разнообразить свою жизнь до невообразимых масштабов.', reply_markup=markup)
    
    # обработка команды (кнопки) - Что такое GPT?
    elif message.text == 'Что такое GPT?':
        voice_gpt = open('audio/gpt.mp3', 'rb')
        bot.send_voice(message.from_user.id, voice_gpt, reply_markup=markup)
        voice_gpt.close()
    
    # обработка команды (кнопки) - В чем разница между SQL и NoSQL?
    elif message.text == 'Разница между SQL и NoSQL':
        voice_sql_nosql = open('audio/sqlnosql.mp3', 'rb')
        bot.send_voice(message.from_user.id, voice_sql_nosql, reply_markup=markup)
        voice_sql_nosql.close()
    
    # обработка команды (кнопки) - История первой любви
    elif message.text == 'История первой любви':
        voice_love = open('audio/firstlove.mp3', 'rb')
        bot.send_voice(message.from_user.id, voice_love, reply_markup=markup)
        voice_love.close()
        
    elif message.voice:
        bot.send_message(message.from_user.id, 'Хотел бы я научиться говорить как человек...', reply_markup=markup)
    
    # обработка несуществующих команд
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю :(", reply_markup=markup)      
        
# переадресация сообщения после обработки команды /nextstep
def forward_message(message):
    bot.forward_message(chat_id, message.from_user.id, message.message_id)
    bot.send_message(message.from_user.id, "Сообщение отправлено Никите.", reply_markup=markup) 

# вывод ошибок в случае их возникновения
while True:
    try:
        # запуск бота
        bot.polling(none_stop=True, interval=1)
    except Exception as e:
        print(e)