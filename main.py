from telegram.ext import Updater, CommandHandler

updater = Updater(token='1699409535:AAE4oMN3JwegpsEEA_r43SS-5KX2cscCzrY', use_context=True)


dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()