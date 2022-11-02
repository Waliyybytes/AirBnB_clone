#!/usr/bin/env python3
"""
    Airbnb command line interpreter
"""
import cmd
import json
import re
import sys

from models import *
from models import storage


class HBNBCommand(cmd.Cmd):
    """
        Console v1.0
        This script inherits the cmd class with all its attributes and methods
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Closes the console """
        return True

    def emptyline(self):
        """ ensures last nonempty command is not called """
        return False

    def do_EOF(self, line):
        """ Quits the console """
        print()
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if line == "" or line is None:
            print("class name is missing")
        elif line not in storage.classes():
            print("class does not exist")
        else:
            obj = storage.classes()[line]()
            obj.save()
            print(obj.id)    

    def do_show(self, line):
        """Prints the string representation of an instance"""
        if line == "" or line is None:
            print("class name is missing")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("class doesnt exist")
            elif len(words) < 2:
                print("Instance Id is missing")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("no instance was found")
                else:
                    print(storage.all()[key])

    def do_all(self, line):
        """Prints all string representation of all instances"""
        instance_obj = storage.all()
        instance_list = []

        if line == "" or line is None:
            for key, value in storage.all().items():
                instance_list.append(str(value))
            print(instance_list)
        else:
            if line not in storage.classes():
                print("class does not exit")
                return
            else:
                for key, value in storage.all().items():
                    class_name, instance_id = key.split(".")
                    if line == class_name:
                        instance_list.append(str(value))
                print(instance_list)                

    def do_destroy(self, line):
        """Delete an instance based on the class name and id"""
        if line == "" or line is None:
            print("class name is missing")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("class does not exist")
            elif len(words) < 2:
                print("instance id is missing")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("no instance found")
                else:
                    del storage.all()[key]
                    storage.save()                  

    def do_update(self, line):
        """Update an instance based on the class name and id by adding or updating attribute"""
        checks = re.search(r"^(\w+)\s([\S]+?)\s({.+?})$", line)
        if checks:
            #whether it is a dictionary
            class_name = checks.group(1)
            instance_id = checks.group(2)
            update_dict = checks.group(3)

            if class_name is None:
                print("class name is missing")
            elif instance_id is None:
                print("instance id is missing")
            elif update_dict is None:
                print("attribute name is missing")
            else:
                if class_name not in storage.classes():
                    print("class doesnot exist")
                else:
                    key = f"{class_name}.{instance_id}"
                    if key not in storage.all():
                        print("no issue found")
                    else:
                        instance_dict = storage.all()[key]
                        update_dict = json.loads(update_dict)

                        attributes = storage.attributes()[class_name]
                        #print attributes
                        for key,value in update_dict.items():
                            if key in attributes:
                                value = attributes[key](value)
                                setattr(instance_dict,key,value)
                                storage.save()

        else:
            checks = re.search( r"^(\w+)\s([\S]+?)\s\"(.+?)\"\,\s\"(.+?)\"", line)
            class_name = checks.group(1)
            instance_id = checks.group(2)
            attribute = checks.group(3)
            value = checks.group(4)

            if class_name is None:
                print("class name is missing")
            elif instance_id is None:
                print("instance id is missing")
            elif attribute is None:
                print("attribute name is missing")
            elif value is None:
                print("value is missing")
            else:
                if class_name not in storage.classes():
                    print("class doesnt exist")
                else:
                    key = f"{class_name}.{instance_id}"
                    if key not in storage.all():
                        print("no instance found")
                    else:
                        instance_dict = storage.all()[key]
                        #print instance dictionary
                        attributes_dict = storage.attributes()[class_name]
                        #update attributes in the instance dictionary
                        value = attributes_dict[attribute](value)
                        setattr(instance_dict,attribute,value)
                        storage.save() 

    def precmd(self,line):
        #make app not work interactively
        if not sys.stdin.isatty():
            print()   

        checks = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line) 

        if checks:
            class_name = checks.group(1)
            command = checks.group(2)
            args = checks.group(3)

            if args is None:
                line = f"{command} {class_name}"
                return ''
            else:
                # print(args)
                args_checks = re.search(r"^\"([^\"]*)\"(?:, (.*))?$", args)
                # print(args_checks.group(1), args_checks.group(2))
                instance_id = args_checks[1]

                if args_checks.group(2) is None:
                    line = f"{command} {class_name} {instance_id}"
                else:
                    attribute_part = args_checks.group(2)
                    # print(attribute_part)
                    line = f"{command} {class_name} {instance_id} \
{attribute_part}"
                return ''

        return cmd.Cmd.precmd(self, line)
        # return ''

    def do_count(self, line):
        '''Counts all the instances of the class'''
        count = 0
        for key in storage.all().keys():
            class_name, instance_id = key.split(".")
            if line == class_name:
                count += 1
        print(count)

    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()    

                                                   

if __name__ == "__main__":
    HBNBCommand().cmdloop()
