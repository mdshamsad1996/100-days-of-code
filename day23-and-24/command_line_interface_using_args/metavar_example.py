import argparse

my_parser = argparse.ArgumentParser()

my_parser.add_argument(
    '-v',
    '--verbosity',
    action='store',
    type=int,
    metavar='LEVEL'
)

args = my_parser.parse_args()

print(vars(args))

"""
$ python metavar_example.py -h
usage: metavar_example.py [-h] [-v LEVEL]

optional arguments:
  -h, --help            show this help message and exit
  -v LEVEL, --verbosity LEVEL
"""