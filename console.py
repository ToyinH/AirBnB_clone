#!/usr/bin/python3
"""
This is the command line interpreter using the cmd class
"""
import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, arg):
        """
        Create a new instance of BaseModel
        """
        if arg:
            try:
                class_name = arg.split()[0]
                BaseModel_instance = eval(class_name)()
                BaseModel_instance.save()
                print(BaseModel_instance.id)
            except:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_create(self):
        """
        Create a new instance of BaseModel
        """
        print("Create a new instance of BaseModel\n")

    def do_show(self, arg):
        """method that prints the string representation of
        an instance based on the class name and id"""

        word_list = arg.split()
        if len(word_list) < 1:
            print("** class name missing **")
        else:
            class_name = word_list[0]
            try:
                if len(word_list) < 2:
                    print("** instance id missing **")
                else:
                    instance_id = word_list[1]
                    key = f"{class_name}.{instance_id}"
                    if key in storage.all():
                        instance = storage.all()[key]
                        print(instance)
                    else:
                        print("** no instance found **")
            except:
                print("** class doesn't exist **")

    def help_show(self):
        """
        method that prints the string representation of
        an instance based on the class name and id
        """
        print(
            "prints the string representation of an instance based on the class name and id\n"
            )

    def do_all(self, arg):
        """method to print all string representation of all instances
        based or not on the class"""

        all_obj = storage.all()

        try:
            if arg:
                args = arg.split()
                class_name_list = []
                for key in all_obj.keys():
                    class_name = key.split(".")[0]
                    class_name_list.append(class_name)
                    if class_name == args[0]:
                        print(all_obj[key])
                if args[0] not in class_name_list:
                    print("** class doesn't exist **")
            else:
                for key in all_obj.keys():
                    print(all_obj[key])
        except:
            print("** class doesn't exist **")

    def help_all(self):
        """method to print to all representation of instances
        base or not on class"""
        print("print all string representation of all instances base or not on class\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
