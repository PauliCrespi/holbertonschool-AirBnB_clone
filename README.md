<h1 align="center">
AirBnB clone - The console
</h1>

<h2 align="center">
By: Nicolle Shiskobcki and Paulina Crespi
</h2>

# INTRODUCTION:

This console will allow to change the type of storage easily without updating all of your codebase. It will be a tool to validate the storage engine.

Our aim is to create our data model, manage (create, update, destroy, etc) objects via a console / command interpreter, store and persist objects to a file (JSON file).

The first piece is to manipulate a powerful storage system. This storage engine will give an abstraction between “My object” and “How they are stored and persisted”. 
This means: from the console code (the command interpreter itself) and from the front-end and RestAPI we will build later.

## HOW TO USE IT:

To open the console type:

$ ./console.py

The console wil print a prompt(hbnb) and expect you to type a command:

$ (hbnb) 

### COMMANDS:

- help

Prints a list of documented commands

- help [command]

Prints a description of the command

- quit

Exits the program

- EOF

Exits the program

- create [ClassName]

Creates a new instance of the ClassName, saves it (to the JSON file) and prints the id.

- show [ClassName] [id]

Prints the string representation of an instance based on the class name and id.

- destroy [ClassName] [id]

Deletes an instance based on the class name and id (save the change into the JSON file).

- all 

Prints all string representation of all instances.

- all [ClassName]

Prints all string representation of all instances based on the class name.

- update [class name] [id] [attribute name] "[attribute value]"

Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).


EXAMPLES:

$ ./console.py

$ (hbnb) help

Documented commands (type help [topic]):

==================================================

EOF help quit create all show destroy update 


$ (hbnb) help quit 

Quit command to exit the program

$ (hbnb) all

["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2022, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2022, 10, 2, 3, 11, 23, 639724)}, [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'created_at': datetime.datetime(2022, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2022, 9, 28, 21, 11, 42, 848291)"]

$ (hbnb) all BaseModel

["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2022, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2022, 10, 2, 3, 11, 23, 639724)}"]

$ (hbnb) create BaseModel

$ (hbnb) show BaseModel 1234-1234-1234

["[BaseModel] (1234-1234-1234) {'id': '1234-1234-1234', 'created_at': datetime.datetime(2022, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2022, 10, 2, 3, 11, 23, 639724)}"]

$ (hbnb) destroy BaseModel 1234-1234-1234

$ (hbnb) update User 38f22813-2753-4d42-b37c-57a17f1e4f88 email "aibnb@mail.com"


## AUTHORS:

- * **Nicolle Shiskobcki** - [NikShiskobcki](https://github.com/NikShiskobcki)
- * **Paulina Crespi** - [PauliCrespi](https://github.com/PauliCrespi)
