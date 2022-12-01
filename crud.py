from datetime import datetime

from conn import session
from models import AddressBook


def create_record(first_name: str, phone: str) -> None:
    todo = AddressBook(first_name=first_name, phone=phone)
    session.add(todo)
    session.commit()


def update_first_name(user_id: int, data_: str) -> None:
    todo = session.query(AddressBook).filter(AddressBook.id == user_id)
    todo.update({AddressBook.first_name: data_})
    session.commit()


def update_last_name(user_id: int, data_: str) -> None:
    todo = session.query(AddressBook).filter(AddressBook.id == user_id)
    todo.update({AddressBook.last_name: data_})
    session.commit()


def update_phone(user_id: int, data_: str) -> None:
    todo = session.query(AddressBook).filter(AddressBook.id == user_id)
    todo.update({AddressBook.phone: data_})
    session.commit()


def update_email(user_id: int, data_: str) -> None:
    todo = session.query(AddressBook).filter(AddressBook.id == user_id)
    todo.update({AddressBook.email: data_})
    session.commit()


def update_birthday(user_id: int, data_: str) -> None:
    data_ = datetime.strptime(data_, '%Y-%m-%d')
    todo = session.query(AddressBook).filter(AddressBook.id == user_id)
    todo.update({AddressBook.birthday: data_})
    session.commit()


def update_address(user_id: int, data_: str) -> None:
    todo = session.query(AddressBook).filter(AddressBook.id == user_id)
    todo.update({AddressBook.address: data_})
    session.commit()


def update_black_list(user_id: int, data_: str) -> None:
    if data_.title() == 'True' or data_ == '1':
        data_ = True
    else:
        data_ = False
    todo = session.query(AddressBook).filter(AddressBook.id == user_id)
    todo.update({AddressBook.black_list: data_})
    session.commit()


def remove_record(user_id: int, *args) -> None:
    todo = session.query(AddressBook).filter(AddressBook.id == user_id)
    todo.delete()
    session.commit()


def show_all(*args) -> str:
    message = ''
    message += "|{:^3}|{:^22}|{:^20}|{:^30}|{:^70}|{:^12}|{:^12}|\n".format("№", "full name", "phone", "e-mail",
                                                                            "address", "birthday", "black_list")
    message += "-" * 175 + '\n'
    for person in session.query(AddressBook).all():
        if person.birthday is None:
            birthday = 'None'
        else:
            birthday = person.birthday.strftime('%d %m %Y')

        message += ("|{:^3}|{:^22}|{:^20}|{:^30}|{:^70}|{:^12}|{:^12}|\n".format(person.id, person.fullname,
                                                                                 person.phone, person.email,
                                                                                 person.address, birthday,
                                                                                 person.black_list))
    return message


def show_record(user_id: int, *args) -> str:
    person = session.query(AddressBook).filter(AddressBook.id == user_id).first()
    message = ''
    message += "|{:^3}|{:^22}|{:^20}|{:^30}|{:^70}|{:^12}|{:^12}|\n".format("№", "full name", "phone", "e-mail",
                                                                            "address", "birthday", "black_list")
    message += "-" * 175 + '\n'
    if person.birthday is None:
        birthday = 'None'
    else:
        birthday = person.birthday.strftime('%d %m %Y')

    message += ("|{:^3}|{:^22}|{:^20}|{:^30}|{:^70}|{:^12}|{:^12}|\n".format(person.id, person.fullname, person.phone,
                                                                             person.email, person.address, birthday,
                                                                             person.black_list))
    return message


def days_to_birthday(user_id: int, *args) -> str:
    """Returns the number of days until the next birthday"""
    person = session.query(AddressBook).filter(AddressBook.id == user_id).first()

    current_date, current_year, next_year = _current_date_and_year()

    birthday = person.birthday
    birthday = birthday.replace(year=current_year)

    if birthday < current_date:
        result = (birthday.replace(year=next_year) - current_date).days
    elif birthday > current_date:
        result = (birthday - current_date).days
    else:
        return f"Today {person.fullname}'s birthday!!!"
    return f" There are {result} days left until {person.fullname}'s birthday"


def _current_date_and_year():
    """Returns the current date, the current year, and the next year"""
    current_date = datetime.now().date()
    current_year = current_date.year
    next_year = current_year + 1
    return current_date, current_year, next_year


if __name__ == '__main__':

    print(days_to_birthday(2))

