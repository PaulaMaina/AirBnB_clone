# AirBnB_clone
## Overview
The AirBnB clone project demonstrates different concepts learned in Python. It portrays the use of classes, inheritance, serialization, and deserialization, using unit tests to validate the project's classes, functions, methods, and storage engine.

The project entails developing a command interpreter that works the same way a Python interpreter works. The console created should execute commands such as EOF, create, all, quit, help, destroy, and update.

It should be able to effectively and efficiently execute the commands in interactive and non-interactive mode.

## Cloning the repository
Clone the repository to your terminal in your desired working directory. To clone the repository, run the following command in your terminal:
`git clone <url of repo>`

### Getting started
Once the repo has been cloned, ensure that all files are executable. To give execution rights, you can use the following command in each directory:
`chmod u+x *` for all files or `chmod u+x <file>` for individual files.

### Usage
For usage, run the following command to your command line for interactive mode:
`./console.py`

The prompt should be "(hbnb) "

For non-interactive mode, please use the following format:
`echo "<cmd>" | ./console.py`

The results will be displayed to the stdout along with your shell's prompt, indicating the program has exited after executing the command.

### Commands
Command | Description
--------|-------------
help    | Displays all available commands in console
EOF     | Exits console, equivalent of ctrl D
quit    | Exits console, equivalent of ctrl C
create  | Creates a new instance
show    | Prints string representation of an instance
all     | Prints all string representation or of a specified class
update  | Updates attributes of an instance and saves
destroy | Deletes specified instance

### Examples
* Interactive mode console
```
$ ./console
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```
* Non-interactive mode console
```
$ echo "help" | ./console
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) $
```

