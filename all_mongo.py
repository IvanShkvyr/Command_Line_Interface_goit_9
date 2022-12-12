from re import search
from typing import Dict, Callable
from mongoengine import Document

# SQL DB
# from crud import create_record, remove_record, show_all, show_record, days_to_birthday, update_address, update_birthday, \
#     update_email, update_phone, update_last_name, update_first_name, update_black_list

# NoSQL DB
from crud_mongo import create_record, remove_record, show_all, show_record, days_to_birthday, update_address, update_birthday, \
    update_email, update_phone, update_last_name, update_first_name, update_black_list

class Main:

    # The data structure "is_phone_is_name"
    # is_phone_is_name[command][0]==name,
    # is_phone_is_name[command][1]==phone,
    # is_phone_is_name[command][2]==email,
    # is_phone_is_name[command][3]==birthday
    # is_phone_is_name[command][4]==id

    # for NoSQL DB
    is_phone_is_name = {
                "help": [False, False, False, False, False],
                "hello": [False, False, False, False, False],
                "create": [True, True, False, False, False],
                "remove": [True, False, False, False, False],
                "update login": [True, False, False, False, True],
                "update last name": [True, False, False, False, True],
                "update phone": [True, True, False, False, False],
                "update email": [True, False, True, False, False],
                "update birthday": [True, False, False, True, False],
                "update address": [True, False, False, False, True],
                "update black list": [True, False, False, False, True],
                "when birthday": [True, False, False, False, False],
                "show all": [False, False, False, False, False],
                "show": [True, False, False, False, False],
                "good bye": [False, False, False, False, False],
                "close": [False, False, False, False, False],
                "exit": [False, False, False, False, False]
                }


    def run_cli(self):
        while True:

            user_input = input("Command: ")

            # command, data_tail, id_ = self.parse_user_input(user_input)

            try:
                command, data_tail, id_ = self.parse_user_input(user_input)
            except Exception as e:
                print(e)
                continue

            command_handler = handlers.get(command)


            try:
                command_response = command_handler(id_, data_tail)
                if command_response is not None:
                    print(command_response)
            except SystemExit as e:
                print(e)
                break
            except Exception as e:
                print(e)
                continue

    def parse_user_input(self, user_input) -> set[str, str]:
        command, is_record_name, is_phone_number, is_email, is_birthday, is_tail = self.matching_command(user_input)

        if is_tail:
            tail = self.matching_id(user_input)
        else:
            tail = None
            # By default, the birthday None is given for processing commands without a id

        if is_phone_number:
            phone_number = self.matching_phone_number(user_input)
        else:
            phone_number = None
            # By default, the phone number None is given for processing commands without a phone number

        if is_email:
            email = self.matching_email(user_input)
        else:
            email = None
            # By default, the email None is given for processing commands without a email


        if is_birthday:
            birthday = self.matching_birthday(user_input)
        else:
            birthday = None
            # By default, the birthday None is given for processing commands without a birthday

        if is_record_name:
            if is_email:
                record_name = self.matching_record_name(user_input, command, email)
            elif is_birthday:
                record_name = self.matching_record_name(user_input, command, birthday)
            elif is_phone_number:
                record_name = self.matching_record_name(user_input, command, phone_number)
            else:
                record_name = self.matching_record_name(user_input, command, tail)
        else:
            record_name = None
            # By default, the name None is given for processing commands without a name

        # for NoSQL DB
        if command == "create":
            return command, phone_number, record_name
        if is_email:
            return command, email, record_name
        elif is_birthday:
            return command, birthday, record_name
        elif is_phone_number:
            return command, phone_number, record_name
        else:
            return command, tail, record_name

    def matching_command(self, user_input: str):
        """
        Searches for a command in the entered pattern and returns the command
        """
        full_command = user_input.lower()  # Converts the command to lower case
        for command in handlers:
            if command in full_command:
                return command, self.is_phone_is_name[command][0], self.is_phone_is_name[command][1],\
                       self.is_phone_is_name[command][2], self.is_phone_is_name[command][3],\
                       self.is_phone_is_name[command][4]
        raise ValueError("Unkown command!")

    def matching_phone_number(self, user_input):
        """
        Searches for a phone number in the entered pattern and returns the phone number
        """
        phone = search("\+?\d?\d?\(?\d{3}.?\d{2,3}.?\d{2,3}.?\d{2,3}",user_input)
        if phone is None:
            raise AttributeError("Give me correct phone please")
        return phone.group()

    def matching_email(self, user_input):
        """
        Searches for a e-mail in the entered pattern and returns the e-mail
        """
        email = search("\w+[.]?\w*[.]?\w*[.]?\w*\@\w{2,100}\.\w{2,100}",user_input)
        if email is None:
            raise AttributeError("Give me correct e-mail please")
        return email.group()

    def matching_birthday(self, user_input):
        """
        Searches for a birthday in the entered pattern and returns the birthday
        """
        birthday = search("\d\d\d\d.\d\d.\d\d",user_input)
        if birthday is None:
            raise AttributeError("Give me correct birthday please")
        birthday = birthday.group()
        if int(birthday[0:4]) > 2022 or int(birthday[0:4]) < 1900 or int(birthday[5:7]) > 12 or int(birthday[8:]) > 31:
            raise AttributeError("Give me correct birthday please")
        return f'{birthday[0:4]}-{birthday[5:7]}-{birthday[8:]}'

    def matching_record_name(self, user_input, command, tail):
        """
        Searches for a name in the entered pattern and returns the name
        """
        if tail is None:
            tail = ""
        record_name = user_input.replace(command, "").replace(tail, "").strip()
        if len(record_name) == 0:
            raise NameError('The name is incorrect') # Raises an error if the name is not specified
        return record_name

    def matching_id(self, user_input):
        """
        Searches for a id in the entered pattern and returns the name
        """
        index = user_input.rfind(' ')
        if index == -1:
            raise AttributeError("Give me correct id")
        id_ = user_input[index + 1:]

        return id_


def _normalize_phones(phone):
    """Normalizes the expression for searching by phone"""
    norm_phone = ""
    for char in phone:
        if char.isdigit():
            norm_phone += char
    phone_pattern = "[" + "].?[".join(norm_phone) + "]"
    return phone_pattern


def help_h(*args):
    with open("README_mongo.md", "r") as fh:
        for line in fh:
            if len(line) <= 2:
                continue
            print(line)
    return ""


def hello_h(*args):
    return "How can i help you?"


def exit_h(*args):
    raise SystemExit("Good bye!!")


handlers: Dict[str, Callable] = {
    "help": help_h,
    "hello": hello_h,
    "create": create_record,
    "remove": remove_record,
    "update login": update_first_name,
    "update last name": update_last_name,
    "update phone": update_phone,
    "update email": update_email,
    "update birthday": update_birthday,
    "update address": update_address,
    "update black list": update_black_list,
    "when birthday": days_to_birthday,
    "show all": show_all,
    "show": show_record,
    "good bye": exit_h,
    "close": exit_h,
    "exit": exit_h
    }


if __name__ == "__main__":
    phone_book = Main()  # Create an instance of the class
    phone_book.run_cli()  # Run the main method

    
