#!/usr/bin/python3
import json
import uuid
from datetime import datetime
""" The Base Model Class """


class BaseModel:
    """ The base model serves as
        a parent class for future subclasses
        this base class imports json, uuid and datetime
        to make unique id
    """

    nb_instances = 0

    def __init__(self, id=0):
        """ __init__ iniatilizes the class
            Instance Variables:
                id: unique id using the uuid1
                created_at: using datetime module to set the date created
                updated_at: sets the time the instance was last updated
        """
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.now())
        self.updated_at = self.created_at
        BaseModel.nb_instances += 1

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_repr = {'class': self.__class__.__name__}
        dict_repr.update(self.__dict__)
        return dict_repr
