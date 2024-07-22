#!/usr/bin/python3
"""Doc
"""
from models.base_model import *
from models.base_model import BaseModel


class BaseModel(BaseModel):
    """Doc
    """

    def __str__(self):
        """Doc
        """
        return "Fake"


if __name__ == '__main__':
    b = BaseModel()
    print(b)
