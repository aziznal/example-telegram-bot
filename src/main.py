#!/usr/bin/env python
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import utils as utils

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Welcome to my bot, baby.')


def help(update, context):
    update.message.reply_text('Help!')


def ahmed(update, context):
    update.message.reply_text('Whazzzzzzzzzzzzzzzaaaaaaaap')

def ilyas(update, context):
    print("received /ilyas command")
    update.message.reply_text('Whazzzzzzzzzzzzzzzaaaaaaaap')


def echo(update, context):
    print(f"received {update.message.text}")
    update.message.reply_text(update.message.text)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(utils.load_bot_token(), use_context=True)

    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(CommandHandler("ahmed", ahmed))
    dp.add_handler(CommandHandler("ilyas", ilyas))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
