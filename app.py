import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# 1. SETTINGS
TOKEN = "8759130990:AAH3YoOL1eGt5NXN9xh5klJKhRCSKwaSd4g"
VIP_USERS = [7899672241]

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def is_vip(user_id):
    return user_id in VIP_USERS

# --- UI BUILDER ---
def get_main_keyboard(user_id):
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
        [InlineKeyboardButton("║ 𝐁𝐮𝐠 𝐌𝐞𝐧𝐮 ║", callback_data="bug_main"), 
         InlineKeyboardButton("║ 𝐌𝐢𝐬𝐜 𝐌𝐞𝐧𝐮 ║", callback_data="misc")],
        [InlineKeyboardButton("║ 𝐒𝐌𝐌 𝐌𝐄𝐍𝐔 ║", callback_data="smm")],
        [InlineKeyboardButton("║ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ║", url="https://t.me/your_channel"), 
         InlineKeyboardButton("║ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 ║", url="https://t.me/your_group")]
    ]
    return text, InlineKeyboardMarkup(keyboard)

# --- START COMMAND ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text, reply_markup = get_main_keyboard(user_id)
    
    # ছবির এরর এড়াতে সরাসরি টেক্সট মেসেজ পাঠানো হচ্ছে
    await update.message.reply_text(text, reply_markup=reply_markup, parse_mode='Markdown')

# --- CALLBACK HANDLER (Fixes Bug & Misc Menu) ---
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    if query.data == "bug_main":
        text = "─── **𝐓𝐎𝐌-𝐗 𝐁𝐔𝐆 𝐈𝐍𝐓𝐄𝐑𝐅𝐀𝐂𝐄** ───\n\nSelect target device type:"
        keyboard = [
            [InlineKeyboardButton("𝐏𝐎𝐊 𝐏𝐎𝐊 𝐀𝐍𝐃𝐑𝐎𝐈𝐃", callback_data="bug_android")],
            [InlineKeyboardButton("𝐏𝐎𝐊 𝐏𝐎𝐊 𝐈𝐎𝐒", callback_data="bug_ios")],
            [InlineKeyboardButton("⬅️ 𝐁𝐚𝐜𝐤 𝐭ো 𝐇𝐨𝐦𝐞", callback_data="back_home")]
        ]
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    elif query.data == "misc":
        text = (
            "─── **𝐌𝐈𝐒𝐂𝐄𝐋𝐋𝐀𝐍𝐄𝐎𝐔𝐒 𝐌𝐄𝐍𝐔** ───\n\n"
            "➤ **connect** [number]\n"
            "➤ **disconnect** [number]\n"
            "➤ **addlove** [id]\n"
            "──────────────────"
        )
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ 𝐁𝐚𝐜𝐤", callback_data="back_home")]]), parse_mode='Markdown')

    elif query.data == "bug_android":
        text = (
            "┌────┤ **𝐏𝐎𝐊 𝐏𝐎𝐊 𝐀𝐍𝐃𝐑𝐎𝐈𝐃**\n"
            "│➤ **tomcsdroid** [num] [time]\n"
            "│➤ **tomjam** [num] [time]\n"
            "│➤ **tomcut** [num] [time]\n"
            "│➤ **tomcrash** [num] [time]\n"
            "└───────────────────────┘"
        )
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ 𝐁𝐚𝐜𝐤", callback_data="bug_main")]]), parse_mode='Markdown')

    elif query.data == "back_home":
        text, reply_markup = get_main_keyboard(user_id)
        await query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_buttons))
    
    print("TOM-X Bot is LIVE - No more image errors!")
    application.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
