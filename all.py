from collections import UserDict
from datetime import datetime
from pickle import dump, load
from re import search
from typing import Dict, Callable


class Main:

    # The data structure "is_phone_is_name"
    # is_phone_is_name[command][0]==name, is_phone_is_name[command][1]==phone, is_phone_is_name[command][2]==email, is_phone_is_name[command][3]==birthday
    is_phone_is_name = {
                "help": [False, False, False, False],
                "hello": [False, False, False, False],
                "create": [True, True, False, False],
                "add phone": [True, True, False, False],
                "change phone": [True, True, False, False],
                "delate phone": [True, False, False, False],
                "add email": [True, False, True, False],
                "change email": [True, False, True, False],
                "delate email": [True, False, False, False],
                "add birthday": [True, False, False, True],
                "change birthday": [True, False, False, True],
                "delate birthday": [True, False, False, False],
                "when birthday": [True, False, False, False],
                "show all": [False, False, False, False],
                "show 3": [False, False, False, False],
                "good bye": [False, False, False, False],
                "close": [False, False, False, False],
                "exit": [False, False, False, False],
                "save": [False, False, False, False],
                "load": [False, False, False, False],
                "find by phone": [True, False, False, False],
                "find by name": [True, False, False, False],
                } 

    def run_cli(self):
        while True:

            user_input = input("Command: ")

            try:
                command, record_name, data_tail = self.parse_user_input(user_input)
            except Exception as e:
                print(e)
                continue

            command_handler = handlers.get(command)

            try:
                command_response = command_handler(record_name, data_tail)
                print(command_response)
            except SystemExit as e:
                print(e)
                break
            except Exception as e:
                print(e)
                continue

    def parse_user_input(self, user_input) -> set[str, str]:
        command, is_record_name, is_phone_number, is_email, is_birthday = self.matching_command(user_input)

        if is_phone_number:
            phone_number = self.matching_phone_number(user_input)
        else:
            phone_number = None
            #By default, the phone number None is given for processing commands without a phone number

        if is_email:
            email = self.matching_email(user_input)
        else:
            email = None
            #By default, the email None is given for processing commands without a email

        if is_birthday:
            birthday = self.matching_birthday(user_input)
        else:
            birthday = None
            #By default, the birthday None is given for processing commands without a birthday

        if is_record_name:
            if is_email:
                record_name = self.matching_record_name(user_input, command, email)
            elif is_birthday:
                record_name = self.matching_record_name(user_input, command, birthday)
            else:
                record_name = self.matching_record_name(user_input, command, phone_number)
        else:
            record_name = None
            #By default, the name None is given for processing commands without a name
        
        if is_email:
            return command, record_name, email
        elif is_birthday:
            return command, record_name, birthday
        else:
            return command, record_name, phone_number

    def matching_command(self, user_input: str):
        """
        Searches for a command in the entered pattern and returns the command
        """
        full_command = user_input.lower()  # Converts the command to lower case
        for command in handlers:
            if command in full_command:
                return command, self.is_phone_is_name[command][0], self.is_phone_is_name[command][1], self.is_phone_is_name[command][2], self.is_phone_is_name[command][3]
        raise ValueError("Unkown command!")

    def matching_phone_number(self, user_input): 
        """
        Searches for a phone number in the entered pattern and returns the phone number
        """
        phone = search("\+?\d?\d?\(?\d{3}.?\d{2,3}.?\d{2,3}.?\d{2,3}",user_input)
        if phone == None:
            raise AttributeError("Give me correct phone please")
        return phone.group()

    def matching_email(self, user_input):
        """
        Searches for a e-mail in the entered pattern and returns the e-mail
        """
        email = search("\w+[.]?\w*[.]?\w*[.]?\w*\@\w{2,100}\.\w{2,100}",user_input)
        if email == None:
            raise AttributeError("Give me correct e-mail please")
        return email.group()

    def matching_birthday(self, user_input):
        """
        Searches for a birthday in the entered pattern and returns the birthday
        """
        birthday = search("\d\d.\d\d.\d\d\d\d",user_input)
        if birthday == None:
            raise AttributeError("Give me correct birthday please")
        birthday = birthday.group()
        if int(birthday[0:2]) > 31 or int(birthday[3:5]) > 12 or int(birthday[6:]) > 2022 or int(birthday[6:]) < 1900:
            raise AttributeError("Give me correct birthday please")
        return birthday

    def matching_record_name(self, user_input, command, tail):
        """
        Searches for a name in the entered pattern and returns the name
        """
        if tail == None:
            tail = ""
        record_name = user_input.replace(command, "").replace(tail, "").strip()
        if len(record_name) == 0:
            raise NameError('The name is incorrect') # Raises an error if the name is not specified
        return record_name


