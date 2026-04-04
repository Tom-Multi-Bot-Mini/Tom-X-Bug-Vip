import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# --- ১. সেটিংস ---
TOKEN = "8759130990:AAH3YoOL1eGt5NXN9xh5klJKhRCSKwaSd4g"
VIP_USERS = [7899672241]
IMAGE_URL = "https://i.postimg.cc/k4r8sG52/1775260136317.png" 

# আপনার দেওয়া গ্রুপ আইডি এবং লিংক
GROUP_CHAT_ID = "-1003529302976" 
GROUP_LINK = "https://t.me/tomxbugvip"
YOUTUBE_LINK = "https://youtube.com/@saycotom?si=nlptFT57FmTMfDrY"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- ২. মেম্বারশিপ চেক ফাংশন ---
async def is_subscribed(context, user_id):
    try:
        # বটকে অবশ্যই গ্রুপে Admin হতে হবে মেম্বার চেক করার জন্য
        member = await context.bot.get_chat_member(chat_id=GROUP_CHAT_ID, user_id=user_id)
        return member.status not in ['left', 'kicked']
    except Exception as e:
        logging.error(f"Membership check error: {e}")
        return False

# --- ৩. মেইন মেনু বিল্ডার ---
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

# --- ৪. কমান্ড হ্যান্ডলার ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # মেম্বারশিপ চেক - জয়েন না থাকলে শুধু সাবস্ক্রিপশন অপশন আসবে
    if not await is_subscribed(context, user_id):
        sub_text = (
            "❌ **You must join our group to use this bot.**\n"
            "After joining, click \"Check Membership\" below."
        )
        sub_kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("👥 Join Group", url=GROUP_LINK)],
            [InlineKeyboardButton("🎥 Subscribe YouTube", url=YOUTUBE_LINK)],
            [InlineKeyboardButton("✅ Check Membership", callback_data="verify_sub")]
        ])
        return await update.message.reply_text(sub_text, reply_markup=sub_kb, parse_mode='Markdown')
    
    # মেম্বার হলে সরাসরি ছবিসহ মেইন মেনু
    text, reply_markup = get_main_menu(user_id)
    try:
        await update.message.reply_photo(photo=IMAGE_URL, caption=text, reply_markup=reply_markup, parse_mode='Markdown')
    except:
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode='Markdown')

async def conect_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in VIP_USERS:
        denied_text = (
            "🚫 **Access Denied**\n\n"
            "The bot Free Trial is Ended, Buy VIP Access.\n\n"
            "💰 **Price:**\n"
            "✅ Access permanent: 1500INR\n"
            "✅ Resell permanent: 2500INR\n\n"
            "📩 **Contact @TomPrimeX for VIP access.**"
        )
        return await update.message.reply_text(denied_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📩 Contact Developer", url="https://t.me/TomPrimeX")]]), parse_mode='Markdown')
    await update.message.reply_text("✅ Connection started...")

# --- ৫. বাটন ক্লিক হ্যান্ডলার ---
async def handle_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    if query.data == "verify_sub":
        if await is_subscribed(context, user_id):
            # ভেরিফিকেশন সফল হলে পুরনো মেসেজ মুছে মেনু ওপেন হবে
            await query.message.delete()
            text, reply_markup = get_main_menu(user_id)
            await context.bot.send_photo(chat_id=user_id, photo=IMAGE_URL, caption=text, reply_markup=reply_markup, parse_mode='Markdown')
        else:
            await query.answer("⚠️ Please join the group first!", show_alert=True)

    elif query.data == "btn_bug":
        bug_text = (
            "┏━━━━━━ **𝐓𝐎𝐌-𝐗 𝐁𝐔𝐆 𝐌𝐄𝐍𝐔** ━━━━━━\n"
            "┣━━━━━━ **𝐏𝐎𝐊 𝐏𝐎𝐊 𝐀𝐍𝐃𝐑𝐎𝐈𝐃** ━━━━━━\n"
            "┃ ➤ tomcsdroid **num time**\n"
            "┃ ➤ tomjam **num time**\n"
            "┃ ➤ tomcut **num time**\n"
            "┃ ➤ tomsys **num time**\n"
            "┃ ➤ tomcrash **num time**\n"
            "┃ ➤ tomkill **num time**\n"
            "┃ ➤ forceblock **num|amount**\n"
            "┃\n"
            "┣━━━━━━ **𝐏𝐎𝐊 𝐏𝐎𝐊 𝐈𝐎𝐒** ━━━━━━\n"
            "┃ ➤ tomcs **num time**\n"
            "┃ ➤ tomhiden **number time**\n"
            "┃ ➤ tomoff **number time**\n"
            "┃ ➤ tomhang **number time**\n"
            "┃\n"
            "┣━━━━━━ **𝐏𝐎𝐊 𝐏𝐎𝐊 𝐆𝐑𝐎𝐔𝐏** ━━━━━━\n"
            "┃ ➤ listgc\n"
            "┃ ➤ grpid **link**\n"
            "┃ ➤ tomsysgp **groupid time**\n"
            "┃ ➤ hangui **groupid time**\n"
            "┃ ➤ pokmix **groupid time**\n"
            "┃ ➤ groupfriz **groupid time**\n"
            "┃ ➤ groupios **groupid time**\n"
            "┃ ➤ forcenc **groupid|amount**\n"
            "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        )
        await query.edit_message_caption(caption=bug_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="home")]]), parse_mode='Markdown')

    elif query.data == "btn_misc":
        misc_text = (
            "┌────┤ **Misc Menu** ├────────┐\n"
            "│➤ conect **number**\n"
            "│➤ delconect **number**\n"
            "│➤ addlove **ID**\n"
            "│➤ dellove **ID**\n"
            "│➤ adtomsell **ID**\n"
            "│➤ deltomsell **ID**\n"
            "│➤ adtoken **token**\n"
            "│➤ deltoken **token**\n"
            "│➤ adbaned **ID**\n"
            "│➤ delbaned **ID**\n"
            "│➤ listbaned\n"
            "│➤ listlove\n"
            "│➤ listtomsell\n"
            "│➤ listtokenn\n"
            "│➤ listuserr\n"
            "│➤ metokenn\n"
            "│➤ info **username/grblink/chlink**\n"
            "│➤ mc\n"
            "│➤ reactmax **linkpost emoji**\n"
            "│➤ setmode\n"
            "└───────────────────────┘"
        )
        await query.edit_message_caption(caption=misc_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="home")]]), parse_mode='Markdown')

    elif query.data == "btn_smm":
        smm_text = (
            "┌────┤ **𝐒𝐌𝐌 𝐌𝐄𝐍𝐔** ├────────┐\n"
            "│➤ reactpost **link emoji**\n"
            "└───────────────────────┘"
        )
        await query.edit_message_caption(caption=smm_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="home")]]), parse_mode='Markdown')

    elif query.data == "home":
        text, reply_markup = get_main_menu(user_id)
        await query.edit_message_caption(caption=text, reply_markup=reply_markup, parse_mode='Markdown')

# --- ৬. মেইন রানার ---
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("conect", conect_cmd))
    app.add_handler(CallbackQueryHandler(handle_click))
    
    print("Bot is running...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
