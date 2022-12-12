from datetime import datetime

from mongoengine.errors import NotUniqueError

from conn_mongo import User


def create_record(login: str, phone: str) -> None:
    try:
        todo = User(login=login, phone=phone).save()
    except NotUniqueError as err:
        return "Duplicate key error"


def update_first_name(login: str, data_: str) -> None:
    todo = User.objects(login=login)
    todo.update(login=data_)


def update_last_name(login: str, data_: str) -> None:
    todo = User.objects(login=login)
    todo.update(last_name=data_)


def update_phone(login: str, data_: str) -> None:
    todo = User.objects(login=login)
    todo.update(phone=data_)


def update_email(login: str, data_: str) -> None:
    todo = User.objects(login=login)
    todo.update(email=data_)


def update_birthday(login: str, data_: str) -> None:
    todo = User.objects(login=login)
    todo.update(birthday=data_)


def update_address(login: str, data_: str) -> None:
    todo = User.objects(login=login)
    todo.update(address=data_)


def update_black_list(login: str, data_: str) -> None:
    todo = User.objects(login=login)
    todo.update(black_list=data_)


def remove_record(login: str, *args) -> None:
    todo = User.objects(login=login)
    todo.delete()


def show_all(*args):
    todo = User.objects()
    for el in todo:
        print(el.to_mongo().to_dict())


def show_record(login: str, *args) -> str:
    todo = User.objects(login=login)
    for el in todo:
        return el.to_mongo().to_dict()


def days_to_birthday(login: str, *args) -> str:
    """Returns the number of days until the next birthday"""


    todo = User.objects(login=login)
    current_date, current_year, next_year = _current_date_and_year()

    for el in todo:
        user = el.to_mongo().to_dict()

    birthday = user['birthday']

    birthday = datetime.strptime(birthday, '%Y-%m-%d')  # \d\d\d\d.\d\d.\d\d to 2020-01-10 00:00:00
    birthday = birthday.date()

    birthday = birthday.replace(year=current_year)

    if birthday < current_date:
        result = (birthday.replace(year=next_year) - current_date).days
    elif birthday > current_date:
        result = (birthday - current_date).days
    else:
        return f"Today {login}'s birthday!!!"
    return f" There are {result} days left until {login}'s birthday"


def _current_date_and_year():
    """Returns the current date, the current year, and the next year"""
    current_date = datetime.now().date()
    current_year = current_date.year
    next_year = current_year + 1
    return current_date, current_year, next_year


if __name__ == '__main__':

    print(days_to_birthday(2))

    # Створив одного користувача
    one = User(login="Ivan2").save()

    # Знайти когось якусь характеристику
    # two = User.objects(login="Ivan")
    # for p in two:
    #     print(p.to_mongo().to_dict(), "1")
    # print("------------")

    # Знайти все
    # t = User.objects()
    # for p in t:
    #     print(p.to_mongo().to_dict())

    # додати якусь характеристику
    # two = User.objects(login="Ivan")
    # two.update(last_name="Nelson")
    # two.update(phone=['1665656'])
    # two.update(email="buijuihjuh")
    # two.update(address="hggyhgiugh")
    # two.update(birthday="jhghuh")

    # Видалити когось
    # two = User.objects(login="Ivan")
    # two.delete()