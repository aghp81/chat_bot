from fastapi import FastAPI
import json
import os

app = FastAPI()

CHAT_HISTORY_FILE = "chat_history.json"

# بررسی اینکه فایل JSON وجود دارد یا نه
if not os.path.exists(CHAT_HISTORY_FILE):
    with open(CHAT_HISTORY_FILE, "w") as f:
        json.dump([], f)

# تابع برای خواندن تاریخچه مکالمات
def load_chat_history():
    with open(CHAT_HISTORY_FILE, "r") as f:
        return json.load(f)

# تابع برای ذخیره مکالمات
def save_chat_history(history):
    with open(CHAT_HISTORY_FILE, "w") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)

@app.post("/chat/")
async def chat(message: dict):
    user_message = message.get("text", "")

    # خواندن تاریخچه مکالمات
    chat_history = load_chat_history()

    # پاسخ نمونه (در مرحله بعد مدل هوش مصنوعی اضافه می‌شود)
    bot_response = f"تو گفتی: {user_message}"  

    # ذخیره مکالمه در JSON
    chat_history.append({"user": user_message, "bot": bot_response})
    save_chat_history(chat_history)

    return {"response": bot_response, "history": chat_history}
