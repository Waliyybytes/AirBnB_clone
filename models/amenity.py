#!/usr/bin/env python3
"""
    amenity module
"""

import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class declaration """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Amenity class initialisation """
        super().__init__(*args, **kwargs)
