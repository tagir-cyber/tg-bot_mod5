# Внимание! Код в хранилище может отличаться от кода в репозитории.
# Код в репозитории обновляется гораздо быстрее, чем код в хранилище,
# если вдруг вносятся какие-то фиксы багов.
# Ссылка на репозиторий: https://github.com/Norrica/NewPythonCourse

from pyrogram.types import ReplyKeyboardMarkup

import buttons

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [buttons.profile_button, buttons.rating_button],
        [buttons.settings_button],
    ],
    resize_keyboard=True,
)

settings_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [buttons.sign_up_button, buttons.back_button],
    ],
    resize_keyboard=True,
)
