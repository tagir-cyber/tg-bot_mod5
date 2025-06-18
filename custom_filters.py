# Внимание! Код в хранилище может отличаться от кода в репозитории.
# Код в репозитории обновляется гораздо быстрее, чем код в хранилище,
# если вдруг вносятся какие-то фиксы багов.
# Ссылка на репозиторий: https://github.com/Norrica/NewPythonCourse

from pyrogram import filters
from pyrogram.types import KeyboardButton, Message


def button_filter(button: KeyboardButton):
    async def func(_, __, message: Message):
        return message.text == button.text

    return filters.create(func, "ButtonFilter", button=button)


def reply_text_filter(text: str):
    async def func(_, __, message: Message):
        return message.reply_to_message and message.reply_to_message.text == text

    return filters.create(func, "ReplyTextFilter", text=text)
