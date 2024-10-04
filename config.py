import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6972029110:AAHV5zg_cGij6QjDyqsXwgD1crd0acy3Ej4")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "17417255"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "73d424d9847f968130cd5b41946f7a5d")
#Your DB channel ID as username with @
CHANNEL_ID = os.environ.get("CHANNEL_ID", "@BatchBotLog")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7086472788"))
#Port use 8080/80 for default 
PORT = os.environ.get("PORT", "80")
#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://nitinkumardhundhara:DARKXSIDE78@cluster0.wdive.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "unknown")
#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = os.environ.get("FORCE_SUB_CHANNEL", "@GenAnimeOfc")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
#start message
START_MSG = os.environ.get("START_MESSAGE", "ʜɪ... ɪ ᴀᴍ Mᴀᴅᴀʀᴀ Uᴄʜɪʜᴀ, ʏᴏᴜʀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ! 🚀\n\n✨ ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ! 🔗\n\n💬 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍs, ᴍᴇssᴀɢᴇ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ!")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6302971969").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Hᴇʟʟᴏ {first}...,\n\nYᴏᴜ Aʀᴇɴ’ᴛ ᴀ Pᴀʀᴛ Oꜰ Oᴜʀ Nᴇᴛᴡᴏʀᴋ. Pʟᴇᴀsᴇ Jᴏɪɴ Oᴜʀ Cʜᴀɴɴᴇʟ Tᴏ Usᴇ Mᴇ. Iꜰ Yᴏᴜ Jᴏɪɴ Oᴜʀ Cʜᴀɴɴᴇʟ, Iᴛ Wɪʟʟ Bᴇ Aᴘᴘʀᴇᴄɪᴀᴛᴇᴅ﹗</b>")
#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌ Pʟᴇᴀsᴇ Dᴏ Nᴏᴛ Sᴇɴᴅ Mᴇ Mᴇssᴀɢᴇs Dɪʀᴇᴄᴛʟʏ﹔ I Aᴍ Oɴʟʏ ᴀ Fɪʟᴇ Sʜᴀʀɪɴɢ Bᴏᴛ﹗"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "bot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
