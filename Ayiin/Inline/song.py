from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def song_markup(videoid, duration, user_id, query, query_type):
    buttons = [
        [
            InlineKeyboardButton(
                text="❮",
                callback_data=f"song_right B|{query_type}|{query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳",
                callback_data=f"qwertyuiopasdfghjkl {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"song_right F|{query_type}|{query}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⍟ 𝙲𝙻𝙾𝚂𝙴 ⍟​",
                callback_data=f"forceclose {query}|{user_id}",
            )
        ],
    ]
    return buttons


def song_download_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="☟︎︎︎ 𝙶𝙴𝚃 𝙰𝚄𝙳𝙸𝙾",
                callback_data=f"gets audio|{videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="☟︎︎︎ 𝙶𝙴𝚃 𝚅𝙸𝙳𝙴𝙾",
                callback_data=f"gets video|{videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⍟ 𝙲𝙻𝙾𝚂𝙴 ⍟​",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons
