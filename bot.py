from telegram.ext import Updater,CommandHandler

def hello(bot,update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

updater = Updater('539037531:AAHSnGe-4sU0Yn5f4OKedLJ28fzhDjtB054')

updater.dispatcher.add_handler(CommandHandler('hello',hello))

updater.start_polling()
updater.idle()