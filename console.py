#!/usr/bin/env python3
"""
    Airbnb module
"""
import cmd
import models
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import shlex

name_convert = {"BaseModel": BaseModel, "Place": Place, "State": State,
                "City": City, "Amenity": Amenity, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """
        Console v1.0
        This script inherits the cmd class with all its attributes and methods
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """ Closes the console """
        return True

    def emptyline(self):
        """ ensures last nonempty command is not called """
        return False

    def do_EOF(self, line):
        """ Quits the console """
        print()
        return True

    def do_create(self, line):
        """
            Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id
        """
        if line in name_convert:
            new_obj = name_convert[line]()
            new_obj.save()
            print(new_obj.id)
        elif not line:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
            Prints the string representation of an instance
            based on the class name and id
        """
        lines = shlex.split(line)
        if len(lines) == 0:
            print("** class name missing **")
        elif len(lines) == 1:
            if lines[0] not in name_convert:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            obj_key = lines[0] + "." + lines[1]
            if obj_key in models.storage.all():
                print(models.storage.all()[obj_key])
            else:
                print("** no instance found **")

    def do_all(self, line):
        if line in name_convert or not line:
            print("[", end="")
            for key in models.storage.all():
                if key != list(models.storage.all())[-1]:
                    print("\"{}\"".format(models.storage.all()[key]), end=", ")
                else:
                    print("\"{}\"".format(models.storage.all()[key]), end="")
                    print("]")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        lines = shlex.split(line)
        if len(lines) == 0:
            print("** class name missing **")
        elif len(lines) == 1:
            if lines[0] not in name_convert:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            obj_key = lines[0] + "." + lines[1]
            if obj_key in models.storage.all():
                models.storage.all().pop(obj_key)
                models.storage.save()
            else:
                print("** no instance found **")

    def do_update(self, line):
        lines = shlex.split(line)
        if len(lines) == 0:
            print("** class name missing **")
        elif len(lines) == 1:
            if lines[0] not in name_convert:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            obj_key = lines[0] + "." + lines[1]
            if obj_key in models.storage.all():
                if len(lines) == 2:
                    print("** attribute name missing **")
                elif len(lines) == 3:
                    print("** value missing **")
                else:
                    setattr(models.storage.all()[obj_key], lines[2], lines[3])
                    models.storage.all()[obj_key].save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
