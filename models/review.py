#!/usr/bin/python3
from models.base_model import BaseModel
from models.place import Place
from models.user import User
""" Review Class """


class Review(BaseModel):
    """ The Review class describes
        the instances of reviews, data and operations associated
    """
    place_id = Place.id
    user_id = User.id
    text = ''
