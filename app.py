import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# 1. SETTINGS
TOKEN = "8759130990:AAH3YoOL1eGt5NXN9xh5klJKhRCSKwaSd4g"
VIP_USERS = [7899672241]

# নোট: এই লিঙ্কটি সরাসরি ছবির লিঙ্ক হতে হবে (যেমন .jpg বা .png দিয়ে শেষ হওয়া)
IMAGE_URL = "https://raw.githubusercontent.com/TomPrimeX/Tom-Bot/main/images/tomx_logo_cool.jpg" 

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
        # ছবিসহ পাঠানোর চেষ্টা
        await update.message.reply_photo(photo=IMAGE_URL, caption=text, reply_markup=reply_markup, parse_mode='Markdown')
    except Exception as e:
        # ছবির লিঙ্ক ভুল হলে শুধু টেক্সট পাঠাবে যাতে এরর না আসে
        logging.error(f"Failed to send photo: {e}")
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode='Markdown')

# --- CALLBACK HANDLER ---
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    if query.data == "bug_all":
        # আপনার স্ক্রিনশটের স্টাইলে বাগ মেনু
        all_bug_text = "┏━━━━━━ **TOM-X BUG VIP** ━━━━━━\n...\n┗━━━━━━━━━━━━━━━━━━━━━━"
        try:
            await query.edit_message_caption(caption=all_bug_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="back_home")]]), parse_mode='Markdown')
        except:
            await query.edit_message_text(all_bug_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="back_home")]]), parse_mode='Markdown')

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
