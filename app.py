import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# 1. SETTINGS
TOKEN = "8759130990:AAH3YoOL1eGt5NXN9xh5klJKhRCSKwaSd4g"
VIP_USERS = [7899672241]
IMAGE_URL = "https://raw.githubusercontent.com/TomPrimeX/Tom-Bot/main/images/tomx_logo_cool.jpg" 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def is_vip(user_id):
    return user_id in VIP_USERS

# --- UI BUILDER ---
def get_main_keyboard(user_id):
    user_status = "VIP Member ✅" if is_vip(user_id) else "Free User ❌"
    text = (
        "┌────┤ **𝐓𝐎𝐌-𝐗 𝐁𝐔𝐆 𝐕𝐈𝐏** ├────┐\n"
        f"│➤ User ID : `{user_id}`\n"
        "│➤ Developer : @TomPrimeX\n"
        f"│➤ Status : {user_status}\n"
        "│➤ Online : 2 days 6 hours 40 minutes\n"
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
        logging.error(f"Image error: {e}")
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode='Markdown')

# --- CALLBACK HANDLER ---
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    if query.data == "bug_all":
        all_bug_text = (
            "┏━━━━━━ **𝐓𝐎𝐌-𝐗 𝐁𝐔𝐆 𝐕𝐈𝐏** ━━━━━━\n"
            "┃\n"
            "┃ 👤 **Name** : `7899672241`\n"
            "┃ 👨‍💻 **Developer** : @TomPrimeX\n"
            "┃ 📊 **Status** : VIP Member ✅\n"
            "┃ 🕒 **Online** : 2 days 6 hours 40 minutes\n"
            "┃\n"
            "┣━━━ **𝐏𝐎𝐊 𝐏𝐎𝐊 𝐀𝐍𝐃𝐑𝐎𝐈𝐃** ━━━\n"
            "┃ ➤ tomcsdroid **num time**\n"
            "┃ ➤ tomjam **num time**\n"
            "┃ ➤ tomcut **num time**\n"
            "┃ ➤ tomsys **num time**\n"
            "┃ ➤ tomcrash **num time**\n"
            "┃ ➤ tomkill **num time**\n"
            "┃ ➤ forceblock **num|amount**\n"
            "┃\n"
            "┣━━━ **𝐏𝐎𝐊 𝐏𝐎𝐊 𝐈𝐎𝐒** ━━━\n"
            "┃ ➤ tomcs **num time**\n"
            "┃ ➤ tomhiden **number time**\n"
            "┃ ➤ tomoff **number time**\n"
            "┃ ➤ tomhang **number time**\n"
            "┃\n"
            "┣━━━ **𝐏𝐎𝐊 𝐏𝐎𝐊 𝐆𝐑𝐎𝐔𝐏** ━━━\n"
            "┃ ➤ listgc\n"
            "┃ ➤ grpid **link**\n"
            "┃ ➤ tomsysgp **groupid time**\n"
            "┃ ➤ pokmix **groupid time**\n"
            "┃ ➤ groupfriz **groupid time**\n"
            "┃ ➤ forcenc **groupid|amount**\n"
            "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        )
        keyboard = [[InlineKeyboardButton("⬅️ Back to Home", callback_data="back_home")]]
        await query.edit_message_caption(caption=all_bug_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    elif query.data == "misc":
        misc_text = (
            "┌────┤ **Misc Menu** ├────────┐\n"
            "│➤ connect number\n"
            "│➤ delconnect number\n"
            "│➤ addlove ID\n"
            "│➤ dellove ID\n"
            "│➤ adtomsell ID\n"
            "│➤ deltomsell ID\n"
            "│➤ adtoken token\n"
            "│➤ deltoken token\n"
            "│➤ adbaned ID\n"
            "│➤ delbaned ID\n"
            "│➤ listbaned\n"
            "│➤ listlove\n"
            "│➤ listtomsell\n"
            "│➤ listtokenn\n"
            "│➤ listuserr\n"
            "│➤ metokenn\n"
            "│➤ info username/grblink/chlink\n"
            "│➤ mc\n"
            "│➤ reactmax linkpost emoji\n"
            "│➤ setmode\n"
            "└───────────────────────┘"
        )
        keyboard = [[InlineKeyboardButton("⬅️ Back to Home", callback_data
