#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from datetime import datetime
import inspect
import models
from models.base_model import BaseModel
import pep8
import unittest
# User = user.User


class test_User(test_basemodel):
    """test user """

    def __init__(self, *args, **kwargs):
        """init instances tests """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value(first_name="a", last_name="po",
                         email="r", password="re")
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value(first_name="a", last_name="po",
                         email="r", password="re")
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value(first_name="a", last_name="po",
                         email="r", password="re")
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value(first_name="a", last_name="po",
                         email="r", password="re")
        self.assertEqual(type(new.password), str)


class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of User class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_conformance_user(self):
        """Test that models/user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

#    def test_pep8_conformance_test_user(self):
#        """Test that tests/test_models/test_user.py conforms to PEP8."""
#        pep8s = pep8.StyleGuide(quiet=True)
#        result = pep8s.check_files(['tests/test_models/test_user.py'])
#        self.assertEqual(result.total_errors, 0,
#                         "Found code style errors (and warnings).")

#     def test_user_module_docstring(self):
#         """Test for the user.py module docstring"""
#         self.assertIsNot(user.__doc__, None,
#                          "user.py needs a docstring")
#         self.assertTrue(len(user.__doc__) >= 1,
#                         "user.py needs a docstring")

#     def test_user_class_docstring(self):
#         """Test for the City class docstring"""
#         self.assertIsNot(User.__doc__, None,
#                          "User class needs a docstring")
#         self.assertTrue(len(User.__doc__) >= 1,
#                         "User class needs a docstring")

#     def test_user_func_docstrings(self):
#         """Test for the presence of docstrings in User methods"""
#         for func in self.user_f:
#             self.assertIsNot(func[1].__doc__, None,
#                              "{:s} method needs a docstring".format(func[0]))
#             self.assertTrue(len(func[1].__doc__) >= 1,
#                             "{:s} method needs a docstring".format(func[0]))


# class TestUser(unittest.TestCase):
#     """Test the User class"""

#     def test_is_subclass(self):
#         """Test that User is a subclass of BaseModel"""
#         user = User()
#         self.assertIsInstance(user, BaseModel)
#         self.assertTrue(hasattr(user, "id"))
#         self.assertTrue(hasattr(user, "created_at"))
#         self.assertTrue(hasattr(user, "updated_at"))

#     def test_email_attr(self):
#         """Test that User has attr email, and it's an empty string"""
#         user = User()
#         self.assertTrue(hasattr(user, "email"))
#         if models.storage_t == 'db':
#             self.assertEqual(user.email, None)
#         else:
#             self.assertEqual(user.email, "")

#     def test_password_attr(self):
#         """Test that User has attr password, and it's an empty string"""
#         user = User()
#         self.assertTrue(hasattr(user, "password"))
#         if models.storage_t == 'db':
#             self.assertEqual(user.password, None)
#         else:
#             self.assertEqual(user.password, "")

#     def test_first_name_attr(self):
#         """Test that User has attr first_name, and it's an empty string"""
#         user = User()
#         self.assertTrue(hasattr(user, "first_name"))
#         if models.storage_t == 'db':
#             self.assertEqual(user.first_name, None)
#         else:
#             self.assertEqual(user.first_name, "")

#     def test_last_name_attr(self):
#         """Test that User has attr last_name, and it's an empty string"""
#         user = User()
#         self.assertTrue(hasattr(user, "last_name"))
#         if models.storage_t == 'db':
#             self.assertEqual(user.last_name, None)
#         else:
#             self.assertEqual(user.last_name, "")

#     def test_to_dict_creates_dict(self):
#         """test to_dict method creates a dictionary with proper attrs"""
#         u = User()
#         new_d = u.to_dict()
#         self.assertEqual(type(new_d), dict)
#         self.assertFalse("_sa_instance_state" in new_d)
#         for attr in u.__dict__:
#             if attr is not "_sa_instance_state":
#                 self.assertTrue(attr in new_d)
#         self.assertTrue("__class__" in new_d)

#     def test_str(self):
#         """test that the str method has the correct output"""
#         user = User()
#         string = "[User] ({}) {}".format(user.id, user.__dict__)
#         self.assertEqual(string, str(user))
