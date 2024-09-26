# Popcorn Picker

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from utils import movie, start, help_command, echo, unknown_command, genre


def main():
    # Replace 'YOUR_TOKEN_HERE' with your actual bot token
    updater = Updater("BOT_API_KEY", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("movie", movie))
    dp.add_handler(CommandHandler("genre", genre))

    # Register a message handler to echo all messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dp.add_handler(MessageHandler(Filters.command, unknown_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl+C
    updater.idle()

if __name__ == '__main__':
    print('Starting...')
    main()
    # print('Started...')
