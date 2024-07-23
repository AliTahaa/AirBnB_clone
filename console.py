#!/usr/bin/python3
'''HBNB console'''
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    '''HBNB class'''

    prompt = "(hbnb) "

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return 1

    def do_EOF(self, line):
        '''EOF (end-of-file) command to exit the program'''
        return 1

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            model = BaseModel()
            model.save()
            print(model.id)

    def do_show(self, arg):
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
