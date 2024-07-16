#!/usr/bin/env python3
import sys
from cmd import Cmd
""" Class Console """


class Console(Cmd):
    """ Console inherits from the cmd class
        this console serves as a means of interaction to this project
        commands used in this console are:
    """
    prompt = 'hbnb $ '

    def do_greet(self, line):
        print('hello {}'.format(line))

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    Console().cmdloop()
