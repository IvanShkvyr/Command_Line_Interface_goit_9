from handlers import handlers
from parser import parse_user_input

def main():
    while True:
        user_input = input("Command: ")

        try:
            command, record_name, phone_number = parse_user_input(user_input)
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


if __name__ == "__main__":
    main()