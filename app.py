import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# --- CONFIGURATION ---
TOKEN = "8759130990:AAH3YoOL1eGt5NXN9xh5klJKhRCSKwaSd4g"
VIP_USERS = [7899672241]
# Use the Direct Link of your Golden TOM-X Logo
IMAGE_URL = "https://raw.githubusercontent.com/TomPrimeX/Tom-Bot/main/images/tomx_logo_cool.jpg" 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def is_vip(user_id):
    return user_id in VIP_USERS

# --- UI COMPONENTS ---
def get_main_menu(user_id):
    status = "VIP Member ✅" if is_vip(user_id) else "Free User ❌"
    text = (
        "┌────┤ **TOM-X  BUG VIP** ├────┐\n"
        f"│➤ User ID : `{user_id}`\n"
        "│➤ Developer : @TomPrimeX\n"
        f"│➤ Status : {status}\n"
        "│➤ Online : Active ✅\n"
        "└───────────────────────┘\n\n"
        "**Press the buttons below to navigate**"
    )
    keyboard = [
        [InlineKeyboardButton("║ Bug Menu ║", callback_data="menu_bug"), 
         InlineKeyboardButton("║ Misc Menu ║", callback_data="menu_misc")],
        [InlineKeyboardButton("║ SMM MENU ║", callback_data="menu_smm")],
        [InlineKeyboardButton("║ Channel ║", url="https://t.me/your_channel"), 
         InlineKeyboardButton("║ Support Group ║", url="https://t.me/tomxbugvip")]
    ]
    return text, InlineKeyboardMarkup(keyboard)

# --- COMMAND HANDLERS ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text, reply_markup = get_main_menu(user_id)
    try:
        await update.message.reply_photo(photo=IMAGE_URL, caption=text, reply_markup=reply_markup, parse_mode='Markdown')
    except Exception:
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode='Markdown')

# --- CALLBACK HANDLER (BUTTON LOGIC) ---
async def button_tap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    if query.data == "menu_bug":
        bug_text = (
            "┏━━━━━━ **TOM-X BUG MENU** ━━━━━━\n"
            "┃\n"
            "┣━━━ **ANDROID BUGS** ━━━\n"
            "┃ ➤ tomcsdroid **num time**\n"
            "┃ ➤ tomjam **num time**\n"
            "┃ ➤ tomcut **num time**\n"
            "┃ ➤ tomsys **num time**\n"
            "┃\n"
            "┣━━━ **IOS BUGS** ━━━\n"
            "┃ ➤ tomcs **num time**\n"
            "┃ ➤ tomhiden **num time**\n"
            "┃\n"
            "┣━━━ **GROUP BUGS** ━━━\n"
            "┃ ➤ listgc\n"
            "┃ ➤ tomsysgp **groupid time**\n"
            "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        )
        await query.edit_message_caption(caption=bug_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back to Home", callback_data="back_home")]]), parse_mode='Markdown')

    elif query.data == "menu_misc":
        misc_text = (
            "┌────┤ **Misc Menu** ├────────┐\n"
            "│➤ connect [number]\n"
            "│➤ delconnect [number]\n"
            "│➤ addlove [ID]\n"
            "│➤ adtomsell [ID]\n"
            "│➤ adtoken [token]\n"
            "│➤ info [username]\n"
            "│➤ reactmax [link] [emoji]\n"
            "└───────────────────────┘"
        )
        await query.edit_message_caption(caption=misc_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back to Home", callback_data="back_home")]]), parse_mode='Markdown')

    elif query.data == "menu_smm":
        smm_text = (
            "┌────┤ **SMM MENU** ├─────┐\n"
            "│➤ reactpost [link]\n"
            "└───────────────────────┘"
        )
        await query.edit_message_caption(caption=smm_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back to Home", callback_data="back_home")]]), parse_mode='Markdown')

    elif query.data == "back_home":
        text, reply_markup = get_main_menu(user_id)
        await query.edit_message_caption(caption=text, reply_markup=reply_markup, parse_mode='Markdown')

# --- MAIN RUNNER ---
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_tap))
    
    print("TOM-X BUG BOT IS RUNNING...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
