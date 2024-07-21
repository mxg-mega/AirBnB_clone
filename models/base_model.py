#!/usr/bin/python3
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

    def __init__(self):
        """ __init__ iniatilizes the class
            Instance Variables:
                id: unique id using the uuid1
                created_at: using datetime module to set the date created
                updated_at: sets the time the instance was last updated
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        BaseModel.nb_instances += 1

    def save(self):
        """ The save func updates the datetime
            value of the instance variable updated_at
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ to_dict returns a dict representation
            of an instance.
        """
        dict_repr = {'__class__': self.__class__.__name__}
        dict_repr.update(self.__dict__)
        dict_repr['created_at'] = str(self.created_at)
        dict_repr['updated_at'] = str(self.updated_at)
        return dict_repr

    def __str__(self):
        """ overrided str repr of an object in this format
            [<class name>] (<self.id>) <self.__dict__>
        """
        str_repr = "[{}] ({}) {}".format(__class__.__name__,
                                         self.id, self.__dict__)
        return str_repr
