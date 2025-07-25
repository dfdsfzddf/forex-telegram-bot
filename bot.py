
import requests
import time
import schedule
from googletrans import Translator

# توکن بات و شناسه چت (فقط برای استفاده شخصی)
BOT_TOKEN = 'توکن_ربات_تو_اینجا'
CHAT_ID = 'شناسه_چت_تو_اینجا'

# گرفتن خبر فارکس از یک منبع رایگان
def get_forex_news():
    url = "https://www.forexfactory.com/calendar.php?day=today"
    return "Forex news headlines (dummy data - replace with real source)"

# ترجمه خبر به فارسی
def translate_news(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='fa')
    return translated.text

# ارسال به تلگرام
def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

# ترکیب همه مراحل
def job():
    print("در حال دریافت اخبار فارکس...")
    news = get_forex_news()
    translated = translate_news(news)
    send_to_telegram(translated)

# تنظیم زمان اجرای روزانه
schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
