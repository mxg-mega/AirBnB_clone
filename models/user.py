#!/usr/bin/env python3
from models.base_model import BaseModel
""" User Class """


class User(BaseModel):
    """ The User class describes
        the instances of Users, data and operations associated
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    def __init__(self, *args, **kwargs):
        """ Initialize instance """
        super().__init__(self, *args, **kwargs)
        if 'email' in kwargs.keys():
            User.email = kwargs['email']
        elif 'password' in kwargs.keys():
            User.password = kwargs['password']
        elif 'first_name' in kwargs.keys():
            User.first_name = kwargs['first_name']
        elif 'last_name' in kwargs.keys():
            User.last_name = kwargs['last_name']

