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
        if line != "" or line is not None:
            if line not in storage.classes():
                print("line does not exits")
            else:
                #creates and instance of a given class   
                obj_instance = storage.classes()[line]()
                obj_instance.save()
                print(object_instance.id) 
        else:
            print("class name is missing")        

    def do_show(self, line):
        """
            Prints the string representation of an instance
            based on the class name and id
        """
        if line = "" or line is None:
            print("class name is missing")
        else:
            #get all arguements passed via command line
            class_info = line.split(" ")
            if len(class_info) < 2:
                print("Instance Id is missing")
            else:
                class_name = class_info[0]
                instance_id = class_info[1]
                #check if class name exits
                if class_name in storage.classes():
                    key = f"{class_name}.{instance_id}"
                    if key not in storage.all():
                        print("no instance was found")
                    else:
                        instance_dict = storage.all()[key]
                        print(instance_dict) 
                else:
                    print("class doesnt exit")

    def do_all(self, line):
        instance_obj = storage.all()
        instace_list = []

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
                        class_name, instance_id = key_split(".")
                        if line == class_name:
                            instance_list.append(str(value))
                    print(instance_list)                

    def do_destroy(self, line):
        if line is ="" or line is None:
            print("class name is missing")
        else:
            #get all the arguements passed through the command line
            class_info = line.slit(" ")
            if len(class_info) < 2:
                print("instance id is missing")
            else:
                class_name = class_info[0]
                instance_id = class_info[1]
                #checks if class name exits
                if class_name in storage.classess():
                    #check if instance id exits
                    key = f"{class_name}.{instance_id}"
                    if key not in storage.all():
                        print("no instance found")
                    else:
                        #delete the instance 
                        del storage.all()[key]
                        storage.save()
                        return
                else:
                    print("class does not exist")                    

    def do_update(self, line):
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
                    if key not in storage.all()
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
                if name not in storage.classes():
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
        '''Usage: 1. count <class name> | 2. <class name>.count()
Function: Counts all the instances  of the class
        '''
        count = 0
        for key in storage.all().keys():
            class_name, instance_id = key.split(".")
            if line == class_name:
                count += 1
        print(count)

                                                   

if __name__ == "__main__":
    HBNBCommand().cmdloop()
