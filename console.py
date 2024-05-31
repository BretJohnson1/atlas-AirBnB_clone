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

    def preloop(self):
        """ Prints if isatty is false """
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def postcmd(self, stop, line):
        """ Prints if isatty is false """
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
            return stop

    def do_quit(self, command):
        """ Method to exit the HBNB console """
        exit()

    def help_quit(self):
        """ Prints the help documentation for quit """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_create(self, args):
        """ Create an object of any class """
        if not args:
            print("** class name missing **")
            return

        # Split the arguments by spaces
        arg_list = args.split()

        # Get the class name from the first argument
        class_name = arg_list[0]

        # CHeck if the class exists in HBNBCommand.classes
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        # Remove the class name from the argument list
        arg_list = arg_list[1:]

        # Create a dictionary to store the attributes
        attributes = {}

        # Parse and process the parameters
        for param in arg_list:
            # Split the parameter by '=' to get key and value
            param_parts = param.split('=')

        # Check if the parameter has valid format (key=value)
        if len(param_parts) != 2:
            continue

        key, value = param_parts[0], param_parts[1]

        # Unquote, underscore to space
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1].replace('_', ' ')

        # Convert values to appropriate data types (float, int, str)
        if '.' in value:
            try:
                value = float(value)
            except ValueError:
                pass
            else:
                try:
                    value = int(value)
                except ValueError:
                    pass

        # Store the key value pair in the attributes dictionary
        attributes[key] = value

        # Create an instance of the specified class with the attributes
        new_instance = HBNBCommand.classes[class_name](**attributes)

        # Save the new instance to the storage
        storage.new(new_instance)
        storage.save()

        # Print the id of the new object
        print(new_instance.id)

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")
