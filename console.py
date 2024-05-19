#!/usr/bin/python3
"""the HBnB console."""
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class."""

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

    def do_quit(self, arg):
        """exit the program."""
        return True

    def do_EOF(self, arg):
        """exit the program."""
        print("")
        return True

    def emptyline(self):
        """don't execute anything."""
        pass

    def do_create(self, arg):
        """Creates a new instance"""
        commands = split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.my_classes:
            print("** class doesn't exist **")
        else:
            new = eval(commands[0])()
            print(new.id)
            storage.save()

    def do_show(self, arg):
        """ Prints the string representation of an instance"""
        commands = split(arg)
        obj_dict = storage.all()
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.my_classes:
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(commands[0], commands[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(commands[0], commands[1])])

    def do_destroy(self, arg):
        """Deletes an instance."""
        commands = split(arg)
        obj_dict = storage.all()
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.my_classes:
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(commands[0], commands[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(commands[0], commands[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        commands = split(arg)
        obj_dict = storage.all()
        if len(commands) == 0:
            for key, value in obj_dict.items():
                print(str(value))
        elif commands[0] not in self.my_classes:
            print(" ** class doesn't exist ** ")
        else:
            for key, value in obj_dict.items():
                if key.split(".")[0] == commands[0]:
                    print(str(value))

    def do_update(self, arg):
        """Updates an instance."""
        commands = split(arg)
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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
