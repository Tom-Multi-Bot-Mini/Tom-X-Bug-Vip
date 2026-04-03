import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# আপনার বোট টোকেন এখানে দিন
TOKEN = "8759130990:AAH3YoOL1eGt5NXN9xh5klJKhRCSKwaSd4g"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (
        "**╔══════════════╗**\n"
        "** TOM-X BUG VIP    **\n"
        "**╚══════════════╝**\n\n"
        f"➤ **User** : {update.effective_user.first_name}\n"
        "➤ **Developer** : @pr78rohitbug\n"
        "➤ **Status** : VIP Active ✅\n"
        "──────────────────\n"
        "**Select a Menu Below**"
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

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    if query.data == "bug":
        await query.edit_message_text(
            text="**⚠️ BUG LIST ⚠️**\n\n1. WhatsApp Crash\n2. iOS Lag\n3. Android Freeze\n\n*Type /send_bug to execute!*",
            parse_mode='Markdown'
        )

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    print("বট সচল আছে...")
    application.run_polling()

if __name__ == "__main__":
    main()
