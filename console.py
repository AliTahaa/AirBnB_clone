#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):

  prompt = "(hbnb) "
  def do_quit(self, line):
     '''Quit command to exit the program'''
     return 1
  def do_EOF(self, line):
     '''EOF (end-of-file) command to exit the program'''
     return 1
  def emptyline(self):
     return super().emptyline()
  def do_hi(self, line):
     '''asassa'''
     print("noo", line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
