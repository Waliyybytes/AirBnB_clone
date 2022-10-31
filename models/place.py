#!/usr/bin/env python3
"""
    place module
"""

import models
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class declaration """
    name = ""
    user_id = ""
    city_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Place class initialisation """
        super().__init__(*args, **kwargs)
