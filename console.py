#!/usr/bin/python3
"""Program that contains the entry point of the command interpreter
"""
import cmd
import json
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter"""

    prompt = "(hbnb) "
    class_dic = [
            "BaseModel",
            "User",
            "City",
            "State",
            "Amenity",
            "Review"
    ]

    def emptyline(self):
        """Doesn't do anything on ENTER
        """
        pass

    def do_quit(self, line):
        """Exits the program
        """
        return True

    def do_EOF(self, line):
        """Handles the end of file
        """
        print()
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to the JSON file
        """
        
        if arg == "":
            print("** class name missing **")
        elif arg not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance 
        based on the class name and id"""
        args = arg.split()

        if args == "":
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id is missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
        save the change into the JSON file
        """
        args = arg.split()

        if args == "":
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")           
        else:
            object_id = args[1]
            objects = storage.all()

            key = "{}.{}".format(args[0], object_id)
            if key not in objects:
                print("** no instance found **")
            else:
                del objects[key]
                storage.save()

    def do_all(self, arg):
        """Prints string representation of sll instances or 
        based on class name"""
        args = arg.split()
        objects = storage.all()
        
        if not args:
            print([str(objects[obj]) for obj in objects])
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            objects_filtered =[str(obj) for obj in objects.values() if obj.__class__.__name__ == class_name]
            if not objects_filtered:
                print("** no instance found **")
            else:
                print(objects_filtered)
    
    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save changes into the JSON file)
        """
        args = arg.split()
        objects = storage.all()

        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                obj = objects[key]
                setattr(obj, args[2], args[3].strip('"'))
                obj.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
