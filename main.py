from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from conf import api_key
from models.base import session_factory
from models.place_model import Place
from models.user_model import User


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Hello, " + update.message.from_user.username)
    session = session_factory()
    username = update.message.from_user.username
    new_user = User(username)
    session.add(new_user)
    session.commit()
    session.close()
    bot.send_message(chat_id=update.message.chat_id,
                     text=update.message.from_user.username + " added")


def add_place(bot, update, args):
    placename = args[0]
    username = update.effective_user
    update.message.reply_text('You was at ' + placename)
    session = session_factory()
    current_user = session.query.filter(User.username == username)
    new_place = Place(placename, current_user)
    session.add(new_place)
    session.commit()
    session.close()
    update.message.reply_text('Place submitted')


updater = Updater(token=api_key)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

add_place_handler = CommandHandler('add_place', add_place, pass_args=True)
dispatcher.add_handler(add_place_handler)

updater.start_polling()
