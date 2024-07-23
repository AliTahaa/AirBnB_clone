#!/usr/bin/python3
"""Test FileStorage class"""


import unittest
import json
import os
import shutil
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """testing file storage"""
    @classmethod
    def setUpClass(cls):
        """ method class setup"""
        cls.aux1.place_id = "testing"
        cls.aux1.user_id = "idUSER"
        cls.aux1.text = "text1"

    @classmethod
    def teardown(cls):
        """ method class tear"""
        del cls.aux1

    def teardown(self):
        """ method tear"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_all(self):
        """ Tests method:all"""
        storage = FileStorage()
        instances_dic = storage.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, storage._FileStorage__objects)

    def test_new(self):
        """ Tests method: new (saves new object into dictionary)"""
        m_storage = FileStorage()
        instances_dic = m_storage.all()
        user1 = User()
        user1.id = 555555
        user1.name = "ali"
        m_storage.new(user1)
        key = user1.__class__.__name__ + "." + str(user1.id)
        self.assertIsNotNone(instances_dic[key])

    def test_reload_empty(self):
        """ Tests method: reload (reloads objects from string file)"""
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except Exception:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)
