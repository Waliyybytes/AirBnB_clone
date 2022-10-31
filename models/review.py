#!/usr/bin/env python3
"""
    Review module
"""

import models
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class declaration """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Review class initialisation """
        super().__init__(*args, **kwargs)
