from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Токен бота
TOKEN = '7099708879:AAHZow-9sEIlrjRZhTJtJZaBFO0oUzR2xkQ'
# Ваш Telegram ID (можно получить, написав @userinfobot в Telegram)
YOUR_CHAT_ID = '6057462695'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот, который пересылает сообщения.')

def forward_message(update: Update, context: CallbackContext) -> None:
    # Пересылаем текстовые сообщения
    if update.message.text:
        context.bot.forward_message(chat_id=YOUR_CHAT_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Пересылаем изображения
    elif update.message.photo:
        context.bot.forward_message(chat_id=YOUR_CHAT_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

def main():
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text | Filters.photo & ~Filters.command, forward_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
