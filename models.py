# Внимание! Код в хранилище может отличаться от кода в репозитории.
# Код в репозитории обновляется гораздо быстрее, чем код в хранилище,
# если вдруг вносятся какие-то фиксы багов.
# Ссылка на репозиторий: https://github.com/Norrica/NewPythonCourse

class User:
    def __init__(self, user_id: str, tg_id: int, username: str):
        self.user_id = user_id
        self.tg_id = tg_id
        self.username = username


class Rating:
    def __init__(self, username: str, wins: int):
        self.username = username
        self.wins = wins
