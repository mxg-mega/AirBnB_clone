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

    time_format = '%Y-%m-%dT%H:%M:%S.%f'

    def __init__(self, *args, **kwargs):
        """ __init__ iniatilizes the class
            Instance Variables:
                id: unique id using the uuid1
                created_at: using datetime module to set the date created
                updated_at: sets the time the instance was last updated
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.id = kwargs['id']
            self.created_at = datetime.strptime(kwargs['created_at'],
                                                BaseModel().time_format)
            self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                BaseModel().time_format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            from models import storage
            storage.new(self)

    def save(self):
        """ The save func updates the datetime
            value of the instance variable updated_at
        """
        self.updated_at = datetime.utcnow()
        from models import storage
        storage.save()

    def to_dict(self):
        """ to_dict returns a dict representation
            of an instance.
        """
        dict_repr = {'__class__' : self.__class__.__name__}
        dict_repr.update(self.__dict__)
        dict_repr.update({'created_at': self.created_at.isoformat()})
        dict_repr.update({'updated_at': str(self.updated_at.isoformat())})
        return dict_repr

    def __str__(self):
        """ returns a string repr in this format:
            [<class name>] (<self.id>) <self.__dict__>
        """
        dict_rep = self.__dict__
        cls = self.__class__.__name__
        str_rep = "[{:s}] ({:s}) {}".format(cls, self.id, dict_rep)
        return str_rep
