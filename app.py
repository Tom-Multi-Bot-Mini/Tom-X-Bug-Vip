import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes, MessageHandler, filters

# 1. SETTINGS
TOKEN = "8759130990:AAH3YoOL1eGt5NXN9xh5klJKhRCSKwaSd4g"
VIP_USERS = [7899672241]
# Catbox এর বদলে অন্য ডাইরেক্ট লিঙ্ক ব্যবহার করে দেখা হচ্ছে
IMAGE_URL = "https://raw.githubusercontent.com/TomPrimeX/Tom-Bot/main/logo.jpg" 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def is_vip(user_id):
    return user_id in VIP_USERS

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.error(f"Exception while handling an update: {context.error}")

# --- START COMMAND ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_status = "𝐕𝐈𝐏 𝐌𝐞𝐦𝐛𝐞𝐫 ✅" if is_vip(user_id) else "𝐅𝐫𝐞𝐞 𝐔𝐬𝐞𝐫 ❌"
    
    text = (
        "┌────┤ **𝐓𝐎𝐌-𝐗  𝐁𝐔𝐆 𝐕𝐈𝐏** ├────┐\n"
        f"│➤ **User ID** : `{user_id}`\n"
        "│➤ **Developer** : @TomPrimeX\n"
        f"│➤ **Status** : {user_status}\n"
        "│➤ **Online** : Active ✅\n"
        "└───────────────────────┘\n\n"
        "**Press the buttons below to navigate**"
    )
    
    keyboard = [
        [InlineKeyboardButton("║ 𝐁𝐮𝐠 𝐌𝐞𝐧𝐮 ║", callback_data="bug_main"), InlineKeyboardButton("║ 𝐌𝐢𝐬𝐜 𝐌𝐞𝐧𝐮 ║", callback_data="misc")],
        [InlineKeyboardButton("║ 𝐒𝐌𝐌 𝐌𝐄𝐍𝐔 ║", callback_data="smm")],
        [InlineKeyboardButton("║ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ║", url="https://t.me/your_channel"), InlineKeyboardButton("║ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 ║", url="https://t.me/your_group")]
    ]
    
    try:
        # প্রথমে ছবি পাঠানোর চেষ্টা করবে
        await update.message.reply_photo(photo=IMAGE_URL, caption=text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')
    except Exception as e:
        # ছবিতে এরর আসলে (যেমন 400 Bad Request) শুধু টেক্সট মেসেজ পাঠাবে
        logging.error(f"Photo error: {e}")
        await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

# --- BUTTON ACTIONS ---
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    if query.data == "back_home":
        # ব্যাক বাটনের জন্য নতুন মেসেজ না পাঠিয়ে আগের মেসেজ এডিট করার চেষ্টা
        user_status = "𝐕𝐈𝐏 𝐌𝐞𝐦𝐛𝐞𝐫 ✅" if is_vip(user_id) else "𝐅𝐫𝐞𝐞 𝐔𝐬𝐞𝐫 ❌"
        text = (
            "┌────┤ **𝐓𝐎𝐌-𝐗  𝐁𝐔𝐆 𝐕𝐈𝐏** ├────┐\n"
            f"│➤ **User ID** : `{user_id}`\n"
            "│➤ **Status** : {user_status}\n"
            "└───────────────────────┘"
        )
        keyboard = [[InlineKeyboardButton("║ 𝐁𝐮𝐠 𝐌𝐞𝐧𝐮 ║", callback_data="bug_main")]]
        try:
            await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')
        except:
            await query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_error_handler(error_handler)
    
    print("Bot is starting...")
    application.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
