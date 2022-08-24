from typing import Dict, Callable
from contacts import contact_book
from contacts import AddressBook, Name, Phone, Email, Record




def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except ValueError as e:
            return ValueError
        except KeyError as e:
            return KeyError
        else:
            return result
    return wrapper


def help_h(*args):
    return "bla-bla-bla"


def hello_h(*args):
    return "How can i help you?"


@input_error
def add_h(user_name: str, numbers: str):
    if contact_book.get(user_name) is None:


        #address_book.add_contact(name=Name(value=user_name), phone=Phone(value=numbers))



        contact_book[user_name] = numbers
        return "The data is recorded"
    raise ValueError('The name is duplicated') # Raises an error if the name is duplicated


@input_error
def change_h(user_name: str, numbers: str):
    if contact_book.get(user_name) is not None:
        contact_book[user_name] = numbers
        return "The data has been changed"
    else:
        raise KeyError('The name is incorrect')  # Raises an error if such a name does not exist


def phone_h(*args):
    phone = contact_book.get(args[0])
    if phone is not None:
        return f"User number is {phone}"
    raise ValueError('There is no such record!')


def show_all_h(*args):
    all_response = "Contacts book\n"
    contacts = "\n".join(
        f"{username} number is {number}" for (username, number) in contact_book.items()
        )
    formated_contacts = "Number does not exists? yet!" if contacts == '' else contacts
    return all_response + formated_contacts


def exit_h(*args):
    raise SystemExit("Good bye!!")


handlers: Dict[str, Callable] = {
    "help": help_h,
    "hello": hello_h,
    "add": add_h,
    "change": change_h,
    "phone": phone_h,
    "show all": show_all_h,
    "good bye": exit_h,
    "close": exit_h,
    "exit": exit_h
    }