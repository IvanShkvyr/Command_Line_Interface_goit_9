from handlers import handlers
from re import search


is_phone_is_name = {
            "help": [False, False],
            "hello": [False, False],
            "add": [True, True],
            "change": [True, True],
            "phone": [True, False],
            "show all": [False, False],
            "good bye": [False, False],
            "close": [False, False],
            "exit": [False, False]
            } 


def parse_user_input(user_input) -> set[str, str]:

    command, is_record_name, is_phone_number = matching_command(user_input)

    if is_phone_number:
        phone_number = matching_phone_number(user_input)
    else:
        phone_number = None
        #By default, the phone number None is given for processing commands without a phone number

    if is_record_name:
        record_name = matching_record_name(user_input, command, phone_number)
    else:
        record_name = None
        #By default, the name None is given for processing commands without a name

    return command, record_name, phone_number


def matching_command(user_input: str):
    """
    Searches for a command in the entered pattern and returns the command
    """
    full_command = user_input.lower()  # Converts the command to lower case
    for command in handlers:
        if command in full_command:
            return command, is_phone_is_name[command][0], is_phone_is_name[command][1]
    raise ValueError("Unkown command!")


def matching_phone_number(user_input): 
    """
    Searches for a phone number in the entered pattern and returns the phone number
    """
    phone = search("\+?\d?\d?\(?\d{3}.?\d{2,3}.?\d{2,3}.?\d{2,3}",user_input)
    if phone == None:
        raise AttributeError("Give me correct phone please")
    return phone.group()


def matching_record_name(user_input, command, phone_number):
    """
    Searches for a name in the entered pattern and returns the name
    """
    if phone_number == None:
        phone_number = ""
    record_name = user_input.replace(command, "").replace(phone_number, "").strip()
    if len(record_name) == 0:
        raise NameError('The name is incorrect') # Raises an error if the name is not specified
    return record_name