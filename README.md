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

command "add email ..."
    Adds e-mail to the contact. Instead of ... the user enters the name and e-mail, necessarily with a space.
    example: add email Ivan Shkvyr gis2011i@gmail.com

command "change email ..."
    Changes e-mail to the entered one. Instead of ... the user enters the name and e-mail, necessarily with a space.
    example: change email Ivan Shkvyr gis2011i@gmail.com

command "delate email ..."
    Deletes e-mail in the contact. Instead of ... the user enters a name.
    example: delate email Ivan Shkvyr

command "add birthday ..."
    Adds birthday to the contact. Instead of ... the user enters the name and birthday (Numbers can be separated by any symbol), necessarily with a space.
    example: add birthday Ivan Shkvyr 12-06-1987

command "change birthday ..."
    Changes birthday to the entered one. Instead of ... the user enters the name and birthday (Numbers can be separated by any symbol), necessarily with a space.
    example: change birthday Ivan Shkvyr 19-06-1988

command "delate birthday ..."
    Deletes birthday in the contact. Instead of ... the user enters a name.
    example: delate birthday Ivan Shkvyr

command "when birthday ..."
    Returns the number of days until the next birthday. Instead of ... the user enters a name.
    example: when birthday Ivan Shkvyr

"show all" command
    With this command, the bot outputs all saved contacts with phone numbers to the console.

"show 3" command
    Outputs 3 entries from the address book at a time

command "good bye", "close", "exit"
    According to any of these commands, the bot completes its work after outputting "Good bye!" to the console.
