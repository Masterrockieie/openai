import openai
import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Set up OpenAI API client
openai.api_key = "YOUR_API_KEY"

# Set up Telegram bot
bot = telegram.Bot(token="YOUR_BOT_TOKEN")
updater = Updater(token="YOUR_BOT_TOKEN", use_context=True)

# Define message handler
def handle_message(update, context):
    message = update.message.text

    # Use OpenAI API to generate response
    response = openai.Completion.create(
        engine="davinci", prompt=message, max_tokens=100
    )
    generated_text = response.choices[0].text.strip()

    # Send response back to user
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=generated_text)

# Add message handler to bot
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Start polling for messages
updater.start_polling()
updater.idle()
