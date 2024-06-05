#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import datetime
import os

"""Defines a class TestBaseModel"""


class TestBaseModel(unittest.TestCase):
    """Class used for test cases"""
    def setUp(self):
        """Set up a new BaseModel instance for each test."""
        self.model = BaseModel()

    def test_save(self):
        """Test the save()"""
        original_updated_at = self.model.updated_at
        self.model.save()
        new_updated_at = original_updated_at
        self.assertEqual(original_updated_at, new_updated_at)

    def test_to_dict(self):
        """Test the to_dict()"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn("__class__", model_dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")

    def test_id(self):
        """Test the self.id"""
        self.assertIsInstance(self.model.id, str)
        self.assertTrue(len(self.model.id) > 0)

    def test_created_at(self):
        """Test the self.created_at"""
        self.assertIsInstance(self.model.created_at, datetime.datetime)

    def test_str(self):
        """Test the __str__(self)"""
        self.assertEqual(str(self.model), "[{}] ({})\
 {}".format(self.model.__class__.__name__, self.model.id, self.model.__dict__))

if __name__ == '__main__':
    unittest.main()
