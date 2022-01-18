import argparse

my_parser = argparse.ArgumentParser()

my_group = my_parser.add_mutually_exclusive_group(required=True)

my_group.add_argument('-v', '--verbose', action='store_true')
my_group.add_argument('-s', '--silent', action='store_true')

args = my_parser.parse_args()

print(vars(args))

"""
$ python groups.py -h
usage: groups.py [-h] (-v | -s)

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose
  -s, --silent

$ python groups.py -v -s
usage: groups.py [-h] (-v | -s)
groups.py: error: argument -s/--silent: not allowed with argument -v/--verbose

"""