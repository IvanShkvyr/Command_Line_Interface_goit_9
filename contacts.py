from typing import Dict
from collections import UserDict

contact_book: Dict [str, str] = {}


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



class AddressBook(UserDict):
    
    def add_contact(self, name: Name, phone: Phone = None, email: Email = None): ###
        contact = Record(phone=phone, email=email)
        self.data[name.value] = contact

    def add_record(self, record: "Record"):
        self.data[record.name.value] = record

    def find_by_name(self, name):
        try:
            return self.data[name]
        except KeyError:
            return None

    def find_by_phone(self, phone: str):
        for record in self.data.values():  # type: Record
            if phone in [number.value for number in record.phones]:
                return record
        return None

    def show_all_h(self):
        return self.data



        

class Record:

    def __init__(self, phone: Phone = None, email: Email = None):

    # def __init__(self, name: Name, phone: Phone = None):
    #     self.name: Name = name

        self.phones: list[Phone] = [phone] if phone is not None else []
        self.email = email

    def __repr__(self):
        return f"{' '.join(phone.value for phone in self.phones)}, {self.email}"
        

    def add_phone(self, phone_number: Phone):
        self.phones.append(phone_number)

    def change_contact(self, old_number: Phone , new_number: Phone ):
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