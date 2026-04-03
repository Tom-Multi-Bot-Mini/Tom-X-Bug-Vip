from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# আপনার ডিটেইলস এখানে বসান
API_ID = "আপনার_API_ID"
API_HASH = "আপনার_API_HASH"
BOT_TOKEN = "8759130990:AAH3YoOL1eGt5NXN9xh5klJKhRCSKwaSd4g"
OWNER_USERNAME = "@pr78rohitbug" # আপনার ইউজারনেম দিন

app = Client("bug_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# স্টার্ট মেনু (আপনার স্ক্রিনশটের মতো)
@app.on_message(filters.command("start"))
async def start(client, message):
    text = (
        "**╔══════════════╗**\n"
        "** TOM-X BUG VIP      **\n"
        "**╚══════════════╝**\n\n"
        f"➤ **Name** : {message.from_user.first_name}\n"
        f"➤ **Developer** : {OWNER_USERNAME}\n"
        "➤ **Status** : Free User\n"
        "➤ **Online** : Active ✅\n"
        "──────────────────\n"
        "**Press Button Menu**"
    )
    
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("║ Bug Menu ║", callback_data="bug_menu"),
            InlineKeyboardButton("║ Misc Menu ║", callback_data="misc_menu")
        ],
        [
            InlineKeyboardButton("║ Channel ║", url="https://t.me/your_channel"),
        ],
        [
            InlineKeyboardButton("║ Group ║", url="https://t.me/your_group")
        ]
    ])
    
    # এখানে আপনার ছবির লিঙ্ক দিন (যেমন আপনার প্রোফাইল পিকচার)
    await message.reply_photo(
        photo="https://telegra.ph/file/your-image-link.jpg", 
        caption=text,
        reply_markup=buttons
    )

# বাটন ক্লিক হ্যান্ডলার
@app.on_callback_query()
async def callback(client, query):
    if query.data == "bug_menu":
        await query.message.edit_text(
            "**⚠️ BUG MENU ⚠️**\n\n1. WhatsApp Crash\n2. Telegram Lag\n3. Vcard Virus\n\nContact Admin to Unlock VIP!",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Back", callback_data="back")]])
        )
    elif query.data == "back":
        await start(client, query.message)

print("বট সচল আছে...")
app.run()
