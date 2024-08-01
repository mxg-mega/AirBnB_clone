import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestConsole(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        models.storage.all().clear()

    def tearDown(self):
        """Tear down the test environment"""
        models.storage.all().clear()

    def get_output(self, command):
        """Capture the output of a console command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(command)
            return f.getvalue().strip()

class TestConsoleCommands(TestConsole):
    def test_create(self):
        """Test the create command"""
        output = self.get_output("create BaseModel")
        self.assertTrue(len(output) > 0)
        instance_id = output
        self.assertIn("BaseModel.{}".format(instance_id), models.storage.all())

        output = self.get_output("create User")
        self.assertTrue(len(output) > 0)
        instance_id = output
        self.assertIn("User.{}".format(instance_id), models.storage.all())

        output = self.get_output("create NonExistentClass")
        self.assertEqual(output, "** class doesn't exist **")

    def test_show(self):
        """Test the show command"""
        instance = BaseModel()
        instance.save()
        instance_id = instance.id
        output = self.get_output("show BaseModel {}".format(instance_id))
        self.assertIn("[BaseModel] ({})".format(instance_id), output)

        output = self.get_output("show BaseModel 1234-5678")
        self.assertEqual(output, "** no instance found **")

        output = self.get_output("show NonExistentClass {}".format(instance_id))
        self.assertEqual(output, "** class doesn't exist **")

    def test_destroy(self):
        """Test the destroy command"""
        instance = BaseModel()
        instance.save()
        instance_id = instance.id
        output = self.get_output("destroy BaseModel {}".format(instance_id))
        self.assertEqual(output, "")
        self.assertNotIn("BaseModel.{}".format(instance_id), models.storage.all())

        output = self.get_output("destroy BaseModel 1234-5678")
        self.assertEqual(output, "** no instance found **")

        output = self.get_output("destroy NonExistentClass {}".format(instance_id))
        self.assertEqual(output, "** class doesn't exist **")

    def test_all(self):
        """Test the all command"""
        output = self.get_output("all")
        self.assertEqual(output, "[]")

        instance = BaseModel()
        instance.save()
        instance_id = instance.id
        output = self.get_output("all BaseModel")
        self.assertIn("[BaseModel] ({})".format(instance_id), output)

        output = self.get_output("all NonExistentClass")
        self.assertEqual(output, "** class doesn't exist **")

    def test_update(self):
        """Test the update command"""
        instance = BaseModel()
        instance.save()
        instance_id = instance.id
        output = self.get_output("update BaseModel {} name 'Test'".format(instance_id))
        self.assertEqual(output, "")
        self.assertEqual(models.storage.all()["BaseModel.{}".format(instance_id)].name, "Test")

        output = self.get_output("update BaseModel {} name".format(instance_id))
        self.assertEqual(output, "** value missing **")

        output = self.get_output("update BaseModel 1234-5678 name 'Test'")
        self.assertEqual(output, "** no instance found **")

        output = self.get_output("update NonExistentClass {} name 'Test'".format(instance_id))
        self.assertEqual(output, "** class doesn't exist **")

        # Testing dictionary update
        output = self.get_output("update BaseModel {} {{'name': 'NewName', 'number': 89}}".format(instance_id))
        self.assertEqual(output, "")
        self.assertEqual(models.storage.all()["BaseModel.{}".format(instance_id)].name, "NewName")
        self.assertEqual(models.storage.all()["BaseModel.{}".format(instance_id)].number, 89)


if __name__ == "__main__":
    unittest.main()
