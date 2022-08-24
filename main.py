from handlers import handlers
from parser import parse_user_input
from contacts import AddressBook

address_book = AddressBook() # Create an instance of the class AddressBook

class Main_CLI:

    

    def run_cli(self):
        while True:

            user_input = input("Command: ")

            try:
                command, record_name, phone_number = parse_user_input(user_input)
            except Exception as e:
                print(e)
                continue

            command_handler = handlers.get(command)

            try:
                print(type(record_name))
                print(type(phone_number))
                command_response = command_handler(record_name, phone_number)
                print(command_response)
            except SystemExit as e:
                print(e)
                break
            except Exception as e:
                print(e)
                continue


if __name__ == "__main__":
    
    phone_book = Main_CLI()  # створюємо екземпляр класу
    phone_book.run_cli()  # стартуємо головний метод