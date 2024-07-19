#!/usr/bin/env python3
import sys
# directory reach
directory = '../..'
# setting path
sys.path.append(directory)
from models.base_model import BaseModel
""" FileStorage Class """


class FileStorage(BaseModel):
    """ The FileStorage class takes care of
        saving the diffrent instances of each class to their
        respective json files
    """
