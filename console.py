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
        '''Creates a new instance of BaseModel'''
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            model = BaseModel()
            model.save()
            print(model.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
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

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
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
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        commands = arg.split()
        obj_dict = storage.all()
        if len(commands) == 0:
            for key, value in obj_dict.items():
                print(str(value))
        elif commands[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            for key, value in obj_dict.items():
                if key.split(".")[0] == commands[0]:
                    print(str(value))

    def do_update(self, arg):
        """Updates an instance."""
        commands = arg.split()
        obj_dict = storage.all()

        if len(commands) == 0:
            print("** class name missing **")
            return False
        elif commands[0] != "BaseModel":
            print("** class doesn't exist **")
            return False
        elif len(commands) == 1:
            print("** instance id missing **")
            return False
        elif "{}.{}".format(commands[0], commands[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        elif len(commands) == 2:
            print("** attribute name missing **")
            return False
        elif len(commands) == 3:
            print("** value missing **")
            return False

        else:
            obj = obj_dict["{}.{}".format(commands[0], commands[1])]
            att_name = commands[2]
            att_value = commands[3]
            try:
                attr_value = eval(attr_value)
            except Exception:
                pass
            setattr(obj, att_name, att_value)
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
