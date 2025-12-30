import time
from datetime import datetime
from telegram import Bot

# ===== НАСТРОЙКИ =====
TOKEN = "8548789444:AAGnprk-olDe1KKn8bQ5mik4f-RTYo7rhqc"
CHAT_ID = "723644853"
# =====================

bot = Bot(token=TOKEN)

def send_signal(text):
    bot.send_message(chat_id=CHAT_ID, text=text)

last_minute = None

while True:
    now = datetime.utcnow()
    minute = now.minute

    if minute % 15 == 0 and minute != last_minute:
        send_signal("⏱ Закрылась свеча M15 по XAUUSD")
        last_minute = minute

    time.sleep(20)
