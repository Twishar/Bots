
from vedis import Vedis
import config


# Пытаемся из базы узнать состояние пользователя
def get_current_state(user_id):
    with Vedis(config.db_file) as db:
        try:
            return db[user_id]
        except KeyError:
            return config.States.S_START.value  # Значение по умолчанию - начало диалога


# Сохраняем текущее "состояние" пользователя в нашу базу
def set_state(user_id, value):
    with Vedis(config.db_file) as db:
        try:
            db[user_id] = value
            return True
        except Exception:
            # Обработка ситуации
            return False
