## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("BAB_Nx2mZj6_St49DLS_P5xYTaoGl0y8aCoQK-BIz81c9GJs4TcBuTFlEDs0lcnF9xfe4B8ZdQU8LOqQm5webY78v42Ss5f8RGCfq2rcAb-B1_9sS6uEmm_ZccYiRUc2xRZxLHBwt6vAN3qdtiOW8Im3rd_eUaCWatKeOuwxkhEks9de_WcTKDMv5xxdQQr5rZ6WNXuZ5fWJgNWWr2xY2c18eC4l23HQYZWSjB638Sf9t2YdjK8WmSYDtsQQ3ukidGtHGKN8lFfS1qjy2EPdH624jQ9GsgD5Lg0gOU1pS4FIudv9h8GeOnrGhfxFvWtBEkupNrlxeQj2yeyVL9mUkNVkAAAAAUCtdZ8A", "")
BOT_TOKEN = getenv("5353641392:AAHrG7uci02NtS_sxbbj_NCUrhUV4yAyTPg", "")
BOT_NAME = getenv("BOT_NAME", "Tom bot")
API_ID = int(getenv("API_ID", "9157919"))
API_HASH = getenv("API_HASH", "b90c282e584222babde5f68b5b63ee3b")
OWNER_NAME = getenv("OWNER_NAME", "Tom")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Tom_01157")
ALIVE_NAME = getenv("ALIVE_NAME", "Tom")
BOT_USERNAME = getenv("BOT_USERNAME", "Tom01212bot")
OWNER_ID = getenv("OWNER_ID", "5352754419")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Ahmed1157")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "m3_us")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Tom01255")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5352754419").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/466de30ee0f9383c8e09e.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/d70bb6fa92728763c671f.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
