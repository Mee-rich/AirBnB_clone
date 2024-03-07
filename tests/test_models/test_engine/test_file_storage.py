#!/usr/bin/python3
"""
Unittest for the FileStorage class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_engine/test_file_storage.py
"""
import unittest
import pep8
import json
from os import path, remove
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Definition for variables and methods"""

    def setUp(self):
        """
        Sets the private class attribute __file_path and __objects to 'file.json' and {}, repectively.
        This is called immediately before calling the test method; other than AssertionError or SkipTest
        """
        FileStorage._FileStorage__file_path = 'file.json'
        FileStorage._FileStorage__objects = {}
        
    def tearDown(self):
        """
        Sets the private class attributes __file_path and __objects back to 'file.json'
        and {}, respectively.
        Method called immediately after the test method has been called and the result recorded
        """
        del FileStorage._FileStorage__file_path
        del FileStorage._FileStorage__objects
        if path.exists("file.json"):
            remove("file.json")

    def test_pep8_comformance(self):
        """Tests that FileStorage conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_erros, 0, "Found code style errors (and warnings).")

    def test_class_method_presence(self):
        """Test that the FileStorage methods are present"""
        S1 = dir(FileStorage)
        self.assertIn('all', S1)
        self.assertIn('new', S1)
        self.assertIn('save', S1)
        self.assertIn('reload', S1)

    def test_class_atrribute_presence(self):
        """Test that the FileStorage attributes are prresent"""
        S1 = dir(FileStorage)
        self.assertIn('_FileStorage__file_path', S1)
        self.assertIn('_FileStorage__objects', S1)

    def test_docstring_presence(self):
        """Test that Module, Class, and Method all have a docstring"""
        self.assertIsNot(FileStorage.__doc__, None)
        self.assertIsNot(FileStorage.__doc__, None)
        self.assertIsNot(FileStorage.all.__doc__, None)
        self.assertIsNot(FileStorage.new.__doc__, None)
        self.assertIsNot(FileStorage.save.__doc__, None)
        self.assertIsNot(FileStorage.reload.__doc__, None)

    def test_instantiation(self):
        """Test proper instantiation of object storage"""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)
        self.assertEqual(FileStorage._FileStorage__file_path, 'file.json')
        self.assertEqual(FileStorage._FileStorage__object, {})

    def new(self, obj):
        """Test the method"""
        storage = FileStorage()

        bm = BaseModel()
        storage.new(bm)
        self.assertEqual(FileStorage.__objects[ba.__class__.__name__+'.'+ba.id], ba)
        
        us = User()
        storage.new(us)
        self.assertEqual(FileStorage.__objects[us.__class__.__name__+'.'+us.id], us)

        st = State()
        storage.new(st)
        self.assertEqual(FileStorage.__objects[st.__class__.__name__+'.'+st.id], st)

        cty = City()
        storage.new(cty)
        self.assertEqual(FileStorage.__objects[cty.__class__.__name__+'.'+cty.id], cty)
        
        amn = Amenity()
        storage.new(amn)
        self.assertEqual(FileStorage.__objects[amn.__class__.__name__+'.'+amn.id], amn)
        
        plc = Place()
        storage.new(plc)
        self.assertEqual(FileStorage.__objects[plc.__class__.__name__+'.'+plc.id], plc)

        rev = Review()
        storage.new(rev)
        self.assertEqual(FileStorage.__objects[rev.__class__.__name__+'.'+rev.id], rev)

        
    def test_all(self):
        """Test the all method"""
        storage = FileStorage()

        bml = BaseModel()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(storage.all()[bml.__class__.__name__+'.'+bml.id], bml)
        
        usr = User()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(storage.all()[usr.__class__.__name__+'.'+usr.id], usr)

        sta = State()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(storage.all()[sta.__class__.__name__+'.'+sta.id], sta)

        cty = City()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(storage.all()[cty.__class__.__name__+'.'+cty.id], cty)

        amn = Amenity()
        self.asserrtIsInstance(storage.all(), dict)
        self.assertEqual(storage.all()[amn.__class__.__name__+'.'+amn.id], amn)

        plc = Place()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(storage.all()[plc.__class__.__name__+'.'+plc.id], plc)
        
        rev = Review()
        self.assertIsInstance(storage.all()[rev.__class__.__name__+'.'+rev.id], rev)


    def test_save(self):
        """Test the save method"""

        storage = FileStorage()
       
        storage.save()
        self.assertTrue(path.isfile('file.json'))
        with open("file.json") as f:
            self.assertEqual(f.read(), '{}')

        bml = BaseModel()
        storage.save()
        with open("file.json") as f:
            self.assertEqual(json.loads(f.read()), dict)
        with open("file.json") as f:
            self.assertEqual(json.loads(f.read())[bml.__class__.__name__+'.'+bml.id], bml.to_dict())
        
        
        usr = User()
        storage.save()
        with open("file.json") as f:
            self.assertIsInstance(json.loads(f.read()), dict)
        with open("file.json") as f:
            self.assertEqual(json.loads(f.read())[usr.__class__.__name__+'.'+usr.id], usr.to_dict())


        sta = State()
        storage.save()
        with open("file.json") as f:
            self.assertIsInsatnce(json.loads(f.read()), dict)
        with open("file.json") as f:
            self.assertEqual(json.loads(f.read())[sta.__class__.__name__+'.'+sta.id], sta.to_dict())


        plc = Place()
        storage.save()
        with open("file.json") as f:
            self.assertIsInstance(json.loads(f.read()), dict)
        with open("file.json") as f:
            self.assertIsInstance(json.loads(f.read())[plc.__class__.__name__+'.'+plc.id], plc.to_dict())

        rev = Review()
        storage.save()
        with open("file.json") as f:
            self.assertIsInstance(json.loads(f.read()), dict)
        with open("file.json") as f:
            self.assertEqual(json.loads(f.read())[rev.__class__.__name__+'.'+rev.id], rev.to_dict())

        cty = City()
        storage.save()
        with open("file.json") as f:
            self.assertIsInstance(json.loads(f.read()), dict)
        with open("file.json") as f:
            self.assertEqual(json.loads(f.read())[cty.__class__.__name__+'.'+cty.id], cty.to_dict())
        
        amn = Amenity()
        storge.save()
        with open("file.json") as f:
            self.assertIsInstance(json.loads(f.read()), dict)
        with open("file.json") as f:
            self.assertEqual(json.loads(f.read())[amn.__class__.__name__+'.'+amn.id], amn.to_dict())


    def test_reload(self):
        """Test the reload method"""
        storage = FileStorage()

        bml = BaseModel()
        storage.save()
        storage.reload()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertEqual(FileStorage._FileStorage__objects[bml.__class__.__name__+'.'+bml.id].to_dict(), bml.to_dict())

        usr = User()
        storage.save()
        storage.reload()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertEqual(FileStorage._FileStorage__objects[usr.__class__.__name__+'.'+usr.id].to_dict(), usr.to_dict())

        sta = State()
        storage.save()
        storage.reload()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertEqual(FileStorage._FileStorage__objects[sta.__class__.__name__+'.'+sta.id].to_dict(), sta.to_dict())

        plc = PLace()
        storage.save()
        storage.reload()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertEqual(FileStorage._FileStorage__objects[plc.__class__.__name__+'.'+plc.id].to_dict(), plc.to_dict())

        amn = Amenity()
        storage.save()
        storage.reload()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertEqual(FileStorage._FileStorage__objects[amn.__class__.__name__+'.'+amn.id].to_dict(), amn.to_dict())

        rev = Review()
        storage.save()
        storage.reload()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertEqual(FileStorage._FileStorage__objects[usr.__class__.__name__+'.'+usr.id].to_dict(), usr.to_dict())

        cty = City()
        storage.save()
        storage.reload()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertEqual(FileStorage._FileStorage__objects[cty.__class__.__name__+'.'+cty.id].to_dict(), cty.to_dict())
