from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.errors import UserNotParticipant
from config import Rkn_Botz as Config
from .database import rkn_botz


# ✅ Async callable filter class for force subscription
class ForceSubCheck:
    def __init__(self, channel: str):
        self.channel = channel.lstrip("@")

    async def __call__(self, _, client: Client, message: Message) -> bool:
        user_id = message.from_user.id

        # Register user in DB if not already
        await rkn_botz.register_user(user_id)

        if not self.channel:
            return False  # No force sub set

        try:
            member = await client.get_chat_member(self.channel, user_id)
            # ✅ Return False if user is a member
            return member.status not in (
                enums.ChatMemberStatus.MEMBER,
                enums.ChatMemberStatus.ADMINISTRATOR,
                enums.ChatMemberStatus.OWNER,
            )
        except UserNotParticipant:
            return True  # ✅ Not joined
        except Exception:
            return False  # In case of unknown error, allow access (or you can block too)


# ✅ Handler that sends join request if user not subscribed
@Client.on_message(filters.private & filters.create(ForceSubCheck(Config.FORCE_SUB)))
async def handle_force_sub(client: Client, message: Message):
    user_id = message.from_user.id
    channel_link = f"https://t.me/{Config.FORCE_SUB.lstrip('@')}"

    # Button to join update channel
    button = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔔 Join Update Channel", url=channel_link)]]
    )

    try:
        member = await client.get_chat_member(Config.FORCE_SUB, user_id)
        if member.status == enums.ChatMemberStatus.BANNED:
            return await message.reply_text(
                "**🚫 You are banned from using this bot.**\nContact admin if this is a mistake."
            )
    except UserNotParticipant:
        pass
    except Exception as e:
        return await message.reply_text(f"⚠️ Unexpected error: `{e}`")

    return await message.reply_text(
        "**Hey buddy! 🔐 Please join our updates channel before using me.**",
        reply_markup=button
    )
