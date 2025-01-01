from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Replace 'YOUR_API_TOKEN' with your bot's API token
API_TOKEN = 'YOUR_API_TOKEN'

# Command handler for the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I’m your bot. How can I help you?')

# Message handler to echo back messages
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f'You said: {user_message}')

# Error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

def main():
    # Create the Application
    application = Application.builder().token(API_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Add error handler
    application.add_error_handler(error)

    # Start the bot
    print('Bot is running...')
    application.run_polling()

if __name__ == '__main__':
    main()