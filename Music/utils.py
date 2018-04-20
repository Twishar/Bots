
import shelve
from SQLighter import SQLighter
from config import shelve_name, database_name


def count_rows():
    """
    Данный метод считает общее кол-во строк в базе данных и сохраняет в хранилище.
    Потом из этого кол-ва будем выбирать музыку
    """
    db = SQLighter(database_name)
    rowsum = db.count_rows()
    with shelve.open(shelve_name) as storage:
        storage['rows_count'] = rowsum


def get_rows_count():
    """
    Получаем из хранилища кол-во строк в БД
    :return (int) Число строк
    """
    with shelve.open(shelve_name) as storage:
        rowsnum = storage['rows_count']
    return rowsnum


def set_user_game(chat_id, estimated_answer):
    """
    Записываем юзера в игроки и запоминаем, что он должен ответить.
    :param chat_id:  id юзера
    :param estimated_answer: правильный ответ(из БД)
    """
    with shelve.open(shelve_name) as storage:
        storage[str(chat_id)] = estimated_answer


def finish_user_game(chat_id):
    """
    Заканчиваем игру текущего пользователя и удаляем правильный ответ из хранилища
    :param chat_id: id юзера
    """
    with shelve.open(shelve_name) as storage:
        del storage[str(chat_id)]


def get_answer_for_user(chat_id):
    """
    Получаем правильный ответ для текущего юзера.
    В случае, если человек просто ввел какие-то символы, не начав игру, возвращаем None
    :param chat_id: id Юзера
    :return (str) Правильный ответ / None
    """
    with shelve.open(shelve_name) as storage:
        try:
            answer = storage[str(chat_id)]
            return answer
        except KeyError:
            return None
