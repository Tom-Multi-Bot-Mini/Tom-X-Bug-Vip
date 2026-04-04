import os
import logging
import subprocess
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, MessageHandler, filters, ContextTypes

# --- Settings ---
TOKEN = "8759130990:AAHxez0e5QFqJ44cYOTc3nsfbvgz0ktR3Ac"
VIP_USERS = [7899672241] 
IMAGE_URL = "https://i.postimg.cc/k4r8sG52/1775260136317.png" 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- 1. Start Menu (Updated YouTube Link) ---
def get_main_menu(user_id):
    is_vip = user_id in VIP_USERS
    status = "VIP Member ✅" if is_vip else "Free User ❌"
    
    text = (
        "┌────┤ **𝐓𝐎𝐌-𝐗 𝐁𝐔𝐆 𝐕𝐈𝐏** ├────┐\n"
        f"│➤ Name : `{user_id}`\n"
        f"│➤ Developer : @TomPrimeX\n"
        f"│➤ Status : {status}\n"
        f"│➤ Online : Active ✅\n"
        "└───────────────────────┘\n\n"
        "**Nicher button gulo diye menu navigate kor**"
    )
    
    keyboard = [
        [
            InlineKeyboardButton("║ Bug Menu ║", callback_data="btn_bug"),
            InlineKeyboardButton("║ Misc Menu ║", callback_data="btn_misc")
        ],
        [InlineKeyboardButton("║ SMM MENU ║", callback_data="btn_smm")],
        [
            InlineKeyboardButton("📺 YouTube", url="https://youtube.com/@saycotom?si=fQ4zbQbrcoW5JQwi"),
            InlineKeyboardButton("📢 Channel", url="https://t.me/tomprime_x")
        ],
        [InlineKeyboardButton("👥 Support Group", url="https://t.me/tomxbugvip")]
    ]
    return text, InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text, reply_markup = get_main_menu(update.effective_user.id)
    await update.message.reply_photo(photo=IMAGE_URL, caption=text, reply_markup=reply_markup, parse_mode='Markdown')

# --- 2. Button Click Handler ---
async def handle_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "btn_bug":
        bug_text = (
            "┏━━━━━━ **𝐁𝐔𝐆 𝐌𝐄𝐍𝐔** ━━━━━━\n"
            "┣━━━━ **𝐏𝐎𝐊 𝐏𝐎𝐊 𝐀𝐍𝐃𝐑𝐎𝐈𝐃** ━━━━\n"
            "┃ ➤ tomcsdroid\n┃ ➤ tomjam\n┃ ➤ tomcut\n┃ ➤ tomsys\n┃ ➤ tomcrash\n┃ ➤ tomkill\n┃ ➤ forceblock\n"
            "┣━━━━━━ **𝐏𝐎𝐊 𝐏𝐎𝐊 𝐈𝐎𝐒** ━━━━━━\n"
            "┃ ➤ tomcs\n┃ ➤ tomhiden\n┃ ➤ tomoff\n┃ ➤ tomhang\n"
            "┣━━━━━━ **𝐏𝐎𝐊 𝐏𝐎𝐊 𝐆𝐑𝐎𝐔𝐏** ━━━━━━\n"
            "┃ ➤ listgc | grpid | tomsysgp\n┃ ➤ hangui | pokmix\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        )
        await query.edit_message_caption(caption=bug_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="home")]]), parse_mode='Markdown')

    elif query.data == "btn_misc":
        misc_text = (
            "┏━━━━━━ **𝐌𝐈𝐒𝐂 𝐌𝐄𝐍𝐔** ━━━━━━\n"
            "┃ ➤ conect number\n┃ ➤ delconect number\n┃ ➤ addlove ID\n┃ ➤ adtoken token\n┃ ➤ reactmax link emoji\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        )
        await query.edit_message_caption(caption=misc_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="home")]]), parse_mode='Markdown')

    elif query.data == "btn_smm":
        smm_text = "┏━━━━━━ **𝐒𝐌𝐌 𝐌𝐄𝐍𝐔** ━━━━━━\n┃ ➤ reactpost link\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        await query.edit_message_caption(caption=smm_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="home")]]), parse_mode='Markdown')

    elif query.data == "home":
        t, r = get_main_menu(query.from_user.id)
        await query.edit_message_caption(caption=t, reply_markup=r, parse_mode='Markdown')

# --- 3. Command Handler ---
async def handle_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in VIP_USERS:
        return await update.message.reply_text("❌ Tor kache membership nei!")

    text = update.message.text.lower()
    args = text.split()
    if not args: return
    cmd = args[0]

    if len(args) >= 2:
        target = args[1]
        await update.message.reply_text(f"🚀 **Executing:** `{cmd}`\n🎯 **Target:** `{target}`")
        subprocess.Popen(["node", "pair.js" if "conect" in cmd else "spam.js", target])

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_click))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_commands))
    
    print("Bot is Live with Updated YouTube Link!")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
