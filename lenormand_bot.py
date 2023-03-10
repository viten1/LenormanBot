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