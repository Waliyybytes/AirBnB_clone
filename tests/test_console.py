#!/usr/bin/python3
"""Module for testing the HBNB Class"""
from email import message
from pydoc import classname
from tokenize import String
import unittest
from models import storage
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import re
import json
from datetime import datetime

class TestConsole(unittest.TestCase):
    """Test the HBNB Console"""

    def test_help(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        message = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

"""
        self.assertEqual(message, f.getvalue())

    def test_help_EOF(self):
        """Test help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            message = ' Quits the console \n'
            self.assertEqual(message,f.getvalue())    

    def test_help_quit(self):
        """Test the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            message = 'Closes the console \n'
            self.assertEqual(message,f.getvalue())  

    def test_help_create(self):
        """Test the help command"""               
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            message = 'Creates a new instance of BaseModel\n'
            self.assertEqual(message,f.getvalue())  

    def test_help_show(self):
        """Test the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            message = 'Prints the string representation of an instance\n'
            self.assertEqual(message,f.getvalue())  

    def test_help_destroy(self):
        """Test the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            message = 'Delete an instance based on the class name and id\n'
            self.assertEqual(message,f.getvalue())  

    def test_help_all(self):
        """Test the help command"""  
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            message = 'Prints all string representation of all instances\n'
            self.assertEqual(message,f.getvalue())

    def test_help_count(self):
        """Test the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
            message = 'Counts all the instances of the class\n'
            self.assertEqual(message,f.getvalue())          

    def test_help_update(self):
        """Tests the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
        message = 'Update an instance based on the class name and id by adding or updating attribute\n'
        self.assertEqual(message, f.getvalue())

    def test_quit(self):
        """Test the quit commannd"""    
        with patch('sys.stdout',new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            message = f.getvalue()
            self.assertTrue(len(message) == 0)
            self.assertEqual("",message)
        with patch('sys.stdout',new=StringIO()) as f:
            HBNBCommand().onecmd("quit console")
            message = f.getvalue()
            self.assertTrue(len(message) == 0)
            self.assertEqual("",message)   

    def test_EOF(self):
        """Tests EOF commmand."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 1)
        self.assertEqual("\n", msg)
        with patch('sys.stdout',new=StringIO()) as f:
            HBNBCommand().onecmd("EOF console")
            message = f.getvalue()
            self.assertTrue(len(message) == 1)
            self.assertEqual("\n",message)

        
    def test_emptyline(self):
        """Tests emptyline functionality."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        message = ""
        self.assertEqual(message, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("                  \n")
        message = ""
        self.assertEqual(message, f.getvalue())    
      
    def test_create(self):
        """Test case for creating classes"""
        for classname in storage.classes():
            self.help_test_create(classname)

    def help_test_create(self,classname):
        """Functin to help test create"""
        with patch('sys.stdout',new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
            uid = f.getvalue()[:-1] 
            self.assertTrue(len(uid) > 0)
            

    def test_create_error(self):
        """Test create commands with errors"""
        with patch('sys.stdout',new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            message = f.getvalue()[:-1]
            self.assertEqual(message,"class name is missing")
        with patch('sys.stdout',new=StringIO()) as f:
            HBNBCommand().onecmd("create something")
            message = f.getvalue()[:-1]    
            self.assertEqual(message,"class does not exist")

    def test_show(self):
        """Test the show command"""
        for classname in storage.classes():
            self.help_test_show(classname)

    def help_test_show(self,classname):
        """Function to help test show command"""
        with patch('sys.stdout',new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
            uid = f.getvalue()[:-1]
            self.assertTrue(len(uid) > 0)

        with patch('sys.stdout',new=StringIO()) as f:
            HBNBCommand().onecmd("show {} {}".format(classname, uid))
            message = f.getvalue()[:-1]
            self.assertTrue(uid in message) 


    def test_do_show_error(self):
        """Tests show command with errors."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        message = f.getvalue()[:-1]
        self.assertEqual(message, "class name is missing")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show unknown")
        message = f.getvalue()[:-1]
        self.assertEqual(message, "class doesnt exist")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
        message = f.getvalue()[:-1]
        self.assertEqual(message, "Instance Id is missing")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 6524359")
        message = f.getvalue()[:-1]
        self.assertEqual(message, "no instance was found")    

    def test_destroy(self):
        """Test the destroy command"""
        for classname in storage.classes():
            self.help_test_destroy(classname)

    def help_test_destroy(self,classname):
        """Helps test destroy function"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy {} {}".format(classname, uid))
        message = f.getvalue()[:-1]
        self.assertTrue(len(message) == 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".all()")
        self.assertFalse(uid in f.getvalue())

    
    def test_do_destroy_error(self):
        """Tests destroy command with errors."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        message = f.getvalue()[:-1]
        self.assertEqual(message, "class name is missing")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy garbage")
        message = f.getvalue()[:-1]
        self.assertEqual(message, "class does not exist")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
        message = f.getvalue()[:-1]
        self.assertEqual(message, "instance id is missing")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 6524359")
        message = f.getvalue()[:-1]
        self.assertEqual(message, "no instance found")

    def test_all(self):
        """Tests all for all classes."""
        for classname in storage.classes():
            self.help_test_all(classname)


    def help_test_all(self, classname):
        """Helps test the all command."""
        with patch('sys.stdout',new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
            uid = f.getvalue()[:-1]
            self.assertTrue(len(uid) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        message = f.getvalue()[:-1]
        self.assertTrue(len(message) > 0)
        self.assertIn(uid, message)


    def test_all_error(self):
        """Tests all command with errors."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all garbage")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "class does not exit")

    # def test_count_all(self):
    #     """Tests count for all classes."""
    #     for classname in storage.classes():
    #         self.help_test_count_advanced(classname)

    # def help_test_count_advanced(self, classname):
    #     """Helps test .count() command."""
    #     for i in range(20):
    #         with patch('sys.stdout',new=StringIO()) as f:
    #             HBNBCommand().onecmd("create {}".format(classname))
    #             uid = f.getvalue()[:-1]
    #             self.assertTrue(len(uid) > 0)
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         HBNBCommand().onecmd("count {}".format(classname))
    #     message = f.getvalue()[:-1]
    #     self.assertTrue(len(message) > 0)
    #     self.assertEqual(message, "20")


    # def test_do_count_error(self):
    #     """Tests .count() command with errors."""
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         HBNBCommand().onecmd("garbage.count()")
    #     msg = f.getvalue()[:-1]
    #     self.assertEqual(msg, "** class doesn't exist **")
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         HBNBCommand().onecmd(".count()")
    #     msg = f.getvalue()[:-1]
    #     self.assertEqual(msg, "** class name missing **")


    def help_load_dict(self, rep):
        """Helper method to test dictionary equality."""
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(rep)
        self.assertIsNotNone(res)
        s = res.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        d = json.loads(s.replace("'", '"'))
        return d

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def attributes(self):
        """Returns the valid attributes and their types for classname."""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime,
                      "updated_at": datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
                     {"place_id": str,
                      "user_id": str,
                      "text": str}
        }
        return attributes