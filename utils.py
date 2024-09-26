from telegram import Update
from telegram.ext import CallbackContext
from model import recommend_movies

# Start Command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your simple Telegram bot. Send me a message and I will echo it back!')


# Define the help command handler
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('I can recommend you movies. Just type /movie and your genre and I will recommend it for you.')


# Define the echo function to reply with the same message
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

# For Unknown Command
def unknown_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"Sorry, I don't understand that command: {update.message.text}")


def movie(update: Update, context: CallbackContext) -> None:
    # Join the arguments passed after /movie to form the movie name
    movie_name = ' '.join(context.args)
    movies = recommend_movies(movie_name)

    if movie_name:  # If user provided a movie name
        # Reply with the captured movie name
        movie_list = "\n".join(movies)  # Format the list with line breaks
        reply_text = f"Movies Suggested for you:\n\n{movie_list}"
        update.message.reply_text(reply_text)
    else:
        # If no movie name is provided
        update.message.reply_text('Please provide a movie name after /movie.')


def genre(update: Update, context: CallbackContext) -> None:
    genre_name = ' '.join(context.args)

    if genre_name:
        update.message.reply_text(f'Your favorite genre is: {genre_name}')
    else:
        update.message.reply_text('Please provide a genre name after /genre.')