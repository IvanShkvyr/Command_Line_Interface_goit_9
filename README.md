# Command_Line_Interface_goit_9
A console assistant bot that will recognize commands entered from the keyboard and respond accordingly.

"help" command
    Displays a description of all commands

"hello" command
    Responds to the console "How can I help you?"

command "create ..."
    Stores a new contact in memory. Instead of ... the user enters the name and phone number, necessarily with a space.
    "name" can consist of several words separated by a space
    "phone" should have the structure \+?\d?\d?\(?\d{3}.?\d{2,3}.?\d{2,3}.?\d{2,3} (for example 093-000-00-00 or +38(097)123-45-67)
    example: create Ivan Shkvyr 093-111-22-33

command "add phone ..."
    Adds another phone to the contact. Instead of ... the user enters the name and phone number, necessarily with a space.
    example: add phone Ivan Shkvyr 093-222-33-44

command "change phone ..."
    Changes all phones to the entered one. Instead of ... the user enters the name and phone number, necessarily with a space.
    example: change phone Ivan Shkvyr 093-333-44-55

command "delete phone ..."
    Deletes all phones in the contact. Instead of ... the user enters a name.
    example: delate phone Ivan Shkvyr

"show all" command
    With this command, the bot outputs all saved contacts with phone numbers to the console.

command "good bye", "close", "exit"
    According to any of these commands, the bot completes its work after outputting "Good bye!" to the console.