class Field:
    def __init__(self, value: str):
        self.__value = value

    
    @property
    def value(self):
        return self.__value


    def __repr__(self):
        return self.value


class Name(Field):
    
    @Field.value.setter
    def value(self, value):
        self.__value = value


class Phone(Field):
    
    @Field.value.setter
    def value(self, value):
        self.__value = value


class Email(Field):
    
    @Field.value.setter
    def value(self, value):
        self.__value = value
      

class Birthday(Field):
    
    @Field.value.setter
    def value(self, value):
        self.__value = value


class Record:

    def __init__(self, name: Name, phone: Phone = None, email: Email = None, birthday: Birthday = None):
        self.name: Name = name
        self.phones: list[Phone] = [phone] if phone is not None else []
        self.emails = email
        self.birthdays = birthday

    def __repr__(self):
        return f"{self.name}, {' '.join(phone.value for phone in self.phones)}, {self.emails}, {self.birthdays}"
       
    def add_phone(self, name: Name, phone: Phone = None):
        """Adds information about a new phone to the Record"""
        name = Name(name)
        phone = Phone(phone)
        self.data.get(name.value, []).phones.append(phone)
        return "The phone is recorded"

    def change_phone(self, name: Name, phone: Phone = None):
        """Changes all phone records to a new one"""
        name = Name(name)
        phone = Phone(phone)
        self.data[name.value].phones.clear()
        self.data[name.value].phones.append(phone)
        return "The data has been changed"

    def delate_phone(self, name: Name, phone: Phone = None):
        """Removes phones"""
        name = Name(name)
        phone = Phone(phone)
        try:
            self.data[name.value].phones.clear()
            return "The phones has been delate" 
        except ValueError:
            return f"{phone} does not exist"

    def add_email(self,name: Name, email: Email = None):
        """Adds information about an email address to the Record"""
        name = Name(name)
        email = Email(email)
        self.data.get(name.value, []).emails = email
        return "The email is recorded"

    def change_email(self,name: Name, email: Email = None):
        """Changes email address"""
        name = Name(name)
        email = Email(email)
        self.data[name.value].emails = email
        return "The e-mail has been changed" 

    def delate_email(self,name: Name, email: Email = None):
        """Deletes an email address"""
        name = Name(name)
        self.data[name.value].emails = None
        return "The e-mail has been delate" 

    def add_birthday(self,name: Name, birthday: Birthday = None):
        """Adds birthday information to the Record"""
        name = Name(name)
        birthday = birthday[0:2] + "_" + birthday[3:5] + "_" + birthday[6:]
        birthday = Birthday(birthday)
        self.data.get(name.value, []).birthdays = birthday
        return "The birthday is recorded"

    def change_birthday(self,name: Name, birthday: Birthday = None):
        """Deletes the date of birth"""
        name = Name(name)
        birthday = birthday[0:2] + "_" + birthday[3:5] + "_" + birthday[6:]
        birthday = Birthday(birthday)
        self.data[name.value].birthdays = birthday
        return "The birthday has been change" 

    def delate_birthday(self,name: Name, birthday: Birthday = None):
        """Deletes the date of birth"""
        name = Name(name)
        self.data[name.value].birthdays = None
        return "The birthday has been delate" 

    def days_to_birthday(self,name: Name, birthday: Birthday = None):
        """Returns the number of days until the next birthday"""
        name = Name(name)
        current_date, current_year, next_year = current_date_and_year()

        birthday = (datetime.strptime(str(self.data[name.value].birthdays), '%d_%m_%Y')).date()
        birthday = birthday.replace(year=current_year)

        if birthday < current_date:
            result = (birthday.replace(year=next_year) - current_date).days
        elif birthday > current_date:
            result = (birthday - current_date).days
        else:
            return f"Today {name}'s birthday!!!"
        return f" There are {result} days left until {name}'s birthday"

    def find_by_name(self, name: Name, *args):
        """Searches for records by name match"""
        found_name = ""
        for address_name in address_book.data.keys():
            if name.lower() in address_name.lower():
                us_name = address_book.data[address_name].name
                us_phone = address_book.data[address_name].phones
                us_email = address_book.data[address_name].emails
                us_birthday = address_book.data[address_name].birthdays
                found_name += f"{us_name}- tel: {us_phone}; e-mail: {us_email}; birthday: {us_birthday}\n"
        if not found_name:
            found_name = "The search did not yield any results"
        return found_name

    def find_by_phone(self, phone, *args):
        """Searches for records by phone match"""
        phone_pattern = self._normalize_phones(phone)
        found_phones = ""

        for address_name in address_book.data.keys():
            for phone in address_book.data[address_name].phones:
                flag = search(phone_pattern, str(phone))
                if flag:
                    us_name = address_book.data[address_name].name
                    us_phone = address_book.data[address_name].phones
                    us_email = address_book.data[address_name].emails
                    us_birthday = address_book.data[address_name].birthdays
                    found_phones += f"{us_name}- tel: {us_phone}; e-mail: {us_email}; birthday: {us_birthday}\n"
        if not found_phones:
            found_phones = "The search did not yield any results"
        
        return found_phones

    def _normalize_phones (self, phone):
        """Normalizes the expression for searching by phone"""
        norm_phone = ""
        for char in phone:
            if char.isdigit():
                norm_phone += char
        phone_pattern = "[" + "].?[".join(norm_phone) + "]"
        return phone_pattern


