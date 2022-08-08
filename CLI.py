from re import search


PHONE_BOOK = {}

def main():
    while True:
        full_command = input()

        # Looks for the team and determines the need for a phone number and name
        command, is_record_name, is_phone_number = matching_command(full_command)  

        if is_phone_number:
            phone_number = matching_phone_number(full_command)
        else:
            phone_number = "000-000-00-00"
            #By default, the phone number "000-000-00-00" is given for processing commands without a phone number

        if is_record_name:
            record_name = matching_record_name(full_command, command, phone_number)
        else:
            record_name = "name"
            #By default, the name "name" is given for processing commands without a name

        if command == "close" or command == "good bye" or command == "exit":
            print("Good bye!")
            break

        if command == "error": # Skips iteration and displays an error message in the command
            print("Enter the correct command")
            continue

        if phone_number == "mistake_phone":  # Skips iteration and displays an error message in the phone number
            print("Give me correct phone please")
            continue

        handler = get_handler(command)  # Selects commands from the dictionary
        result = handler(phone_number, record_name)

        if result == "The name is duplicated":  # Skips iteration and displays an error message in the name
            print("The name is duplicated")
            continue
        elif result == "The name is incorrect":
            print("The name is incorrect")
            continue

        print(result)

        

def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except AttributeError:
            return "mistake_phone"
        except NameError:
            return "The name is duplicated"
        except KeyError:
            return "The name is incorrect"
        else:
            return result
    return inner


def matching_command(full_command):
    """
    Searches for a command in the entered pattern and returns the command
    """
    full_command = full_command.lower()  # Converts the command to lower case
    for command in COMMANDS:
        if command in full_command:
            return command, COMMANDS[command][1], COMMANDS[command][2]
    return "error", False, False


@input_error
def matching_phone_number(full_command): 
    """
    Searches for a phone number in the entered pattern and returns the phone number
    """ 
    phone = search("\+?\d?\d?\(?\d{3}.?\d{2,3}.?\d{2,3}.?\d{2,3}",full_command)
    return phone.group()


@input_error
def matching_record_name(full_command, command, phone_number):
    """
    Searches for a name in the entered pattern and returns the name
    """
    record_name = full_command.replace(command, "").replace(phone_number, "").strip()
    if len(record_name) == 0:
        raise NameError('The name is incorrect') # Raises an error if the name is not specified
    return record_name


def hello(phone_number, record_name):
    return "How can I help you?"


@input_error
def add(phone_number, record_name):
    if record_name in PHONE_BOOK:
        raise NameError('The name is duplicated') # Raises an error if the name is duplicated
    PHONE_BOOK[record_name] = phone_number
    return "The data is recorded"


@input_error
def change(phone_number, record_name):
    if PHONE_BOOK[record_name]:
        PHONE_BOOK[record_name] = phone_number
        return "The data has been changed"
    else:
        raise NameError('The name is incorrect')  # Raises an error if such a name does not exist


@input_error
def phone(phone_number, record_name):
    return PHONE_BOOK[record_name]


def show_all(phone_number, record_name):
    return PHONE_BOOK


COMMANDS = {"hello": [hello, False, False],"add": [add, True, True],"change": [change , True, True],
"phone": [phone, True, False],"show all": [show_all, False, False], "good bye": ["good bye", False, False],
"close": ["close", False, False],"exit": ["exit", False, False]} 
# "close", "show all", "good bye" commands have no functions, and are handled through "if"


def get_handler(command):
    return COMMANDS[command][0]


if __name__ == "__main__":
    main()