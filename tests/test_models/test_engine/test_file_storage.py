#!/user/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os

"""Defines a class TestFileStorage"""


class TestFileStorage(unittest.TestCase):
    """Class used for test cases"""
    def setUp(self):
        """Set up a new BaseModel instance for each test."""
        self.filestorage = FileStorage()
        self.model = BaseModel()
        self.model_key = "{}.{}".format(self.model.__class__.__name__, self.model.id)

    def tearDown(self):
        """tear down after each test"""
        from models import storage
        self.storage._FileStorage__objects.clear()
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_obj_create_retrieve(self):
        """Test creating and retrieving objects"""
        from models import storage
        self.storage.new(self.model)
        objs = self.storage.all()

    if __name__ == '__main__':
        unittest.main()
