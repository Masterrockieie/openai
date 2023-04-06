from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Group 💫", url="https://t.me/EDIT_REPO"),
         InlineKeyboardButton(
            "Owner ✨️", url="https://t.me/Unni0240")]
    ])
    
    welcomed = f"𝐻𝐸𝑌 <b>{message.from_user.first_name}</b>\n ɪ ᴀᴍ ᴛʜᴇ ᴄʟᴏɴᴇ ᴠᴇʀsɪᴏɴ ᴏғ ᴄʜᴀᴛ ɢᴛᴘ"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
