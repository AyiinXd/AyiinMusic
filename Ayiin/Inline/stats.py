from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

stats1 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="System Stats", callback_data="sys_stats"
            ),
            InlineKeyboardButton(
                text="Storage Stats", callback_data="sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(text="Bot Stats", callback_data="bot_stats"),
            InlineKeyboardButton(
                text="MongoDB Stats", callback_data="mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Assistant Stats", callback_data="assis_stats"
            )
        ],
    ]
)


stats2 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="General Stats", callback_data="gen_stats"
            ),
            InlineKeyboardButton(
                text="Storage Stats", callback_data="sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(text="Bot Stats", callback_data="bot_stats"),
            InlineKeyboardButton(
                text="MongoDB Stats", callback_data="mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Assistant Stats", callback_data="assis_stats"
            )
        ],
    ]
)


stats3 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="System Stats", callback_data="sys_stats"
            ),
            InlineKeyboardButton(
                text="General Stats", callback_data="gen_stats"
            ),
        ],
        [
            InlineKeyboardButton(text="Bot Stats", callback_data="bot_stats"),
            InlineKeyboardButton(
                text="MongoDB Stats", callback_data="mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Assistant Stats", callback_data="assis_stats"
            )
        ],
    ]
)


stats4 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="System Stats", callback_data="sys_stats"
            ),
            InlineKeyboardButton(
                text="Storage Stats", callback_data="sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="General Stats", callback_data="gen_stats"
            ),
            InlineKeyboardButton(
                text="MongoDB Stats", callback_data="mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Assistant Stats", callback_data="assis_stats"
            )
        ],
    ]
)


stats5 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="System Stats", callback_data="sys_stats"
            ),
            InlineKeyboardButton(
                text="Storage Stats", callback_data="sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(text="Bot Stats", callback_data="bot_stats"),
            InlineKeyboardButton(
                text="General Stats", callback_data="gen_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Assistant Stats", callback_data="assis_stats"
            )
        ],
    ]
)


stats6 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="System Stats", callback_data="sys_stats"
            ),
            InlineKeyboardButton(
                text="Storage Stats", callback_data="sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(text="Bot Stats", callback_data="bot_stats"),
            InlineKeyboardButton(
                text="MongoDB Stats", callback_data="mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="General Stats", callback_data="gen_stats"
            )
        ],
    ]
)



stats7 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Getting Assistant Stats....", callback_data="wait_stats"
            )
        ]
    ]
)
