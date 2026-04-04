import os
import logging
import subprocess
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, MessageHandler, filters, ContextTypes

# --- সেটিংস ---
TOKEN = "8759130990:AAHxez0e5QFqJ44cYOTc3nsfbvgz0ktR3Ac" # তোর নতুন টোকেন
VIP_USERS = [7899672241]
IMAGE_URL = "https://i.postimg.cc/k4r8sG52/1775260136317.png" 

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
    keyboard = [[InlineKeyboardButton("║ Bug Menu ║", callback_data="btn_bug")], [InlineKeyboardButton("║ Support Group ║", url="https://t.me/tomxbugvip")]]
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
        await update.message.reply_text(f"⏳ **Requesting Pairing Code for {num}...**\nCheck Inbox in 10 seconds!")
        # নোড ফাইল রান করা
        subprocess.Popen(["node", "pair.js", num])

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_commands))
    print("Bot is running...")
    await app.initialize()
    await app.start_polling()
    # এখানে কোনো লুপ লাগবে না, রেলওয়ে এটা হ্যান্ডেল করবে
    import asyncio
    while True: await asyncio.sleep(1)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
