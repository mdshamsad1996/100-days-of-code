import argparse
from ast import arg

my_parser = argparse.ArgumentParser()
my_parser.add_argument('input',
                       action='store',
                       nargs='?',
                       default='my default value')

args = my_parser.parse_args()
print(args.input)

"""
$ python nargs_example_1.py 'my custom value'
my custom value

$ python nargs_example_1.py
my default value

"""