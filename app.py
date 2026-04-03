import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# আপনার বোট টোকেন
TOKEN = "8759130990:AAH3YoOL1eGt5NXN9xh5klJKhRCSKwaSd4g"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "**╔══════════════╗**\n"
        "** 𝐓𝐎𝐌-𝐏𝐑𝐈𝐌𝐄-𝐁𝐔𝐆-𝐁𝐎𝐓    **\n"
        "**╚══════════════╝**\n\n"
        f"➤ **Name** : `{update.effective_user.id}`\n"
        "➤ **Developer** : @pr78rohitbug\n"
        "➤ **Status** : Free User\n"
        "➤ **Online** : 2 days 4 hours 20 minutes\n"
        "──────────────────"
    )
    keyboard = [
        [
            InlineKeyboardButton("║ Bug Menu ║", callback_data="bug_main"),
            InlineKeyboardButton("║ Misc Menu ║", callback_data="misc"),
        ],
        [InlineKeyboardButton("║ SMM MENU ║", callback_data="smm")],
        [InlineKeyboardButton("║ Support Group ║", url="https://t.me/your_group")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, reply_markup=reply_markup, parse_mode='Markdown')

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    # --- BUG MAIN MENU ---
    if query.data == "bug_main":
        bug_text = "─── **POK POK BUG MENU** ───\n\nসিলেক্ট করুন কোন ডিভাইসে বাগ পাঠাতে চান:"
        keyboard = [
            [InlineKeyboardButton("POK POK ANDROID", callback_data="bug_android")],
            [InlineKeyboardButton("POK POK IOS", callback_data="bug_ios")],
            [InlineKeyboardButton("POK POK GROUP", callback_data="bug_group")],
            [InlineKeyboardButton("⬅️ Back", callback_data="back_home")]
        ]
        await query.edit_message_text(text=bug_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    # --- ANDROID BUG LIST ---
    elif query.data == "bug_android":
        text = (
            "─── **POK POK ANDROID** ───\n"
            "➤ **rohitcsdroid** num time\n"
            "➤ **rohitjam** num time\n"
            "➤ **rohitcut** num time\n"
            "➤ **rohitsys** num time\n"
            "➤ **rohitcrash** num time\n"
            "➤ **rohitkill** num time\n"
            "➤ **forceblock** num|amount\n"
            "──────────────────"
        )
        await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="bug_main")]]), parse_mode='Markdown')

    # --- IOS BUG LIST ---
    elif query.data == "bug_ios":
        text = (
            "─── **POK POK IOS** ───\n"
            "➤ **rohitcs** num time\n"
            "➤ **rohithiden** number time\n"
            "➤ **rohitoff** number time\n"
            "➤ **rohithang** number time\n"
            "──────────────────"
        )
        await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="bug_main")]]), parse_mode='Markdown')

    # --- GROUP BUG LIST ---
    elif query.data == "bug_group":
        text = (
            "─── **POK POK GROUP** ───\n"
            "➤ **listgc**\n"
            "➤ **grpid** link\n"
            "➤ **rohitsysgp** groupid time\n"
            "➤ **hangui** groupid time\n"
            "➤ **pokmix** groupid time\n"
            "➤ **groupfriz** groupid time\n"
            "➤ **groupios** groupid time\n"
            "➤ **forcenc** groupid|amount\n"
            "──────────────────"
        )
        await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="bug_main")]]), parse_mode='Markdown')

    # --- MISC MENU ---
    elif query.data == "misc":
        text = (
            "─── **Misc Menu** ───\n"
            "➤ **conect** number\n"
            "➤ **delconect** number\n"
            "➤ **addlove** ID\n"
            "➤ **dellove** ID\n"
            "➤ **adrohitsell** ID\n"
            "➤ **delrohitsell** ID\n"
            "➤ **adtoken** token\n"
            "➤ **deltoken** token\n"
            "➤ **adbaned** ID\n"
            "➤ **delbaned** ID\n"
            "➤ **listbaned**\n"
            "➤ **listlove**\n"
            "➤ **listrohitsell**\n"
            "➤ **listtokenn**\n"
            "➤ **listuserr**\n"
            "➤ **metokenn**\n"
            "➤ **info** username/grblink/chlink\n"
            "➤ **mc**\n"
            "➤ **reactmax** linkpost emoji\n"
            "➤ **setmode**\n"
            "──────────────────"
        )
        await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="back_home")]]), parse_mode='Markdown')

    # --- SMM MENU ---
    elif query.data == "smm":
        text = (
            "─── **SMM MENU** ───\n"
            "➤ **reactpost**\n"
            "──────────────────"
        )
        await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="back_home")]]), parse_mode='Markdown')

    # --- BACK TO HOME ---
    elif query.data == "back_home":
        text = (
            "**╔══════════════╗**\n"
            "** ROHIT-X  BUG VIP    **\n"
            "**╚══════════════╝**\n\n"
            f"➤ **Name** : `{query.from_user.id}`\n"
            "➤ **Developer** : @pr78rohitbug\n"
            "➤ **Status** : Free User\n"
            "➤ **Online** : Active ✅\n"
            "──────────────────"
        )
        keyboard = [
            [InlineKeyboardButton("║ Bug Menu ║", callback_data="bug_main"), InlineKeyboardButton("║ Misc Menu ║", callback_data="misc")],
            [InlineKeyboardButton("║ SMM MENU ║", callback_data="smm")],
            [InlineKeyboardButton("║ Support Group ║", url="https://t.me/your_group")]
        ]
        await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    print("বট চলছে...")
    application.run_polling()

if __name__ == "__main__":
    main()
