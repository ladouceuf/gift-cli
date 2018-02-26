"""
gift

Usage:
  gift register (--add_name | --remove_name)
  gift login (--admin | --user)
  gift guest_list
  gift reset
  gift (-h | --help | --version)

Options:
  --add_name			    Add a name to the guest list.
  --remove_name			    Remove a name from the guest list.
  --admin			    Login as admin.
  --user			    Login as user.
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  gift register --add_name
  gift register --remove_name
  gift login --admin
  gift login --user
  gift guest_list
  gift reset
  gift -h
  gift --help
  gift --version
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    import gift.commands
    options = docopt(__doc__, version=VERSION)

    for (k, v) in options.items(): 
        if hasattr(gift.commands, k) and v:
            module = getattr(gift.commands, k)
            gift.commands = getmembers(module, isclass)
            command = [command[1] for command in gift.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()