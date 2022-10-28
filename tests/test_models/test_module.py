#!/usr/bin/env python3
"""
Test cases for base model
"""

import os
import unittest
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test case attributes for base model
    """

    def test_basic(self):
        """Test basic attributes for base model"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        print(my_model)
        my_model.save()
        print(my_model)
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