class AddressBook(UserDict, Record):

    MAX_VALUE_ON_PAGE = 3
    count = 0

    def __next__(self):
        keys_list = list(self.data)
        if self.count < len(keys_list) - self.MAX_VALUE_ON_PAGE:
            element = ""
            for n in range(self.MAX_VALUE_ON_PAGE):
                element += f"{keys_list[self.count + n]}: {self.data[keys_list[self.count + n]]}\n" 
            self.count += self.MAX_VALUE_ON_PAGE
            return element
        else:
            tail = (len(keys_list) - self.count)
            element = ""
            for n in range(tail):
                element += f"{keys_list[self.count + n]}: {self.data[keys_list[self.count + n]]}\n" 
            print(element)
            raise StopIteration("End of records")

    def __iter__(self):
        return self
 
    def add_contact(self, name: Name, phone: Phone = None, *args):
        """Adds a new contact to Record (Name and phone)"""
        name = Name(name)
        phone = Phone(phone)
        contact = Record(name=name, phone=phone)
        self.data[name.value] = contact
        return "The data is recorded"

    def show_all_h(self, *args):
        """Returns all records"""
        all_response = "Contacts book\n"
        contacts = "\n".join(
            f"{username} contacts is {number}" for (username, number) in address_book.data.items()
            )
        formated_contacts = "Number does not exists? yet!" if contacts == '' else contacts
        return all_response + formated_contacts

    def show_3_records(self, *args):
        """Returns 3 records"""
        return self.__next__()
    
    def save_address_book(self, *args):
        
        with open("save.bin", "wb") as file:
            dump(self.data, file)
        return "The Address Book has been saved"
        
    def load_address_book(self, *args):
        with open ("save.bin", "rb") as file:
            self.data = load(file)
        return "The Address Book has been loaded"


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


def current_date_and_year():
    """Returns the current date, the current year, and the next year"""
    current_date = datetime.now().date()
    current_year = current_date.year
    next_year = current_year + 1
    return current_date, current_year, next_year


address_book = AddressBook() # Create an instance of the class AddressBook


handlers: Dict[str, Callable] = {
    "help": help_h,
    "hello": hello_h,
    "create": address_book.add_contact,
    "add phone": address_book.add_phone,
    "change phone": address_book.change_phone,
    "delate phone": address_book.delate_phone,
    "add email": address_book.add_email,
    "change email": address_book.change_email,
    "delate email": address_book.delate_email,
    "add birthday": address_book.add_birthday,
    "change birthday": address_book.change_birthday,
    "delate birthday": address_book.delate_birthday,
    "when birthday": address_book.days_to_birthday,
    "show all": address_book.show_all_h,
    "show 3": address_book.show_3_records,
    "good bye": exit_h,
    "close": exit_h,
    "exit": exit_h,
    "save": address_book.save_address_book,
    "load": address_book.load_address_book,
    "find by phone": address_book.find_by_phone,
    "find by name": address_book.find_by_name
    }


if __name__ == "__main__":
    phone_book = Main()  # Create an instance of the class
    phone_book.run_cli()  # Run the main method

    
