#!/usr/bin/python3
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

""" FileStorage Class """


class FileStorage:
    """ The FileStorage class takes care of
        saving the diffrent instances of each class to their
        respective json files
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with
            key <obj class name>.id
        """
        format_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects.update({format_key: obj})

    def save(self):
        """ serializes __objects to the JSON file
            (path: __file_path)
        """
        serial_obj = {}
        with open(FileStorage.__file_path, 'w') as savefile:
            for key, value in FileStorage.__objects.items():
                serial_obj[key] = value.to_dict()
            serial = json.dumps(serial_obj, indent=4)
            savefile.write(serial)

    def reload(self):
        """ deserializes the JSON file to __objects """
        deserial_obj = {}
        try:
            with open(FileStorage.__file_path, 'r') as jfile:
                contents = jfile.read()
                deserial = json.loads(contents)
                for key, value in deserial.items():
                    deserial_obj[key] = classes[value['__class__']](**value)
                FileStorage.__objects = deserial_obj
        except FileNotFoundError:
            pass
