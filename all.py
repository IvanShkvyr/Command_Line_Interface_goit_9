from re import search
from typing import Dict, Callable
from collections import UserDict


class Main:

    is_phone_is_name = {
            "help": [False, False],
            "hello": [False, False],
            "create": [True, True],
            "add phone": [True, True],
            "change phone": [True, True],
            "delate phone": [True, False],
            "show all": [False, False],
            "good bye": [False, False],
            "close": [False, False],
            "exit": [False, False]
            } 

    def run_cli(self):
        while True:

            user_input = input("Command: ")

            try:
                command, record_name, phone_number = self.parse_user_input(user_input)
            except Exception as e:
                print(e)
                continue

            command_handler = handlers.get(command)

            try:
                command_response = command_handler(record_name, phone_number)
                print(command_response)
            except SystemExit as e:
                print(e)
                break
            except Exception as e:
                print(e)
                continue


    def parse_user_input(self, user_input) -> set[str, str]:

        command, is_record_name, is_phone_number = self.matching_command(user_input)

        if is_phone_number:
            phone_number = self.matching_phone_number(user_input)
        else:
            phone_number = None
            #By default, the phone number None is given for processing commands without a phone number

        if is_record_name:
            record_name = self.matching_record_name(user_input, command, phone_number)
        else:
            record_name = None
            #By default, the name None is given for processing commands without a name

        return command, record_name, phone_number


    def matching_command(self, user_input: str):
        """
        Searches for a command in the entered pattern and returns the command
        """
        full_command = user_input.lower()  # Converts the command to lower case
        for command in handlers:
            if command in full_command:
                return command, self.is_phone_is_name[command][0], self.is_phone_is_name[command][1]
        raise ValueError("Unkown command!")


    def matching_phone_number(self, user_input): 
        """
        Searches for a phone number in the entered pattern and returns the phone number
        """
        phone = search("\+?\d?\d?\(?\d{3}.?\d{2,3}.?\d{2,3}.?\d{2,3}",user_input)
        if phone == None:
            raise AttributeError("Give me correct phone please")
        return phone.group()


    def matching_record_name(self, user_input, command, phone_number):
        """
        Searches for a name in the entered pattern and returns the name
        """
        if phone_number == None:
            phone_number = ""
        record_name = user_input.replace(command, "").replace(phone_number, "").strip()
        if len(record_name) == 0:
            raise NameError('The name is incorrect') # Raises an error if the name is not specified
        return record_name


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
    with open("README.md", "r") as fh:

        for line in fh:
            if len(line) <= 2:
                continue
            print(line)
    
    return ""


def hello_h(*args):
    return "How can i help you?"

def exit_h(*args):
    raise SystemExit("Good bye!!")


class Field:
    def __init__(self, value: str):
        self.value = value


    def __repr__(self):
        return self.value


class Name(Field):
    pass


class Phone(Field):
    pass


class Email(Field):
    pass
      

class Record:

    def __init__(self, name: Name, phone: Phone = None, email: Email = None):
        self.name: Name = name
        self.phones: list[Phone] = [phone] if phone is not None else []
        self.email = email

    def __repr__(self):
        return f"{' '.join(phone.value for phone in self.phones)}, {self.email}"

    
    def add_phone(self, phone_number: Phone):
        self.phones.append(phone_number)
        
    def change_phone(self, old_number: Phone , new_number: Phone ):
        try:
            self.phones.remove(old_number)
            self.phones.append(new_number)
        except ValueError:
            return f"{old_number} does not exist"

    def delete_phone(self, phone: Phone ):
        try:
            self.phones.remove(phone)
        except ValueError:
            return f"{phone} does not exist"


class AddressBook(UserDict):

    
    def add_contact(self, name: Name, phone: Phone = None): ###
        name = Name(name) ##############################
        phone = Phone(phone) ###################################

        # неможу викликати помилку
        # for key in self.data.keys():
        #     key = Name(key)
        #     print(f"key == {key}, {type(key)}; name == {name}, {type(name)}")
        #     if key == name:
        #         raise ValueError('The name is duplicated') # Raises an error if the name is duplicated


        contact = Record(name=name, phone=phone)
        self.data[name.value] = contact

        return "The data is recorded"




    def add_phone_A(self, name: Name, phone: Phone = None):
        name = Name(name) ##############################
        phone = Phone(phone) ###################################

        record_l = self.data.get(name.value, [])
        record_l.phones.append(phone)
        
        return "The phone is recorded"

    
    def change_phone_A(self, name: Name, phone: Phone = None):
        name = Name(name) ##############################
        phone = Phone(phone) ###################################

        record_l = self.data.get(name.value, [])
        record_l.phones.clear()
        record_l.phones.append(phone)

        return "The data has been changed"


    
    def delete_phone_A(self, name: Name, *args):
        name = Name(name) ##############################

        record_l = self.data.get(name.value, [])
        record_l.phones.clear()

        return "The data has been delate"

        

    def show_all_h(self, *args):
        all_response = "Contacts book\n"
        contacts = "\n".join(
            f"{username} contacts is {number}" for (username, number) in address_book.items()
            )
        formated_contacts = "Number does not exists? yet!" if contacts == '' else contacts
        return all_response + formated_contacts


address_book = AddressBook() # Create an instance of the class AddressBook

# Add metod add phone ----------------------------------
handlers: Dict[str, Callable] = {
    "help": help_h,
    "hello": hello_h,
    "create": address_book.add_contact,
    "add phone": address_book.add_phone_A,
    "change phone": address_book.change_phone_A,
    "delate phone": address_book.delete_phone_A,
    "show all": address_book.show_all_h,
    "good bye": exit_h,
    "close": exit_h,
    "exit": exit_h
    }

if __name__ == "__main__":
    
    phone_book = Main()  # створюємо екземпляр класу
    phone_book.run_cli()  # стартуємо головний метод