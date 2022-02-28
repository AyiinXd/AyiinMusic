from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Ayiin import db_mem


def others_markup(videoid, user_id):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 1
    buttons = [
        [
            InlineKeyboardButton(
                text="🔎 𝚂𝙴𝙰𝚁𝙲𝙷 𝙻𝚈𝚁𝙸𝙲𝚂",
                callback_data=f"lyrics {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="✚ 𝚈𝙾𝚄𝚁 𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃",
                callback_data=f"your_playlist {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="✚ 𝙶𝚁𝙾𝚄𝙿 𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃",
                callback_data=f"group_playlist {videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="☟︎︎︎ 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝚄𝙳𝙸𝙾/𝚅𝙸𝙳𝙴𝙾",
                callback_data=f"audio_video_download {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="❮ 𝙶𝙾 𝙱𝙰𝙲𝙺",
                callback_data=f"pr_go_back_timer {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="⍟ 𝙲𝙻𝙾𝚂𝙴 ⍟",
                callback_data=f"close",
            ),
        ],
    ]
    return buttons


def download_markup(videoid, user_id):
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
                text="❮ 𝙶𝙾 𝙱𝙰𝙲𝙺", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="•Cʟᴏsᴇ•​", callback_data=f"close"),
        ],
    ]
    return buttons
