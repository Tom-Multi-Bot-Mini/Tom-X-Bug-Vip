import os
import logging
import subprocess
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
# ৫ নম্বর লাইনের ভুল ইম্পোর্টটি ঠিক করা হয়েছে যাতে রেলওয়েতে ক্র্যাশ না করে
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, MessageHandler, filters, ContextTypes

# --- ১. সেটিংস ---
TOKEN = "8759130990:AAH3YoOL1eGt5NXN9xh5klJKhRCSKwaSd4g"
VIP_USERS = [7899672241]
IMAGE_URL = "https://i.postimg.cc/k4r8sG52/1775260136317.png" 
GROUP_CHAT_ID = "-1003529302976" 
GROUP_LINK = "https://t.me/tomxbugvip"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- ২. মেনু বিল্ডার ফাংশনস ---

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

# --- ৩. কমান্ড হ্যান্ডলারস ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text, reply_markup = get_main_menu(user_id)
    await update.message.reply_photo(photo=IMAGE_URL, caption=text, reply_markup=reply_markup, parse_mode='Markdown')

async def handle_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not update.message or not update.message.text: return
    
    text = update.message.text.lower()
    args = text.split()
    cmd = args[0]

    # VIP Check
    if user_id not in VIP_USERS:
        return await update.message.reply_text("🚫 **Access Denied!** Buy VIP to use this feature.")

    # সব অ্যাটাক কমান্ড লিস্ট (Android, iOS, Group সব একসাথে)
    attack_cmds = [
        'tomcsdroid', 'tomjam', 'tomcut', 'tomsys', 'tomcrash', 'tomkill', 'forceblock',
        'tomcs', 'tomhiden', 'tomoff', 'tomhang', 'tomsysgp', 'hangui', 'pokmix'
    ]
    
    # /reqpair কমান্ড হ্যান্ডেল করা
    if cmd == "/reqpair":
        if len(args) < 2: return await update.message.reply_text("❌ Usage: `/reqpair +880...`")
        subprocess.Popen(["node", "pair.js", args[1]])
        await update.message.reply_text(f"⏳ **Pairing Code Request Sent.** Check Railway Logs!")

    elif any(cmd.startswith(c) for c in attack_cmds):
        if len(args) < 2: return await update.message.reply_text(f"❌ Usage: `{cmd} number/groupid time`")
        target = args[1]
        subprocess.Popen(["node", "spam.js", target]) 
        
        success_msg = (
            "┌───┤ **𝐓𝐎𝐌-𝐗 𝐁𝐔𝐆 𝐒𝐘𝐒𝐓𝐄𝐌** ├───┐\n"
            f"🦠 **Status:** `Success Executions`\n"
            f"👤 **Target:** `{target}`\n"
            f"🎭 **Type Bug:** `{cmd.upper()}`\n"
            "📊 **Power:** `Maximum` ⚡\n"
            "└───────────────────────┘"
        )
        await update.message.reply_photo(photo=IMAGE_URL, caption=success_msg, parse_mode='Markdown')

# --- ৪. বাটন ক্লিক হ্যান্ডলার (তোর হুবহু সব মেনু এখানে আছে) ---

async def handle_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "btn_bug":
        bug_text = (
            "┏━━━━━━ **𝐓𝐎𝐌-𝐗 𝐁𝐔𝐆 𝐌𝐄𝐍𝐔** ━━━━━━\n"
            "┣━━━━ **𝐏𝐎𝐊 𝐏𝐎𝐊 𝐀𝐍𝐃𝐑𝐎𝐈𝐃** ━━━━\n"
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
            "┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        )
        await query.edit_message_caption(caption=bug_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="home")]]), parse_mode='Markdown')
    
    elif query.data == "btn_misc":
        misc_text = (
            "┌────┤ **Misc Menu** ├────────┐\n"
            "│➤ conect **number**\n"
            "│➤ delconect **number**\n"
            "│➤ addlove **ID**\n"
            "│➤ adtoken **token**\n"
            "│➤ info **username**\n"
            "│➤ reactmax **linkpost emoji**\n"
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
        t, r = get_main_menu(query.from_user.id)
        await query.edit_message_caption(caption=t, reply_markup=r, parse_mode='Markdown')

# --- ৫. মেইন রানার ---
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("reqpair", handle_commands))
    app.add_handler(CallbackQueryHandler(handle_click))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_commands))
    
    print("Tom-X Ultimate System is Live on Railway...")
    app.run_polling()

if __name__ == "__main__":
    main()
