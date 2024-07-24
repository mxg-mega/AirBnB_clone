#!/usr/bin/python3
import json
from models.base_model import BaseModel
""" FileStorage Class """


class FileStorage(BaseModel):
    """ The FileStorage class takes care of
        saving the diffrent instances of each class to their
        respective json files
    """
    def __init__(self, file_path='file.json', obj={}):
        """ Initializes the class for storing of information
            Args:
                __file_path: path to JSON file
                __objects: dictionary of objects
                            the keys are in format "<class_name>.id"
        """
        self.__file_path = file_path
        self.__objects = obj

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with
            key <obj class name>.id
        """
        format_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects.update({format_key: obj})

    def save(self):
        """ serializes __objects to the JSON file
            (path: __file_path)
        """
        serial_obj = {}
        with open(self.__file_path, 'w') as savefile:
            for key, value in self.__objects.items():
                serial_obj[key] = value.to_dict()
            serial = json.dumps(serial_obj, indent=4)
            savefile.write(serial)

    def reload(self):
        """ deserializes the JSON file to __objects """
        deserial_obj = {}
        try:
            with open(self.__file_path, 'r') as jfile:
                contents = jfile.read()
                deserial = json.loads(contents)
                for key, value in deserial.items():
                    deserial_obj[key] = BaseModel(**value)
                self.__objects = deserial_obj
        except:
            print()
