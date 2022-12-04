#!/usr/bin/env python
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import telegram

import utils as utils

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Welcome to my bot, baby.')


def help(update, context):
    update.message.reply_text("""
Example Telegram Bot. made by aziznal (github.com/aziznal)

You can use the following commands:

    /start          - Displays first-time start message
    /help           - Displays this help message
    /ahmed          - Displays a custom message I made for my brother
    /ilyas          - Displays a custom message I made for a friend

The bot will echo back to any message outside of these commands
""")


def ahmed(update: telegram.update.Update, context):
    update.message.reply_text('Whazzzzzzzzzzzzzzzaaaaaaaap')


def ilyas(update: telegram.update.Update, context):
    print("received /ilyas command")
    update.message.reply_text('Whazzzzzzzzzzzzzzzaaaaaaaap')


def echo(update: telegram.update.Update, context):
    print(
        f"{update.effective_user.full_name}: {update.message.text} ({update.message.date.hour}:{update.message.date.minute})")

    update.message.reply_text(update.message.text)


def error(update: telegram.update.Update, context):
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
