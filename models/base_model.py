#!/usr/bin/env python3
"""
    Base Model where UUID and date-time is here
"""

import uuid
import datetime
import time

class BaseModel:
    """Blue print to my base model"""


    def __init__(self, id, created_at, updated_at):

        today = datetime.datetime.now()
        string_date = today.isoformat()

        self.id = str(uuid.uuid4())
        self.created_at = string_date
        self.updated_at = string_date

    def __str__(self):
        """Prints string representation of the class"""
        return "{},{},{}".format(self.__class__.__name__,self.id,self.__dict__)

    def save(self):
        """Updates the updated time to current date time"""
        self.updated_at = string_date

    def to_dict(self):
        """Saves class instances and date to dictionary"""
        map_object = {}
        for key,value in self.__dict__.item():
            if key == "created_at" or key == "updated_at":
                map_object[key] == value.isoformat()
            else:
                map_object[key] == value
            map_object[__class__] == self.__class__.__name__
        return map_object                
