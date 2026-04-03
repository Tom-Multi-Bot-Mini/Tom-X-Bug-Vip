import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# 1. SETTINGS
TOKEN = "8759130990:AAH3YoOL1eGt5NXN9xh5klJKhRCSKwaSd4g"
VIP_USERS = [7899672241]
IMAGE_URL = "https://files.catbox.moe/v5m4y8.jpg"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def is_vip(user_id):
    return user_id in VIP_USERS

# --- ACCESS DENIED ---
async def access_denied(update: Update):
    denied_text = (
        "🚫 **𝐀𝐜𝐜𝐞𝐬𝐬 𝐃𝐞𝐧𝐢𝐞𝐝**\n\n"
        "Your Free Trial has expired. Please purchase VIP Access to continue.\n\n"
        "💰 **𝐏𝐫𝐢𝐜𝐢𝐧𝐠:**\n"
        "✅ Permanent Access: 1500 INR\n"
        "✅ Resell Rights: 2500 INR\n\n"
        "📩 **Contact @TomPrimeX for VIP Activation.**"
    )
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("📩 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫", url="https://t.me/TomPrimeX")]])
    
    if update.message:
        await update.message.reply_text(denied_text, reply_markup=keyboard, parse_mode='Markdown')
    else:
        await update.callback_query.message.reply_text(denied_text, reply_markup=keyboard, parse_mode='Markdown')

# --- MAIN MENU UI ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_status = "𝐕𝐈𝐏 𝐌𝐞𝐦𝐛𝐞𝐫 ✅" if is_vip(user_id) else "𝐅𝐫𝐞𝐞 𝐔𝐬𝐞𝐫 ❌"
    
    text = (
        "┌────┤ **𝐓𝐎𝐌-𝐗  𝐁𝐔𝐆 𝐕𝐈𝐏** ├────┐\n"
        f"│➤ **User ID** : `{user_id}`\n"
        "│➤ **Developer** : @TomPrimeX\n"
        f"│➤ **Status** : {user_status}\n"
        "│➤ **Online** : Active ✅\n"
        "└───────────────────────┘\n\n"
        "**Press the buttons below to navigate**"
    )
    
    keyboard = [
        [InlineKeyboardButton("║ 𝐁𝐮𝐠 𝐌𝐞𝐧𝐮 ║", callback_data="bug_main"), InlineKeyboardButton("║ 𝐌𝐢𝐬𝐜 𝐌𝐞𝐧𝐮 ║", callback_data="misc")],
        [InlineKeyboardButton("║ 𝐒𝐌𝐌 𝐌𝐄𝐍𝐔 ║", callback_data="smm")],
        [InlineKeyboardButton("║ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ║", url="https://t.me/your_channel"), InlineKeyboardButton("║ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 ║", url="https://t.me/your_group")]
    ]
    
    if update.message:
        await update.message.reply_photo(photo=IMAGE_URL, caption=text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')
    else:
        await update.callback_query.message.edit_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

# --- ALL BUTTON ACTIONS ---
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    # 1. BUG MENU
    if query.data == "bug_main":
        if not is_vip(user_id):
            await access_denied(update)
            return
        
        bug_text = "─── **𝐓𝐎𝐌-𝐗 𝐁𝐔𝐆 𝐈𝐍𝐓𝐄𝐑𝐅𝐀𝐂𝐄** ───\n\nSelect target device type:"
        keyboard = [
            [InlineKeyboardButton("𝐏𝐎𝐊 𝐏𝐎𝐊 𝐀𝐍𝐃𝐑𝐎𝐈𝐃", callback_data="bug_android")],
            [InlineKeyboardButton("𝐏𝐎𝐊 𝐏𝐎𝐊 𝐈𝐎𝐒", callback_data="bug_ios")],
            [InlineKeyboardButton("𝐏𝐎𝐊 𝐏𝐎𝐊 𝐆𝐑𝐎𝐔𝐏", callback_data="bug_group")],
            [InlineKeyboardButton("⬅️ 𝐁𝐚𝐜𝐤 𝐭𝐨 𝐇𝐨𝐦𝐞", callback_data="back_home")]
        ]
        await query.edit_message_caption(caption=bug_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    # 2. ANDROID BUG
    elif query.data == "bug_android":
        text = (
            "┌────┤ **𝐏𝐎𝐊 𝐏𝐎𝐊 𝐀𝐍𝐃𝐑𝐎𝐈𝐃**\n"
            "│➤ **tomcsdroid** [num] [time]\n"
            "│➤ **tomjam** [num] [time]\n"
            "│➤ **tomcut** [num] [time]\n"
            "│➤ **tomsys** [num] [time]\n"
            "│➤ **tomcrash** [num] [time]\n"
            "│➤ **tomkill** [num] [time]\n"
            "│➤ **forceblock** [num]|[amount]\n"
            "└───────────────────────┘"
        )
        await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ 𝐁𝐚𝐜𝐤", callback_data="bug_main")]]), parse_mode='Markdown')

    # 3. MISC MENU
    elif query.data == "misc":
        if not is_vip(user_id):
            await access_denied(update)
            return
        text = (
            "─── **𝐌𝐈𝐒𝐂𝐄𝐋𝐋𝐀𝐍𝐄𝐎𝐔𝐒 𝐌𝐄𝐍𝐔** ───\n"
            "➤ **connect** [number]\n"
            "➤ **disconnect** [number]\n"
            "➤ **addlove** [id]\n"
            "➤ **settoken** [token]\n"
            "──────────────────"
        )
        await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ 𝐁𝐚𝐜𝐤", callback_data="back_home")]]), parse_mode='Markdown')

    # 4. SMM MENU
    elif query.data == "smm":
        if not is_vip(user_id):
            await access_denied(update)
            return
        await query.edit_message_caption(caption="─── **𝐒𝐌𝐌 𝐏𝐀𝐍𝐄𝐋 𝐌𝐄𝐍𝐔** ───\n\n➤ **reactpost** [link]\n➤ **viewboost** [link]", 
                                         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ 𝐁𝐚𝐜𝐤", callback_data="back_home")]]), parse_mode='Markdown')

    # 5. BACK TO HOME
    elif query.data == "back_home":
        await start(update, context)

def main():
    application = Application.builder().token(TOKEN).build()
    
    # কমান্ড এবং বাটন হ্যান্ডলার যোগ করা
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    print("TOM-X Bot is LIVE - Buttons Fixed!")
    application.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
