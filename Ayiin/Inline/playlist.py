from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def check_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃",
                callback_data=f"playlist_check {user_id}|𝙶𝚁𝙾𝚄𝙿|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s 𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃",
                callback_data=f"playlist_check {user_id}|𝙿𝙴𝚁𝚂𝙾𝙽𝙰𝙻|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="⍟ 𝙲𝙻𝙾𝚂𝙴 ⍟​", callback_data="close")],
    ]
    return buttons


def playlist_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃​",
                callback_data=f"show_genre {user_id}|𝙶𝚁𝙾𝚄𝙿|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s 𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃",
                callback_data=f"show_genre {user_id}|𝙿𝙴𝚁𝚂𝙾𝙽𝙰𝙻|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="⍟ 𝙲𝙻𝙾𝚂𝙴 ⍟​", callback_data="close")],
    ]
    return buttons


def play_genre_playlist(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"𝙳𝙹",
                callback_data=f"play_playlist {user_id}|{type}|𝙱𝙾𝙻𝙻𝚈𝚆𝙾𝙾𝙳",
            ),
            InlineKeyboardButton(
                text=f"𝚂𝙻𝙴𝙴𝙿",
                callback_data=f"play_playlist {user_id}|{type}|𝙷𝙾𝙻𝙻𝚈𝚆𝙾𝙾𝙳",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"𝚂𝙰𝙳",
                callback_data=f"play_playlist {user_id}|{type}|𝙿𝙰𝚁𝚃𝚈",
            ),
            InlineKeyboardButton(
                text=f"𝙿𝙰𝚁𝚃𝚈",
                callback_data=f"play_playlist {user_id}|{type}|𝙻𝙾𝙵𝙸",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⍟ 𝙱𝙰𝙲𝙺 ⍟",
                callback_data=f"main_playlist {videoid}|{type}|{user_id}",
            ),
            InlineKeyboardButton(text="⍟ 𝙲𝙻𝙾𝚂𝙴 ⍟​", callback_data="close"),
        ],
    ]
    return buttons


def add_genre_markup(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"✚ 𝙳𝙹",
                callback_data=f"add_playlist {videoid}|{type}|𝚆𝙴𝙴𝙱",
            ),
            InlineKeyboardButton(
                text=f"✚ 𝙿𝙰𝚁𝚃𝚈",
                callback_data=f"add_playlist {videoid}|{type}|𝚂𝙰𝙳",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ 𝚂𝙰𝙳",
                callback_data=f"add_playlist {videoid}|{type}|𝙿𝙰𝚁𝚃𝚈",
            ),
            InlineKeyboardButton(
                text=f"✚ 𝚂𝙻𝙴𝙴𝙿",
                callback_data=f"add_playlist {videoid}|{type}|𝙻𝙾𝙵𝙸",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⍟ 𝙱𝙰𝙲𝙺 ⍟​", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="⍟ 𝙲𝙻𝙾𝚂𝙴 ⍟", callback_data="close"),
        ],
    ]
    return buttons


def check_genre_markup(type, videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"𝙳𝙹", callback_data=f"check_playlist {type}|𝚆𝙴𝙴𝙱"
            ),
            InlineKeyboardButton(
                text=f"𝙿𝙰𝚁𝚃𝚈", callback_data=f"check_playlist {type}|𝚂𝙰𝙳"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"𝚂𝙰𝙳", callback_data=f"check_playlist {type}|𝙿𝙰𝚁𝚃𝚈"
            ),
            InlineKeyboardButton(
                text=f"𝚂𝙻𝙴𝙴𝙿", callback_data=f"check_playlist {type}|𝙻𝙾𝙵𝙸"
            ),
        ],
        [InlineKeyboardButton(text="⍟ 𝙲𝙻𝙾𝚂𝙴 ⍟​", callback_data="close")],
    ]
    return buttons


def third_playlist_markup(user_name, user_id, third_name, userid, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃​",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s 𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{third_name[:16]}'s 𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃",
                callback_data=f"show_genre {userid}|third|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="⍟ 𝙲𝙻𝙾𝚂𝙴 ⍟​", callback_data="close")],
    ]
    return buttons


def paste_queue_markup(url):
    buttons = [
        [
            InlineKeyboardButton(text="▶️", callback_data=f"resumecb"),
            InlineKeyboardButton(text="⏸️", callback_data=f"pausecb"),
            InlineKeyboardButton(text="⏭️", callback_data=f"skipcb"),
            InlineKeyboardButton(text="⏹️", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton(text="𝙲𝙷𝙴𝙲𝙺𝙾𝚄𝚃 𝚀𝚄𝙴𝚄𝙴𝙳 𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃", url=f"{url}")],
        [InlineKeyboardButton(text="⍟ 𝙲𝙻𝙾𝚂𝙴 ⍟​", callback_data=f"close")],
    ]
    return buttons


def fetch_playlist(user_name, type, genre, user_id, url):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"𝙿𝙻𝙰𝚈 {user_name[:10]}'s {genre} 𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃",
                callback_data=f"play_playlist {user_id}|{type}|{genre}",
            ),
        ],
        [InlineKeyboardButton(text="𝙲𝙷𝙴𝙲𝙺𝙾𝚄𝚃 𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃", url=f"{url}")],
        [InlineKeyboardButton(text="⍟ 𝙲𝙻𝙾𝚂𝙴 ⍟​", callback_data=f"close")],
    ]
    return buttons


def delete_playlist_markuup(type, genre):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"𝚈𝙴𝚂 𝙳𝙴𝙻𝙴𝚃𝙴!",
                callback_data=f"delete_playlist {type}|{genre}",
            ),
            InlineKeyboardButton(text="⍟ 𝙽𝙾 ⍟​", callback_data=f"close"),
        ],
    ]
    return buttons
