#!/usr/bin/python3
""" Console module """
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console """

    # Determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Place': Place,
        'Review': Review,
        'Amenity': Amenity
    }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
        'first_name': str, 'number_rooms': int, 'number_bathrooms': int, 'max_guest': int, 'price_by_night': int, 'email': str, 'latitude': float, 'longitude': float, 'last_name': str, 'password': str
            }