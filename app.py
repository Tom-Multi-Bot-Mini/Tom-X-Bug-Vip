import os
import logging
import subprocess
import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- সেটিংস (তোর নতুন টোকেন) ---
TOKEN = "8759130990:AAHxez0e5QFqJ44cYOTc3nsfbvgz0ktR3Ac"
VIP_USERS = [7899672241]
IMAGE_URL = "https://i.postimg.cc/k4r8sG52/1775260136317.png" 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status = "VIP Member ✅" if update.effective_user.id in VIP_USERS else "Free User ❌"
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
    await update.message.reply_photo(photo=IMAGE_URL, caption=text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

async def handle_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in VIP_USERS: return
    text = update.message.text.lower()
    args = text.split()
    if args[0] == "/reqpair":
        if len(args) < 2: return await update.message.reply_text("❌ Usage: `/reqpair +880...`")
        num = args[1].replace("+", "")
        await update.message.reply_text(f"⏳ **Requesting Pairing Code for {num}...**\nCheck Inbox in 10-15 seconds!")
        subprocess.Popen(["node", "pair.js", num])

def main():
    # Application তৈরি
    app = Application.builder().token(TOKEN).build()
    
    # হ্যান্ডলার অ্যাড
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_commands))
    
    print("Cleaning old sessions and starting bot...")
    
    # drop_pending_updates=True দিলে পুরোনো সব Conflict এরর নিজে থেকে ঠিক হয়ে যাবে
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
