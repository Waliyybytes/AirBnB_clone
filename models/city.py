#!/usr/bin/env python3
"""
    city module
"""

import models
from models.base_model import BaseModel


class City(BaseModel):
    """ City class declaration """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """City class initialisation """
        super().__init__(*args, **kwargs)
