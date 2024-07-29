#!/usr/bin/python3
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City

""" Place Class """


class Place(BaseModel):
    """ The Place class describes
        the instances of places, data and operations associated
    """
    city_is = City.id
    user_id = User.id
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0.0
    latitude = 0.0
    longitude = 0.0
    amenity_id = Amenity.id
