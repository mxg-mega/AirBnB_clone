#!/usr/bin/python3
""" The HBNBCommand """

from models.engine.file_storage import classes
import models
import sys
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

    def precmd(self, line):
        """ Custom commands with different syntax
            Custom Command formats:
                retrieve all instances of a class by using:
                    <class name>.all().
        """
        try:
            if '.' in line and '(' in line:
                cls, method = line.split('.')
                method, args = method.split('(')
                args = args.replace(')', '')
                if ',' in args and method == 'update':
                    splitted = args.split(',', 1)
                    if '{' in splitted[1] and '}' in splitted[1]:
                        id_str, dict_repr = splitted[0], splitted[1]
                        line = "{} {} {} {}".format(method, cls,
                                                     id_str, dict_repr)
                    else:
                        line = "{} {} ".format(method, cls)
                        for arg in args.split(','):
                            line += arg + ' '
                        print("line : {}".format(line))
                else:
                    line = "{} {} {}".format(method, cls, args)
        except Exception as e:
            pass
        return line

    def do_count(self, class_name):
        if class_name is not None and class_name != '':
            class_name = class_name.split()[0]
            models.storage.reload()
            objs = models.storage.all()
            count = 0
            if self.isClassAvailable(class_name):
                for i in objs.values():
                    if i.to_dict()['__class__'] == class_name:
                        count += 1
                print(count)
            else:
                print("** class doesn't exist **")
        

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
        else:
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
        args = args.split()
        if self.arg_checks(args):
            class_name = args[0]
            instance_id = args[1]
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
        args = args.split()
        if self.arg_checks(args):
            class_name = args[0]
            instance_id = args[1]
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
        class_type = classTypes.split()[0]
        models.storage.reload()
        objs = models.storage.all()
        if classTypes is None or classTypes == '':
            print([objs[key].__str__() for key in objs.keys()])
        else:
            if not self.isClassAvailable(classTypes):
                print("** class doesn't exist **")
            else:
                print([objs[key].__str__() for key in objs.keys()
                      if key.split(".")[0] == class_type])

    def do_update(self, args):
        """ update: Updates an instance based on the class name
            and id by adding or updating attribute
            (save the change into the JSON file).
            Ex: $ update BaseModel 1234-1234-1234 email "airbnb@mail.com"

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if '{' in args and '}' in args:
            args = args.split(' ', 2)
        else:
            args = args.split()

        if self.arg_checks(args):
            if len(args) == 3 and '{' in args[2] and '}' in args[2]:
                try:
                    dict_repr = eval(args[2])
                    for key, value in dict_repr.items():
                        self.updating(args[0], args[1],
                                      key, value)
                except Exception as e:
                    print("** Invalid Dictionary **")
                    return
            elif len(args) < 3:
                print("** attribute name missing **")
                return
            elif len(args) < 4:
                print("** value missing **")
                return
            else:
                self.updating(args[0], args[1],
                              args[2], args[3])

    def updating(self, c_name, inst_id, attr_name, attr_value):
        class_name = c_name
        instance_id = inst_id
        models.storage.reload()
        objs = models.storage.all()
        key_format = "{}.{}".format(class_name, instance_id)
        if key_format not in objs.keys():
            print("** no instance found **")
        else:
            setattr(objs[key_format], attr_name, attr_value)
            models.storage.save()

    def arg_checks(self, args):
        if args is None or args == '':
            print("** class name missing **")
            return False
        else:
            if not self.isClassAvailable(args[0]):
                print("** class doesn't exist **")
                return False
            elif len(args) < 2:
                print("** instance id missing **")
                return False
        return True

    def isClassAvailable(self, class_name):
        if class_name in classes:
            return True
        return False


if __name__ == '__main__':
    if len(sys.argv) > 1:
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
