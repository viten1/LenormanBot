import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import random

    # Задаем уровень логов
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)

    # Задаем токен и создаем экземпляр бота
TOKEN = '5478416461:AAHaNYaKZzLmBjuVG9Y-mbd78H7eAzJa064'
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

    # Функция для обработки команды /start
def start(update, context):
    # Создаем клавиатуру для меню
    keyboard = [[InlineKeyboardButton("Прогноз на день", callback_data='predict')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с приветствием и клавиатурой
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Привет! Я бот для гадания на картах Ленорман. Что бы вы хотели сделать?",
                             reply_markup=reply_markup)

    # Функция для обработки колбэка от кнопки "Прогноз на день"
def predict_callback(update, context):
    # Создаем клавиатуру для меню
    keyboard = [[InlineKeyboardButton("Назад", callback_data='back')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

def get_random_card_and_position():
    # Случайно выбираем карту из списка
    card = random.choice(cards)
    
    # Получаем номер позиции карты в раскладе Ленорман
    position = cards.index(card) + 1
    
    return card, positions[position]
    # Получаем случайную карту и информацию о ее позиции в раскладе
    card, position = get_random_card_and_position()

    # Отправляем сообщение с информацией о карте и ее позиции, а также кнопкой "Назад"
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open(f'images/{card}.jpg', 'rb'),
                           caption=f"Позиция карты в раскладе: {position}\n\n{get_card_meaning(card)}",
                           reply_markup=reply_markup)

    # Функция для обработки колбэка от кнопки "Назад"
def back_callback(update, context):
    # Создаем клавиатуру для меню
    keyboard = [[InlineKeyboardButton("Прогноз на день", callback_data='predict')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с клавиатурой
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Что бы вы хотели сделать?",
                             reply_markup=reply_markup)

    # Регистрируем обработчик команды /start
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

import random

    # Список карт Ленорман
cards = ['01_rytsar', '02_vyzvanie', '03_soroka', '04_chayka', '05_dom', '06_buket', '07_kvartira', '08_luk', '09_ryumka', '10_mech', '11_krest', '12_koltso', '13_rebenok', '14_korabl', '15_rytsar', '16_doroga', '17_pisma', '18_dengi', '19_zvony', '20_serdce', '21_dar', '22_puteshestvie', '23_myslitel', '24_golova', '25_dama', '26_yabloko', '27_ploshchadka', '28_bereza', '29_krysy', '30_sleza', '31_solntse', '32_luk', '33_kniga', '34_lisa', '35_lotos', '36_slepye']

    # Словарь с позициями карт в раскладе Ленорман
positions = {
    1: "Рыцарь",
    2: "Вызов",
    3: "Сорока",
    4: "Чайка",
    5: "Дом",
    6: "Букет",
    7: "Квартира",
    8: "Лук",
    9: "Рюмка",
    10: "Меч",
    11: "Крест",
    12: "Кольцо",
    13: "Ребенок",
    14: "Корабль",
    15: "Козырь",
    16: "Дорога",
    17: "Письма",
    18: "Деньги",
    19: "Звоны",
    20: "Сердце",
    21: "Дар",
    22: "Путешествие",
    23: "Мыслитель",
    24: "Голова",
    25: "Деньги",
    26: "Книга",
    27: "Путешествие",
    28: "Город",
    29: "Лиса",
    30: "Лотос",
    31: "Солнце",
    32: "Луна",
    33: "Ключ",
    34: "Рюмка",
    35: "Корона",
    36: "Крысы"
}

  # Словарь с значениями карт в данном раскладе Ленорман
card_meanings = {
    '01_rytsar': 'Предстоит встреча с человеком, который защитит вас от неприятностей.',
    '02_vyzvanie': 'Предстоит встреча с человеком, который сделает вам предложение или даст задание.',
    '03_soroka': 'Предстоит встреча с человеком, который будет препятствовать вашим планам.',
    '04_chayka': 'Предстоит поездка или переезд в ближайшем будущем.',
    '05_dom': 'Семейные дела будут занимать главное место в ближайшее время.',
    '06_buket': 'Получите приятный подарок или сюрприз.',
    '07_kvartira': 'Получите важную информацию, которая связана с жильем.',
    '08_luk': 'Будьте готовы к встрече с трудностями и испытаниями.',
    '09_ryumka': 'В ближайшее время предстоит встреча с друзьями.',
    '10_mech': 'Предстоит борьба за свои права.',
    '11_krest': 'Предстоит важное событие, которое повлияет на вашу жизнь.',
    '12_koltso': 'Предстоит встреча с человеком, который будет иметь влияние на вашу жизнь.',
    '13_rebenok': 'Новое начало, положительные изменения.',
    '14_korabl': 'Предстоит долгое путешествие или переезд.',
    '15_rytsar': 'Будьте готовы к тому, что придется защищать свои интересы.',
    '16_doroga': 'Предстоит выбор между двумя возможностями.',
    '17_pisma': 'Получите важное сообщение или информацию.',
    '18_dengi': 'Появятся новые финансовые возможности.',
    '19_zvony': 'Получите новости, которые могут изменить вашу жизнь.',
    '20_serdce': 'Будет любовь и гармония в личной жизни.',
    '21_dar': 'Получите ценный подарок или вознаграждение за свои заслуги.',
    '22_puteshestvie': 'Предстоит путешествие или изменение обстановки.',
    '23_myslitel': 'Предстоит важное решение или размышление над проблемой.',
    '24_golova': 'Предстоит решение сложной проблемы.',
    '24_golova': 'Предстоит решение сложной проблемы.',
    '25_dengi': 'Появятся новые финансовые возможности.',
    '26_kniga': 'Предстоит получение новых знаний или информации.',
    '27_puteshestvie': 'Предстоит путешествие или изменение обстановки.',
    '28_gorod': 'Предстоит переезд в город или другую местность.',
    '29_lisa': 'Будьте осторожны, кто-то может попытаться обмануть вас.',
    '30_lotos': 'Получите приятный и долгожданный результат своих усилий.',
    '31_solntse': 'Будет процветание и успех в личной и профессиональной жизни.',
    '32_luna': 'Будет творческий подъем и успех в делах, связанных с искусством.',
    '33_klyuch': 'Появится решение проблемы или разгадка загадки.',
    '34_ryumka': 'В ближайшее время предстоит встреча с друзьями.',
    '35_korona': 'Предстоит важное достижение или победа.',
    '36_krysy': 'Будьте осторожны, кто-то может пытаться вас подвести.'
}

#Словарь с позициями карт в раскладе Ленорман
card_positions = {
1: '01_rytsar', 2: '02_vyzvanie', 3: '03_soroka', 4: '04_chayka', 5: '05_dom', 6: '06_buket',
7: '07_kvartira', 8: '08_luk', 9: '09_ryumka', 10: '10_mech', 11: '11_krest', 12: '12_koltso',
13: '13_rebenok', 14: '14_korabl', 15: '15_rytsar', 16: '16_doroga', 17: '17_pisma',
18: '18_dengi', 19: '19_zvony', 20: '20_serdce', 21: '21_dar', 22: '22_puteshestvie',
23: '23_myslitel', 24: '24_golova', 25: '25_dengi', 26: '26_kniga', 27: '27_puteshestvie',
28: '28_gorod', 29: '29_lisa', 30: '30_lotos', 31: '31_solntse', 32: '32_luna', 33: '33_klyuch',
34: '34_ryumka', 35: '35_korona', 36: '36_krysy'
}

# Функция для генерации расклада Ленорман
def lenormand_spread():
    return random.sample(list(card_positions.keys()), k=3)

# Функция для обработки команды /start
def start(update, context):
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    keyboard = [
        [InlineKeyboardButton("Гадать на сегодня", callback_data='spread')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите действие:', reply_markup=reply_markup)


#Функция для обработки команды /start
def start(update, context):
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    keyboard = [[InlineKeyboardButton("Гадать на сегодня", callback_data='spread')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите действие:', reply_markup=reply_markup)

# Регистрация функции обратного вызова в диспетчере
dispatcher.add_handler(CommandHandler("start", start))

#Функция для обработки выбора кнопки "Гадать на сегодня"
def spread_choice(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Ваш прогноз на сегодня:")
spread = lenormand_spread()

# Обработка карт из расклада Ленорман
for position in spread:
    card = card_positions[position]
    meaning = card_meanings[card]
    img_path = f'cards/{card}.jpg'
    with open(img_path, 'rb') as f:
        context.bot.send_photo(chat_id=query.message.chat_id, photo=f)
    context.bot.send_message(chat_id=query.message.chat_id, text=meaning)
  
 # Расшифровка общего результата
def get_total_value(cards):
    total = 0
    for card in cards:
        value = CARD_VALUES.get(card)
        if value:
            total += value
    return total

def forecast(update, context):
    # Выбираем случайные карты
    chosen_cards = random.sample(CARD_NAMES.keys(), 3)

    # Отправляем пользователю вопросы и карты
    for i, card in enumerate(chosen_cards):
        question = QUESTIONS[i]
        image_url = CARD_IMAGES[card]
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url, caption=question)


    # Вычисляем общий результат
    total_value = get_total_value(chosen_cards)

    # Отправляем общий результат
    if total_value <= 23:
        message = "Общий результат: Вы на верном пути. Ваше будущее обещает быть ярким и успешным."
    elif total_value <= 29:
        message = "Общий результат: Вам необходимо остерегаться неожиданностей и опасностей, которые могут возникнуть на вашем пути."
    else:
        message = "Общий результат: Вам следует проявлять больше осторожности и внимательности, чтобы избежать серьезых проблем в будущем."

context.bot.send_message(chat_id=update.effective_chat.id, text=message)

#Создаем обработчики для команды /start и /forecast
start_handler = CommandHandler('start', start)
forecast_handler = CommandHandler('forecast', forecast)

#Создаем меню в виде кнопок
menu = [['/forecast']]
menu_markup = ReplyKeyboardMarkup(menu, one_time_keyboard=True)

#Регистрируем обработчики и меню
dispatcher.add_handler(start_handler)
dispatcher.add_handler(forecast_handler)
dispatcher.add_handler(MessageHandler(Filters.text, unknown))
dispatcher.add_handler(CallbackQueryHandler(button))
dispatcher.bot.set_my_commands(commands)
dispatcher.bot.set_webhook(url=WEBHOOK_URL)

#Запускаем бот
updater.start_polling()
updater.idle()
