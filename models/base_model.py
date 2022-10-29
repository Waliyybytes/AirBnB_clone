#!/usr/bin/env python3
"""
    Base Model where UUID and date-time is here
"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """
    Blue print to my base model

    Atrribute: 
            id(str) => unique id for each individual instance
            created_at(str) => unique date for when instance was created using iso format
            updated_at(str) => unique date for when instance attribute was updated using iso format

    Method:
        __str__: prints the class name, id, and creates dictionary
        representations of the input values
        save(self): updates instance arttributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj        
    """


    def __init__(self, *args, **kwargs):

        """
        Public instance artributes initialization
        after creation
        Args:
            *args(args): arguments
            **kwargs(dict): attrubute values
        """

        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
        else:
            for key,value in kwargs.keys():
                if key == "__class__":
                    continue 
                else:
                     # check and change the format for updated_at & created_at
                    if key == "updated_at" or key == "created_at":
                        kwargs[key] = datetime.datetime.strptime(kwargs[key], DATE_TIME_FORMAT)
                    # set the attributes of the instance
                    setattr(self, key, kwargs[key])

    def __str__(self):
        """Prints string representation of the class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,self.id,self.__dict__)

    def save(self):
        """Updates the updated time to current date time"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        object_dict = {}
        for key in self.__dict__:
            if key not in ('created_at', 'updated_at'):
                object_dict[key] = self.__dict__[key]
            else:
                object_dict[key] = datetime.isoformat(self.__dict__[key])
        object_dict['__class__'] = self.__class__.__name__
        return object_dict
