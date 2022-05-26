import unittest
from api import create_app, db
from config import TestConfig


class ApiBaseTestCase(unittest.TestCase):
    """base TestCase"""

    def setUp(self) -> None:
        """function to set up app context and test db"""
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()  # push app to app_context
        db.create_all()


    def tearDown(self) -> None:
        """function to remove app context and delete test db"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
