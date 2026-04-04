import os
import logging
import subprocess
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, MessageHandler, filters, ContextTypes

# --- তোর সেটিংস ---
TOKEN = "8759130990:AAHxez0e5QFqJ44cYOTc3nsfbvgz0ktR3Ac"
VIP_USERS = [7899672241] 
IMAGE_URL = "https://i.postimg.cc/k4r8sG52/1775260136317.png" 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- ১. মেম্বারশিপ চেক ও মেইন মেনু ---
def get_membership_menu():
    text = (
        "❌ **You must subscribe my telegram channel to use this bot.**\n"
        "After doing so, click \"Check Membership\" or use /checkmembership."
    )
    keyboard = [
        [InlineKeyboardButton("👥 Join Group", url="https://t.me/tomprime_x")],
        [InlineKeyboardButton("🎬 Suscribe YouTube", url="https://youtube.com/@saycotom?si=fQ4zbQbrcoW5JQwi")],
        [InlineKeyboardButton("✅ Check Membership", callback_data="check_member")]
    ]
    return text, InlineKeyboardMarkup(keyboard)

def get_vip_menu(user_id):
    text = (
        "┌────┤ **𝐓𝐎𝐌-𝐗 𝐁𝐔𝐆 𝐕𝐈𝐏** ├────┐\n"
        f"│➤ Name : `TOM PRIME X`\n"
        f"│➤ Developer : @TomPrimeX\n"
        f"│➤ Status : VIP Member ✅\n"
        "└───────────────────────┘\n\n"
        "**Press the buttons below to navigate**"
    )
    keyboard = [
        [InlineKeyboardButton("║ Bug Menu ║", callback_data="btn_bug"),
         InlineKeyboardButton("║ Misc Menu ║", callback_data="btn_misc")],
        [InlineKeyboardButton("║ SMM MENU ║", callback_data="btn_smm")],
        [InlineKeyboardButton("📢 Channel", url="https://t.me/tomprime_x"),
         InlineKeyboardButton("👥 Support", url="https://t.me/tomxbugvip")]
    ]
    return text, InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text, reply_markup = get_membership_menu()
    await update.message.reply_text(text, reply_markup=reply_markup, parse_mode='Markdown')

# --- ২. বাটন হ্যান্ডলার (সব কমান্ডের ডিজাইন এখানে) ---
async def handle_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    
    if query.data == "check_member":
        if user_id in VIP_USERS:
            t, r = get_vip_menu(user_id)
            await query.message.reply_photo(photo=IMAGE_URL, caption=t, reply_markup=r, parse_mode='Markdown')
            await query.message.delete()
        else:
            await query.answer("❌ Tui member na! Age join kor.", show_alert=True)

    elif query.data == "btn_bug":
        bug_text = (
            "┏━━━━━━ **𝐁𝐔𝐆 𝐌𝐄𝐍𝐔** ━━━━━━\n"
            "┣━━━━ **𝐏𝐎𝐊 𝐏𝐎𝐊 𝐀𝐍𝐃𝐑𝐎𝐈𝐃** ━━━━\n"
            "┃ ➤ tomcsdroid | tomjam | tomcut\n┃ ➤ tomsys | tomcrash | tomkill\n┃ ➤ forceblock\n"
            "┣━━━━━━ **𝐏𝐎𝐊 𝐏𝐎𝐊 𝐈𝐎𝐒** ━━━━━━\n"
            "┃ ➤ tomcs | tomhiden | tomoff\n┃ ➤ tomhang\n"
            "┣━━━━━━ **𝐏𝐎𝐊 𝐏𝐎𝐊 𝐆𝐑𝐎𝐔𝐏** ━━━━━━\n"
            "┃ ➤ listgc | grpid | tomsysgp\n┃ ➤ hangui | pokmix | groupfriz\n┃ ➤ groupios | forcenc\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        )
        await query.edit_message_caption(caption=bug_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="go_vip")]]), parse_mode='Markdown')

    elif query.data == "btn_misc":
        misc_text = (
            "┏━━━━━━ **𝐌𝐈𝐒𝐂 𝐌𝐄𝐍𝐔** ━━━━━━\n"
            "┃ ➤ conect | delconect | addlove\n┃ ➤ dellove | adrohitsell | delrohitsell\n┃ ➤ adtoken | deltoken | adbaned\n"
            "┃ ➤ delbaned | listbaned | listlove\n┃ ➤ listrohitsell | listtokenn | listuserr\n"
            "┃ ➤ metokenn | info | mc | setmode\n┃ ➤ reactmax linkpost emoji\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        )
        await query.edit_message_caption(caption=misc_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="go_vip")]]), parse_mode='Markdown')

    elif query.data == "go_vip":
        t, r = get_vip_menu(user_id)
        await query.edit_message_caption(caption=t, reply_markup=r, parse_mode='Markdown')

# --- ৩. কমান্ড রানার ---
async def handle_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in VIP_USERS: return
    
    text = update.message.text.lower()
    args = text.split()
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
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
