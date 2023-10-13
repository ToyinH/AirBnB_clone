#!/usr/bin/python3
"""
This is the command line interpreter using the cmd class
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand inheriting from cmd.Cmd
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(self):
        """
        method to handle the help message for quit"""
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """
        EOF command
        """
        print()
        return True

    def help_EOF(self):
        """
        help message for EOF
        """
        print("EOF command\n")

    def emptyline(self):
        """
        method to handle the empty line
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()