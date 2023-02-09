from Zaid import Zaid, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
Hᴇʏᴀ! {}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ I'ᴍ ᴀ Sɪᴍᴘʟᴇ Tᴇʟᴇɢʀᴀᴍ Mᴜꜱɪᴄ ᴀɴᴅ Mᴀɴᴀɢᴇᴍᴇɴᴛ Bᴏᴛ.
‣ I Cᴀɴ Pʟᴀʏ ꜱᴏɴɢꜱ ɪɴ ʏᴏᴜʀ ᴠᴏɪᴄᴇ.
‣ ɪ ʜᴀᴠᴇ ᴀʟᴍᴏꜱᴛ ᴀʟʟ ꜰᴇᴀᴛᴜʀᴇꜱ ᴡʜɪᴄʜ ɴᴇᴇᴅꜱ ᴀ ᴍᴜꜱɪᴄ ʙᴏᴛ
‣ ᴛʜɪꜱ ʙᴏᴛ ʙᴀꜱᴇᴅ ᴏɴ ᴛᴇʟᴇᴛʜᴏɴ. ꜱᴏ ɪᴛ'ꜱ ᴘʀᴏᴠɪᴅᴇ ᴍᴏʀᴇ ꜱᴛᴀʙɪʟɪᴛʏ ꜰʀᴏᴍ ᴏᴛʜᴇʀ ʙᴏᴛꜱ!
‣ ɪ ᴄᴀɴ ᴅᴏ ᴏᴛʜᴇʀ ᴛʜɪɴɢꜱ ʟɪᴋᴇ ᴘɪɴꜱ ᴇᴛᴄꜱ.
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ 🔘 ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ℹ️.
"""

@Zaid.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 Cʀᴇᴀᴛᴏʀ", "t.me/official_pro_xD")],
        [Button.url("🗣️ Sᴜᴘᴘᴏʀᴛ", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 Uᴘᴅᴀᴛᴇꜱ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("Hᴇʟᴘ Aɴᴅ Cᴏᴍᴍᴀɴᴅꜱ", data="help")]])
       return

    if event.is_group:
       await event.reply("**ʜᴇʏ! ɪ'ᴍ ꜱᴛɪʟʟ ᴀʟɪᴠᴇ ✅**")
       return



@Zaid.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 Cʀᴇᴀᴛᴏʀ", "t.me/official_pro_xD")],
        [Button.url("🗣️ Sᴜᴘᴘᴏʀᴛ", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 Uᴘᴅᴀᴛᴇꜱ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("Hᴇʟᴘ Aɴᴅ Cᴏᴍᴍᴀɴᴅꜱ", data="help")]])
       return
