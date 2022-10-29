#!/usr/bin/env python3
"""
    User Class inherits it attritubes and methods from base model
"""

import uuid
from datetime import datetime
import models
from models.BaseModel import BaseModel

class User(BaseModel):
    """
    Blue print to user onject

    Attribute:
        Email => email of the user
        Password => password to the user's account
        first_name => this is the first name of the user
        last_name > this is the last name of the user

        User will inherit id,date_created and date_updated from parent class
    """
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, *kwargs):
        """Initializes attributes for the user class"""
        super().__init__(*args, **kwargs)
        