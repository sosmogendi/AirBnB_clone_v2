#!/usr/bin/python3
"""Test for the BaseModel class."""
import unittest
import os
from os import getenv
from models import storage
from models.base_model import BaseModel
from models.state import State
import pep8
import MySQLdb
import datetime


class TestBaseModel(unittest.TestCase):
    """This class will test the BaseModel class."""

    @classmethod
    def setUpClass(cls):
        """Set up for the test."""
        cls.base = BaseModel()
        cls.base.name = "Kev"
        cls.base.num = 20
        if getenv("HBNB_TYPE_STORAGE") == "db":
            cls.db = MySQLdb.connect(getenv("HBNB_MYSQL_HOST"),
                                     getenv("HBNB_MYSQL_USER"),
                                     getenv("HBNB_MYSQL_PWD"),
                                     getenv("HBNB_MYSQL_DB"))
            cls.cursor = cls.db.cursor()

    @classmethod
    def tearDown(cls):
        """Tear down at the end of the test."""
        del cls.base
        if getenv("HBNB_TYPE_STORAGE") == "db":
            cls.db.close()

    def tearDown(self):
        """Tear down."""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """Test for PEP8 style."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "Fix PEP8")

    def test_checking_for_docstring_BaseModel(self):
        """Test if docstrings are present."""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """Test if BaseModel has methods."""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "delete"))

    def test_init_BaseModel(self):
        """Test if the base is an instance of BaseModel."""
        self.assertTrue(isinstance(self.base, BaseModel))

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', "Can't run if storage is set to file")
    def test_save_BaseModel(self):
        """Test if the save method works."""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_BaseModel(self):
        """Test if the to_dict method works."""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'file', "Can't run if storage is set to file")
    def test_attributes_v2_BaseModel(self):
        """Test the attributes from the v2."""
        attributes = storage.attributes()["BaseModel"]
        o = BaseModel()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'file', "Can't run if storage is set to file")
    def test_to_dict_v2_BaseModel(self):
        """Test the to_dict() method v2."""
        base_dict = self.base.to_dict()
        self.assertFalse('_sa_instance_state' in base_dict.keys())

if __name__ == "__main__":
    unittest.main()
