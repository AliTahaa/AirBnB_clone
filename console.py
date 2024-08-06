#!/usr/bin/python3
'''HBNB console'''
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ HBNB class """

    prompt = "(hbnb) "
    my_classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def default(self, line):
        try:
            args = line.split(".")
            class_name = args[0]
            args2 = args[1].split("(")
            command = args2[0]
            args3 = args2[1].split(")")
            class_id = args3[0]
        except:
            print("*** Unknown syntax: {}".format(line))
            return
        self.onecmd("{} {} {}".format(command, class_name, class_id))

    def do_quit(self, line):
        """ Quit command to exit the program """
        return 1

    def do_EOF(self, line):
        """ EOF (end-of-file) command to exit the program """
        return 1

    def emptyline(self):
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif arg not in self.my_classes:
            print("** class doesn't exist **")
        else:
            model = eval(args[0])()
            model.save()
            print(model.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.my_classes:
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
        """ Deletes an instance based on the class name and id """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.my_classes:
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
        """ Prints all string representation of all instances. """
        commands = arg.split()
        obj_dict = storage.all()
        if len(commands) == 0:
            for key, value in obj_dict.items():
                print(str(value))
        elif commands[0] not in self.my_classes:
            print("** class doesn't exist **")
        else:
            for key, value in obj_dict.items():
                if key.split(".")[0] == commands[0]:
                    print(str(value))

    def do_update(self, arg):
        """ Updates an instance based on the class name and id. """
        commands = arg.split()
        obj_dict = storage.all()

        if len(commands) == 0:
            print("** class name missing **")
            return False
        elif commands[0] not in self.my_classes:
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

    def do_count(self, arg):
        '''Count the number of instances of a class'''
        count = 0
        for key in storage.all().keys():
            if arg in key:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
