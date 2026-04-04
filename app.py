import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# --- ১. সেটিংস ---
TOKEN = "8759130990:AAH3YoOL1eGt5NXN9xh5klJKhRCSKwaSd4g"
VIP_USERS = [7899672241]
IMAGE_URL = "https://i.postimg.cc/k4r8sG52/1775260136317.png" 

# গ্রুপ ও সোশ্যাল লিংক
GROUP_CHAT_ID = "-1003529302976" 
GROUP_LINK = "https://t.me/tomxbugvip"
YOUTUBE_LINK = "https://youtube.com/@saycotom?si=nlptFT57FmTMfDrY"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- ২. মেম্বারশিপ চেক ফাংশন ---
async def is_subscribed(context, user_id):
    try:
        member = await context.bot.get_chat_member(chat_id=GROUP_CHAT_ID, user_id=user_id)
        return member.status not in ['left', 'kicked']
    except Exception as e:
        logging.error(f"Membership check error: {e}")
        return False

# --- ৩. মেনু বিল্ডার ---
def get_main_menu(user_id):
    status = "VIP Member ✅" if user_id in VIP_USERS else "Free User ❌"
    text = (
        "┌────┤ **𝐓𝐎𝐌-𝐗 𝐁𝐔𝐆 𝐕𝐈𝐏** ├────┐\n"
        f"│➤ Name : `TOM PRIME X`\n"
        "│➤ Developer : @TomPrimeX\n"
        f"│➤ Status : {status}\n"
        "│➤ Online : Active ✅\n"
        "└───────────────────────┘\n\n"
        "**Press the buttons below to navigate**"
    )
    keyboard = [
        [InlineKeyboardButton("║ Bug Menu ║", callback_data="btn_bug"), 
         InlineKeyboardButton("║ Misc Menu ║", callback_data="btn_misc")],
        [InlineKeyboardButton("║ SMM MENU ║", callback_data="btn_smm")],
        [InlineKeyboardButton("║ Support Group ║", url=GROUP_LINK),
         InlineKeyboardButton("║ YouTube ║", url=YOUTUBE_LINK)]
    ]
    return text, InlineKeyboardMarkup(keyboard)

# --- ৪. কমান্ড হ্যান্ডলারস (New Features) ---

# WhatsApp Pairing (/reqpair)
async def reqpair(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in VIP_USERS:
        return await update.message.reply_text("🚫 **Access Denied!** Buy VIP to use Pairing feature.")
    if not context.args:
        return await update.message.reply_text("❌ **Usage:** `/reqpair +8801XXXXXXXXX`")
    
    number = context.args[0]
    pairing_msg = (
        "✅ **Pairing Code Ready!**\n\n"
        f"📱 **Nomor:** `{number}`\n"
        "🔐 **Kode:** `1MYP9AVP`\n\n"
        "Masukkan kode ini di WhatsApp Anda."
    )
    await update.message.reply_text(pairing_msg, parse_mode='Markdown')

# Bug Crash Command (/shah-andro)
async def crash_andro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in VIP_USERS:
        return await update.message.reply_text("🚫 **VIP Only!** Contact @TomPrimeX for access.")
    if not context.args:
        return await update.message.reply_text("❌ **Usage:** `/shah-andro +8801XXXXXXXXX`")
    
    target = context.args[0]
    success_msg = (
        "┌───┤ **𝐓𝐎𝐌-𝐗 𝐁𝐔𝐆 𝐒𝐘𝐒𝐓𝐄𝐌** ├───┐\n"
        "🦠 **Status:** `Success Executions`\n"
        f"👤 **Target:** `{target}`\n"
        "🎭 **Type Bug:** `Crash Android`\n"
        "📊 **Power:** `Maximum` ⚡\n"
        "└───────────────────────┘"
    )
    await update.message.reply_photo(photo=IMAGE_URL, caption=success_msg, parse_mode='Markdown')

# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not await is_subscribed(context, user_id):
        sub_kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("👥 Join Group", url=GROUP_LINK)],
            [InlineKeyboardButton("✅ Check Membership", callback_data="verify_sub")]
        ])
        return await update.message.reply_text("❌ **Join our group to use this bot!**", reply_markup=sub_kb)
    
    text, reply_markup = get_main_menu(user_id)
    await update.message.reply_photo(photo=IMAGE_URL, caption=text, reply_markup=reply_markup, parse_mode='Markdown')

# --- ৫. বাটন ক্লিক হ্যান্ডলার ---
async def handle_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    if query.data == "verify_sub":
        if await is_subscribed(context, user_id):
            await query.message.delete()
            text, reply_markup = get_main_menu(user_id)
            await context.bot.send_photo(chat_id=user_id, photo=IMAGE_URL, caption=text, reply_markup=reply_markup, parse_mode='Markdown')
        else:
            await query.answer("⚠️ Please join the group first!", show_alert=True)

    elif query.data == "btn_bug":
        bug_text = (
            "┏━━━━━━ **𝐓𝐎𝐌-𝐗 𝐁𝐔𝐆 𝐌𝐄𝐍𝐔** ━━━━━━\n"
            "┃ ➤ /reqpair **number** (New)\n"
            "┃ ➤ /shah-andro **number** (New)\n"
            "┣━━━━━━ **𝐏𝐎𝐊 𝐏𝐎𝐊 𝐀𝐍𝐃𝐑𝐎𝐈𝐃** ━━━━━━\n"
            "┃ ➤ tomcsdroid **num time**\n"
            "┃ ➤ tomjam **num time**\n"
            "┃ ➤ tomcut **num time**\n"
            "┃ ➤ tomsys **num time**\n"
            "┃ ➤ tomcrash **num time**\n"
            "┃ ➤ tomkill **num time**\n"
            "┃\n"
            "┣━━━━━━ **𝐏𝐎𝐊 𝐏𝐎𝐊 𝐆𝐑𝐎𝐔𝐏** ━━━━━━\n"
            "┃ ➤ tomsysgp **groupid time**\n"
            "┃ ➤ hangui **groupid time**\n"
            "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        )
        await query.edit_message_caption(caption=bug_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="home")]]), parse_mode='Markdown')

    elif query.data == "btn_misc":
        misc_text = "┌────┤ **Misc Menu** ├────────┐\n│➤ conect **number**\n│➤ info **username**\n└───────────────────────┘"
        await query.edit_message_caption(caption=misc_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="home")]]), parse_mode='Markdown')

    elif query.data == "btn_smm":
        smm_text = "┌────┤ **𝐒𝐌𝐌 𝐌𝐄𝐍𝐔** ├────────┐\n│➤ reactpost **link emoji**\n└───────────────────────┘"
        await query.edit_message_caption(caption=smm_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="home")]]), parse_mode='Markdown')

    elif query.data == "home":
        text, reply_markup = get_main_menu(user_id)
        await query.edit_message_caption(caption=text, reply_markup=reply_markup, parse_mode='Markdown')

# --- ৬. মেইন রানার ---
def main():
    app = Application.builder().token(TOKEN).build()
    
    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("reqpair", reqpair))
    app.add_handler(CommandHandler("shah-andro", crash_andro))
    app.add_handler(CallbackQueryHandler(handle_click))
    
    print("Tom-X Multi-Bot is Online...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
