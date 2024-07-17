#!/usr/bin/env python3
import sys
from cmd import Cmd
""" Class Console """


class Console(Cmd):
    """ Console inherits from the cmd class
        this console serves as a means of interaction to this project
        commands used in this console are:
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Syntax to Quit Interpreter
            usage:
                quit
        """
        return True

    def do_EOF(self, line):
        """ A shortcut for exiting the Interpreter """
        return True


if __name__ == '__main__':
    Console().cmdloop()
