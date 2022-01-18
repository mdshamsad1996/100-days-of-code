import argparse

my_parser = argparse.ArgumentParser()

my_parser.add_argument(
    '-a',
    action='store',
    choices=['head', 'tail'],
    help='set the user choice to head or tail'
)

args = my_parser.parse_args()

print(vars(args))

"""
$ python help_example.py -h
usage: help_example.py [-h] [-a {head,tail}]

optional arguments:
  -h, --help      show this help message and exit
  -a {head,tail}  set the user choice to head or tail

"""