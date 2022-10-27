#!/usr/bin/env python3
"""
    Airbnb module
"""
import cmd


class Console(cmd.Cmd):
    """
        Console v1.0
        This script inherits the cmd class with all its attributes and methods
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """ Closes the console """
        print()
        return True

    def emptyline(self):
        """ ensures last nonempty command is not called """
        return False

    def do_EOF(self, line):
        """ Quits the console """
        return True


if __name__ == "__main__":
    Console().cmdloop()
