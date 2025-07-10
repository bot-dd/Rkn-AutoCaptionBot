# AutoCaptionBot by RknDeveloper
# Copyright (c) 2024 RknDeveloper
# Licensed under the MIT License
# https://github.com/RknDeveloper/Rkn-AutoCaptionBot/blob/main/LICENSE
# Please retain this credit when using or forking this code.

# Developer Contacts:
# Telegram: @RknDeveloperr
# Updates Channel: @Rkn_Bots_Updates & @Rkn_Botz
# Special Thanks To: @ReshamOwner
# Update Channels: @Digital_Botz & @DigitalBotz_Support

# ⚠️ Please do not remove this credit!


import os
import time

class Rkn_Botz(object):
    # Rkn client config (required)
    API_ID = os.environ.get("API_ID", "26649585")
    API_HASH = os.environ.get("API_HASH", "588a3ea6fd01ae88bd2e10fed7d55b2c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # Start pic (default image link)
    RKN_PIC = os.environ.get("RKN_PIC", "https://i.imgur.com/P4yykLb.jpeg")

    # Bot uptime (start time)
    BOT_UPTIME = time.time()

    # Server port (default 8080)
    PORT = int(os.environ.get("PORT", "8080"))

    # Force subscribe channel username (without @) (only public chats username required)
    FORCE_SUB = os.environ.get("FORCE_SUB", "RMxBots")

    # Database config (required)
    DB_NAME = os.environ.get("DB_NAME", "AutoCaption_V05_Bot")
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://rohanahamed75:gt4RXJZ1mUtOh4Xv@mmtg.0ong5.mongodb.net/?retryWrites=true&w=majority&appName=mmtg")

    # Default caption (with safe fallback)
    DEFAULT_CAPTION = os.environ.get(
        "DEFAULT_CAPTION",
        "<b><a href='https://t.me/RM_Movie_Flix'>{file_name} Movie Update Channel: @RM_Movi</a></b>"
    )

    # Sticker ID default
    STICKER_ID = os.environ.get(
        "STICKER_ID",
        "CAACAgIAAxkBAAELFqBllhB70i13m-woXeIWDXU6BD2j7wAC9gcAAkb7rAR7xdjVOS5ziTQE"
    )

    # Admin ID (single integer)
    ADMIN = [int(x) for x in os.environ.get('ADMIN', '7822720438').split()]
# ————
# End of file
# Original author: @RknDeveloperr
# GitHub: https://github.com/RknDeveloper

# Developer Contacts:
# Telegram: @RknDeveloperr
# Updates Channel: @Rkn_Bots_Updates & @Rkn_Botz
# Special Thanks To: @ReshamOwner
# Update Channels: @Digital_Botz & @DigitalBotz_Support

# ⚠️ Please do not remove this credit!
