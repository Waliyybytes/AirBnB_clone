#!/usr/bin/env python3
"""
    state module
"""

import models
from models.base_model import BaseModel


class State(BaseModel):
    """ State class declaration """
    name = ""

    def __init__(self, *args, **kwargs):
        """ State class initialisation """
        super().__init__(*args, **kwargs)
