#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""
import cmd
from models import storage, classes


class HBNBCommand(cmd.Cmd):
    """Definition of the HBNBCommand class"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_help(self):
        """Help command"""
        print("More information on the existing commands")

    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates a new instance,  saves it and prints the id"""
        if line == "":
            print("** class name missing**")
        elif line in classes:
            model_new = classes[line]()
            model_new.save()
            print(model_new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the str rep of an instance based on the class name and id"""
        arg = line.split()
        if line == "":
            print("** class name missing **")
        elif arg[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg) != 2:
            print("** instance id missing **")
        elif arg[0] + "." + arg[1] not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[arg[0] + "." + arg[1]])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        arg = line.split()
        if line == "":
            print("** class name missing **")
        elif arg[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg) != 2:
            print("** instance id missing **")
        elif arg[0] + "." + arg[1] not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[arg[0] + "." + arg[1]]
            storage.save()

    def do_all(self, line):
        """Prints all string representaion of all instances"""
        if line == "":
            for value in storage.all().values():
                print([str(value)])
        elif line in classes:
            for key, value in storage.all().items():
                obj_key = key.split(".")
                if obj_key[0] == line:
                    print([str(value)])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attributes
        """
        args = line.split()
        if line == "":
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            args = args[0:4]
            key = args[0] + "." + args[1]
            instance = storage.all()[key]
            args[3] = eval(args[3])
            setattr(instance, args[2], args[3])
            instance.save()

    def default(self, line):
        """Handles cases where the command usage is different"""
        args = line.split(".")
        line = args[0]
        if line in classes:
            if args[1] == "all()":
                all = getattr(self, 'do_all')
                all(line)
            elif args[1] == "count()":
                count = 0
                for key in storage.all().keys():
                    count_key = key.split(".")
                    if count_key[0] == line:
                        count += 1
                print(count)
            elif args[1].startswith('show("') and args[1].endswith('")'):
                arg_id = args[1][6:-2]
                line = line + " " + arg_id
                show = getattr(self, 'do_show')
                show(line)
            elif args[1].startswith('destroy("') and args[1].endswith('")'):
                arg_id = args[1][9:-2]
                line = line + " " + arg_id
                destroy = getattr(self, 'do_destroy')
                destroy(line)
            elif args[1].startswith('update(') and args[1].endswith(')'):
                args[1] = args[1][7:-1]
                args = args[1].split(", ")
                for i in range(min(len(args), 2)):
                    args[i] = eval(args[i])
                line += " " + " ".join(args)
                update = getattr(self, 'do_update')
                update(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
