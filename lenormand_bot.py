
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# задаем уровень логов
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)

# функция, которая будет вызываться при команде /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я простой бот Виталька.")

# функция, которая будет вызываться при получении текстового сообщения
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# создаем экземпляр бота и регистрируем обработчики команд и сообщений
updater = Updater(token='5478416461:AAHaNYaKZzLmBjuVG9Y-mbd78H7eAzJa064', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, echo))

# запускаем бота
updater.start_polling()
updater.idle()
