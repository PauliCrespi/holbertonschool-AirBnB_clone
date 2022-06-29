#!/usr/bin/python3
"""console"""
import cmd, sys
from models.base_model import BaseModel
import models

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
        elif x[0] == "BaseModel":
            ins = BaseModel()
            ins.save()
            print(ins.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """prints string representation based on class name and id"""
        x = args.split(" ")
        if len(x) == 0:
            print("** class name missing **")
        elif x[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(x) == 1:
            print("** instance id missing **")
        else:
            elem = x[0] + "." + x[1]
            if str(elem) in models.storage.all():
                print(models.storage.all[elem])
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
