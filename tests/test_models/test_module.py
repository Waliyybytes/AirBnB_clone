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

    def setup(self):
        pass

    def test_basic(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual([my_model.name,my_model.my_number],["My First Model",89])
