#!/usr/bin/python3
"""console"""
import cmd, sys
from models.base_model import BaseModel
import models
from models.user import User

model = {"BaseModel": BaseModel,
         "User": User
         }

class HBNBCommand(cmd.Cmd):
    """cmd class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True;

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True;

    def emptyline(self):
        """empty line + enter"""
        pass

    def do_create(self, arg):
        """creates new instance"""
        x = arg.split()
        if len(x) == 0:
            print("** class name missing **")
        elif x[0] not in model:
            print("** class doesn't exist **")
        else:
            for key, value  in model.items():
                if x[0] == key:
                    ins = value()
                    ins.save()
                    print(ins.id)

    def do_show(self, arg):
        """prints string representation based on class name and id"""
        commands = arg.split()
        objs = models.storage.all()
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in model:
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        else:
            elem = commands[0] + "." + commands[1]
            if str(elem) in models.storage.all():
                print(objs[elem])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """deletes an instance"""
        commands = arg.split()
        objs = models.storage.all()
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in model:
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        else:
            elem = commands[0] + "." + commands[1]
            if str(elem) in models.storage.all():
                models.storage.all().pop(elem)
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        commands = arg.split()
        objs = models.storage.all()
        lis = []
        if len(commands) == 0:
            for key in objs:
                lis.append(objs[key].__str__())
            print(lis)
        elif commands[0] in model:
            for key in objs:
                if objs[key].__class__.__name__ == commands[0]:
                    lis.append(objs[key].__str__())
            print(lis)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()