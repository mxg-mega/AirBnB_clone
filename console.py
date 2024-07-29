#!/usr/bin/python3
from models.engine.file_storage import classes
import models
import cmd
""" HBNBCommand Class """


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
