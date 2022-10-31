#!/usr/bin/env python3
"""
Help stores dictionary to a JSON format for serialization and deserialization
"""
import json
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

name_convert = {"BaseModel": BaseModel, "Place": Place, "State": State,
                "City": City, "Amenity": Amenity, "Review": Review}


class FileStorage:
    """
        File Storage class that serializes and deserializes the instance
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj"""
        if obj is not None:
            obj_key = obj.__class__.__name__ + "." + obj.id
            self.__objects[obj_key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        obj_json = {}
        for key in self.__objects:
            obj_json[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(obj_json, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                j_obj = json.load(f)
            for key in j_obj:
                self.__objects[key] = name_convert[j_obj[key]
                                                   ["__class__"]](j_obj[key])
        except Exception:
            pass
