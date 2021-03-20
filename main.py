import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from actions.actions import *


updater = Updater(token=os.environ['TOKEN_BOT'], use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()