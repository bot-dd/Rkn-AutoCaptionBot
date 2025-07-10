from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.errors import UserNotParticipant
from config import Rkn_Botz as Config
from .database import rkn_botz

# ✅ Custom async filter function
async def is_not_subscribed(_, client: Client, message: Message) -> bool:
    user_id = message.from_user.id

    # Register the user in the database
    await rkn_botz.register_user(user_id)

    if not Config.FORCE_SUB:
        return False

    try:
        member = await client.get_chat_member(Config.FORCE_SUB, user_id)

        # ✅ Only allow if not a member/admin/owner
        return member.status not in (
            enums.ChatMemberStatus.MEMBER,
            enums.ChatMemberStatus.ADMINISTRATOR,
            enums.ChatMemberStatus.OWNER,
        )
    except UserNotParticipant:
        return True
    except Exception:
        return False


# ✅ Handler for unsubscribed users
@Client.on_message(filters.private & filters.create(is_not_subscribed))
async def handle_force_sub(client: Client, message: Message):
    user_id = message.from_user.id
    channel_username = Config.FORCE_SUB.lstrip("@")
    channel_link = f"https://t.me/{channel_username}"

    try:
        member = await client.get_chat_member(Config.FORCE_SUB, user_id)
        if member.status == enums.ChatMemberStatus.BANNED:
            return await message.reply_text(
                "**🚫 You are banned from using this bot.**\n"
                "Contact admin if this is a mistake."
            )
    except UserNotParticipant:
        pass
    except Exception as e:
        return await message.reply_text(f"⚠️ Unexpected error: `{e}`")

    # 🔘 Inline Button
    button = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔔 Join Update Channel", url=channel_link)],
        [InlineKeyboardButton("✅ I've Joined", url=f"https://t.me/{client.me.username}")]
    ])

    await message.reply_text(
        "**Hey buddy! 🔐 To use this bot, you must join our updates channel.**\n"
        f"👉 Channel: @{channel_username}",
        reply_markup=button
    )
