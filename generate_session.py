from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("--- Telethon Session String Generator ---")

# សួរអ្នកប្រើឱ្យបញ្ចូលព័ត៌មាន
api_id_str = input("Please enter your API ID: ")
api_hash = input("Please enter your API HASH: ")

try:
    api_id = int(api_id_str)
except ValueError:
    print("Error: API ID must be a number.")
    exit()

# ចាប់ផ្តើម Client និងបង្កើត Session String
with TelegramClient(StringSession(), api_id, api_hash) as client:
    session_string = client.session.save()
    print("\n✅ SUCCESS! Your session string is ready.")
    print("Copy the entire block of text below (it's one very long line):\n")
    print("="*50)
    print(session_string)
    print("="*50)
    print("\nKeep this string SAFE and SECRET. Add it to the SESSION_STRING environment variable on Render.com.")