import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from currancy import get_currancy_rate
from forecast import get_forecast

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = os.getenv('BOT_TOKEN')
CURRENCY_FROM = 'RUB'
CURRENCY_TO = 'KZT'


async def on_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    forecast = get_forecast()
    currency_rate = f'Курс ₸: {get_currancy_rate(CURRENCY_FROM, CURRENCY_TO)}'
    await context.bot.send_message(chat_id=chat.id, text=forecast)
    await context.bot.send_message(chat_id=chat.id, text=currency_rate)


if __name__ == '__main__':
    application = Application.builder().token(BOT_TOKEN).build()
    start_handler = CommandHandler('start', on_start)
    application.add_handler(start_handler)
    application.run_polling()
