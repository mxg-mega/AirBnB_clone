#!/usr/bin/python3
""" The HBNBCommand """

from models.engine.file_storage import classes
import models
import cmd


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand inherits from the cmd class
        this console serves as a means of interaction to this project
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Syntax to Quit Interpreter
            usage:
                quit
        """
        return True

    def emptyline(self):
        """ An Emptyline Does Nothing """
        pass

    def do_EOF(self, line):
        """ A shortcut for exiting the Interpreter """
        return True

    def do_create(self, class_name=None):
        """ create command creates a new instance of a class
            specified as the argument of this command, save and print
            its id,
            in case of unavailable or missing class name
            an error is printed

            Usage:
                create <class_name>
        """
        if class_name is None or class_name == '':
            print("** class name missing **")
        if self.isClassAvailable(class_name):
            new_instance = classes[class_name]()
            new_instance.save()
            print("{}".format(new_instance.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, args=None):
        """ show: Prints the string representation of
            an instance based on the class name and id.
            Ex: $ show BaseModel 1234-1234-1234
        """
        if self.arg_checks(args):
            class_name = args.split()[0]
            instance_id = args.split()[1]
            models.storage.reload()
            objs = models.storage.all()
            key_format = "{}.{}".format(class_name, instance_id)
            if key_format not in objs.keys():
                print("** no instance found **")
            else:
                print(objs[key_format])

    def do_destroy(self, args=None):
        """ destroy: Deletes an instance based on
        the class name and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        if self.arg_checks(args):
            class_name = args.split()[0]
            instance_id = args.split()[1]
            models.storage.reload()
            objs = models.storage.all()
            key_format = "{}.{}".format(class_name, instance_id)
            if key_format not in objs.keys():
                print("** no instance found **")
            else:
                del objs[key_format]
                models.storage.save()

    def do_all(self, classTypes=None):
        """ all: Prints all string representation of all
            instances based or not on the class name.
            Ex: $ all BaseModel or $ all
        """
        models.storage.reload()
        objs = models.storage.all()
        if classTypes is None or classTypes == '':
            print([objs[key].__str__() for key in objs.keys()])
        else:
            if not self.isClassAvailable(classTypes):
                print("** class doesn't exist **")
            else:
                print([objs[key].__str__() for key in objs.keys()
                      if key.split(".")[0] == classTypes])

    def do_update(self, args):
        """ update: Updates an instance based on the class name
            and id by adding or updating attribute
            (save the change into the JSON file).
            Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if self.arg_checks(args):
            if len(args.split()) < 3:
                print("** attribute name missing **")
            elif len(args.split()) < 4:
                print("** value missing **")
            else:
                class_name = args.split()[0]
                instance_id = args.split()[1]
                models.storage.reload()
                objs = models.storage.all()
                key_format = "{}.{}".format(class_name, instance_id)
                if key_format not in objs.keys():
                    print("** no instance found **")
                else:
                    setattr(objs[key_format], args.split()[2], args.split()[3])
                    models.storage.save()

    def arg_checks(self, args):
        if args is None or args == '':
            print("** class name missing **")
            return False
        else:
            if not self.isClassAvailable(args.split()[0]):
                print("** class doesn't exist **")
                return False
            elif len(args.split()) < 2:
                print("** instance id missing **")
                return False
        return True

    def isClassAvailable(self, class_name):
        if class_name in classes:
            return True
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
