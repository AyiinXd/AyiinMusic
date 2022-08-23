from inspect import getfullargspec

from pyrogram import Client, filters
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InlineQueryResultArticle,
                            InlineQueryResultPhoto, InputTextMessageContent,
                            Message)

from Ayiin import (ASS_CLI_1, ASS_CLI_2, ASS_CLI_3, ASS_CLI_4, ASS_CLI_5,
                   ASSISTANT_PREFIX, BOT_ID, BOT_USERNAME, LOG_GROUP_ID,
                   MUSIC_BOT_NAME, SUDOERS, app)
from Ayiin.Database import (approve_pmpermit, disapprove_pmpermit, is_on_off,
                            is_pmpermit_approved)

flood = {}


@Client.on_message(
    filters.command("block", prefixes=ASSISTANT_PREFIX)
    & filters.user(SUDOERS)
    & ~filters.user("me")
    & ~filters.me
    & ~filters.via_bot
)
async def block_user_func(client, message):
    if not message.reply_to_message:
        return await eor(message, text="Reply to a user's message to block.")
    user_id = message.reply_to_message.from_user.id
    await eor(message, text="Successfully blocked the user")
    await client.block_user(user_id)


@Client.on_message(
    filters.command("unblock", prefixes=ASSISTANT_PREFIX)
    & filters.user(SUDOERS)
    & ~filters.user("me")
    & ~filters.me
    & ~filters.via_bot
)
async def unblock_user_func(client, message):
    if not message.reply_to_message:
        return await eor(
            message, text="Reply to a user's message to unblock."
        )
    user_id = message.reply_to_message.from_user.id
    await client.unblock_user(user_id)
    await eor(message, text="Successfully Unblocked the user")


@Client.on_message(
    filters.command("pfp", prefixes=ASSISTANT_PREFIX)
    & filters.user(SUDOERS)
    & ~filters.user("me")
    & ~filters.me
    & ~filters.via_bot
)
async def set_pfp(client, message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        return await eor(message, text="Reply to a photo.")
    photo = await message.reply_to_message.download()
    try:
        await client.set_profile_photo(photo=photo)
        await eor(message, text="Successfully Changed PFP.")
    except Exception as e:
        await eor(message, text=e)


@Client.on_message(
    filters.command("bio", prefixes=ASSISTANT_PREFIX)
    & filters.user(SUDOERS)
    & ~filters.user("me")
    & ~filters.me
    & ~filters.via_bot
)
async def set_bio(client, message):
    if len(message.command) == 1:
        return await eor(message, text="Give some text to set as bio.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await eor(message, text="Changed Bio.")
        except Exception as e:
            await eor(message, text=e)
    else:
        return await eor(message, text="Give some text to set as bio.")


async def eor(msg: Message, **kwargs):
    func = (
        (msg.edit_text if msg.from_user.is_self else msg.reply)
        if msg.from_user
        else msg.reply
    )
    spec = getfullargspec(func.__wrapped__).args
    return await func(**{k: v for k, v in kwargs.items() if k in spec})
