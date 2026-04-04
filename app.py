import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# --- 1. SETTINGS ---
TOKEN = "8759130990:AAH3YoOL1eGt5NXN9xh5klJKhRCSKwaSd4g"
VIP_USERS = [7899672241]
IMAGE_URL = "https://i.postimg.cc/k4r8sG52/1775260136317.png" 

# নিজের চ্যানেলের ইউজারনেম এখানে দিন (@ সহ)
CHANNEL_ID = "https://t.me/tomxbugvip" 
GROUP_LINK = "https://t.me/tomxbugvip"
YOUTUBE_LINK = "https://youtube.com/@saycotom?si=nlptFT57FmTMfDrY"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- 2. HELPERS ---
async def is_subscribed(context, user_id):
    try:
        c_member = await context.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        return c_member.status not in ['left', 'kicked']
    except: return True

# --- 3. UI BUILDERS ---
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
        [InlineKeyboardButton("║ Channel ║", url=f"https://t.me/{CHANNEL_ID[1:]}"),
         InlineKeyboardButton("║ Support Group ║", url=GROUP_LINK)]
    ]
    return text, InlineKeyboardMarkup(keyboard)

# --- 4. COMMAND HANDLERS ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    if not await is_subscribed(context, user_id):
        sub_text = (
            "❌ **You must subscribe my telegram channel to use this bot.**\n"
            "After doing so, click \"Check Membership\" or use /checkmembership."
        )
        # Fixed syntax error: added url=
        sub_kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{CHANNEL_ID[1:]}")],
            [InlineKeyboardButton("👥 Join Group", url=GROUP_LINK)],
            [InlineKeyboardButton("🎥 Subscribe YouTube", url=YOUTUBE_LINK)],
            [InlineKeyboardButton("✅ Check Membership", callback_data="verify_sub")]
        ])
        return await update.message.reply_text(sub_text, reply_markup=sub_kb, parse_mode='Markdown')
    
    text, reply_markup = get_main_menu(user_id)
    try: await update.message.reply_photo(photo=IMAGE_URL, caption=text, reply_markup=reply_markup, parse_mode='Markdown')
    except: await update.message.reply_text(text, reply_markup=reply_markup, parse_mode='Markdown')

async def conect_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in VIP_USERS:
        # Access Denied layout
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

# --- 5. CALLBACK HANDLERS ---
async def handle_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    if query.data == "btn_bug":
        bug_text = (
            "┏━━━━━━ **TOM-X BUG MENU** ━━━━━━\n"
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
            "┌────┤ **SMM MENU** ├────────┐\n"
            "│➤ reactpost **link emoji**\n"
            "└───────────────────────┘"
        )
        await query.edit_message_caption(caption=smm_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="home")]]), parse_mode='Markdown')

    elif query.data == "home":
        text, reply_markup = get_main_menu(user_id)
        try: await query.edit_message_caption(caption=text, reply_markup=reply_markup, parse_mode='Markdown')
        except: 
            await query.message.delete()
            await context.bot.send_photo(chat_id=user_id, photo=IMAGE_URL, caption=text, reply_markup=reply_markup, parse_mode='Markdown')

    elif query.data == "verify_sub":
        if await is_subscribed(context, user_id):
            # Success message from your screenshot
            success_text = "✅ Membership verified! You are now a member of both the channel and group. Try your command again (e.g., /start or /conect)."
            await query.message.reply_text(success_text, parse_mode='Markdown')
            await query.message.delete()
            # Then show main menu
            text, reply_markup = get_main_menu(user_id)
            await context.bot.send_photo(chat_id=user_id, photo=IMAGE_URL, caption=text, reply_markup=reply_markup, parse_mode='Markdown')
        else:
            await query.answer("⚠️ Please join our channel/group first!", show_alert=True)

# --- 6. MAIN ---
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("conect", conect_cmd))
    app.add_handler(CallbackQueryHandler(handle_click))
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
