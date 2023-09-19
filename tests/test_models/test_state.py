#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest
import MySQLdb

class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
class TestCreateStateCommand(unittest.TestCase):
    def setUp(self):
        # Connect to your database and create a cursor
        self.db = MySQLdb.connect(
            host='localhost',
            user='hbnb_test',
            passwd='hbnb_test_pwd',
            db='hbnb_test_db'
        )
        self.cursor = self.db.cursor()

    def tearDown(self):
        # Close the database connection
        self.db.close()

    def test_create_state_command(self):
        # Step 1: Get the initial number of records
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        # Step 2: Execute the console command
        # Replace this with the actual console command execution code

        # Step 3: Get the number of records again
        self.cursor.execute("SELECT COUNT(*) FROM states")
        final_count = self.cursor.fetchone()[0]

        # Step 4: Assertion
        self.assertEqual(final_count - initial_count, 1)

if __name__ == '__main__':
    unittest.main()
