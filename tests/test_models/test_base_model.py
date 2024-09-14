#!/usr/bin/python3
"""
Base model test
"""
import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    # Test case for initializing the model
    def test_init(self):
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    # Test case for saving the model
    def test_save(self):
        my_model = BaseModel()

        initial_updated_at = my_model.updated_at

        my_model.save()

        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    # Test case for converting the model to a dictionary
    def test_to_dict(self):
        my_model = BaseModel()

        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)

        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'],
                         my_model.created_at.isoformat())
        self.assertEqual(my_model_dict['updated_at'],
                         my_model.updated_at.isoformat())

    # Test case for checking the string representation of the model
    def test_str(self):
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))

        self.assertIn(my_model.id, str(my_model))

        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == "__main__":
    unittest.main()
