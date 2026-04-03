import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# 1. SETTINGS
TOKEN = "8759130990:AAH3YoOL1eGt5NXN9xh5klJKhRCSKwaSd4g"
VIP_USERS = [7899672241]
# আপনার এডিট করা নতুন কুল গোল্ডেন লোগোর লিঙ্কটি এখানে দিন
IMAGE_URL = "https://i.postimg.cc/k4r8sG52/1775260136317.png" 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def is_vip(user_id):
    return user_id in VIP_USERS

# --- UI BUILDER ---
def get_main_keyboard(user_id):
    user_status = "VIP Member ✅" if is_vip(user_id) else "Free User ❌"
    text = (
        "┌────┤ **TOM-X BUG VIP** ├────┐\n"
        f"│➤ User ID : `{user_id}`\n"
        "│➤ Developer : @TomPrimeX\n"
        f"│➤ Status : {user_status}\n"
        "│➤ Online : Active ✅\n"
        "└───────────────────────┘\n\n"
        "**Press the buttons below to navigate**"
    )
    keyboard = [
        [InlineKeyboardButton("║ Bug Menu ║", callback_data="bug_all"), 
         InlineKeyboardButton("║ Misc Menu ║", callback_data="misc")],
        [InlineKeyboardButton("║ SMM MENU ║", callback_data="smm")],
        [InlineKeyboardButton("║ Channel ║", url="https://t.me/your_channel"), 
         InlineKeyboardButton("║ Support Group ║", url="https://t.me/your_group")]
    ]
    return text, InlineKeyboardMarkup(keyboard)

# --- START COMMAND ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text, reply_markup = get_main_keyboard(user_id)
    try:
        await update.message.reply_photo(photo=IMAGE_URL, caption=text, reply_markup=reply_markup, parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode='Markdown')

# --- CALLBACK HANDLER ---
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    # ১. BUG ALL MENU - এখানে আপনার সব কমান্ড ঠিক করে দেওয়া হয়েছে
    if query.data == "bug_all":
        all_bug_text = (
            "┏━━━━━━ **TOM-X BUG VIP** ━━━━━━\n"
            "┃\n"
            "┃ 👤 **Name** : `7899672241`\n"
            "┃ 👨‍💻 **Developer** : @TomPrimeX\n"
            "┃ 📊 **Status** : VIP Member ✅\n"
            "┃\n"
            "┣━━━ **POK POK ANDROID** ━━━\n"
            "┃ ➤ tomcsdroid **num time**\n"
            "┃ ➤ tomjam **num time**\n"
            "┃ ➤ tomcut **num time**\n"
            "┃ ➤ tomsys **num time**\n"
            "┃ ➤ tomcrash **num time**\n"
            "┃ ➤ tomkill **num time**\n"
            "┃\n"
            "┣━━━ **POK POK IOS** ━━━\n"
            "┃ ➤ tomcs **num time**\n"
            "┃ ➤ tomhiden **number time**\n"
            "┃ ➤ tomoff **number time**\n"
            "┃\n"
            "┣━━━ **POK POK GROUP** ━━━\n"
            "┃ ➤ listgc\n"
            "┃ ➤ grpid **link**\n"
            "┃ ➤ tomsysgp **groupid time**\n"
            "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        )
        keyboard = [[InlineKeyboardButton("⬅️ Back", callback_data="back_home")]]
        try:
            await query.edit_message_caption(caption=all_bug_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')
        except:
            await query.edit_message_text(all_bug_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    elif query.data == "back_home":
        text, reply_markup = get_main_keyboard(user_id)
        try:
            await query.edit_message_caption(caption=text, reply_markup=reply_markup, parse_mode='Markdown')
        except:
            await query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_buttons))
    application.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
