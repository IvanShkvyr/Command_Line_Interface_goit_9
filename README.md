# Command_Line_Interface_goit_9
A console assistant bot that will recognize commands entered from the keyboard and respond accordingly.

### "help" command  
Displays a description of all commands

    help

### "hello" command  
Responds to the console "How can I help you?"

    hello

### command "create ..."  
Stores a new contact in DB. Instead of ... the user enters the name and phone number, necessarily with a space.
"name" can consist of one word
"phone" should have the structure \+?\d?\d?\(?\d{3}.?\d{2,3}.?\d{2,3}.?\d{2,3} (for example 093-000-00-00 or +38(097)123-45-67)
example:

    create Ivan 093-111-22-33  

### command "remove ..."  
SDeletes a record in the database. Instead of ... the user enters the record number.
example:

    remove 3  

### command "update ..."  

The user can change any data in the database. Instead of ... the user enters the name of the data, the data to be 
changed and the number of the record in the database, necessarily with a space.

    update phone 093-333-44-55 3

### command "when birthday ..."  
Returns the number of days until the next birthday. Instead of ... the user enters the number of the record 
in the database.

    when birthday 3

### "show all" command  
With this command, the bot outputs all saved contacts to the console.

    show all

### "show ..." command  
Retrieves records from the database by record number

    show 3

### command "good bye", "close", "exit"  
According to any of these commands, the bot completes its work after outputting "Good bye!" to the console.

    good bye
or

    close
or

    exit
