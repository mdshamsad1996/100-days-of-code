import argparse

my_parser = argparse.ArgumentParser()

my_parser.add_argument(
    'input',
    action='store',
    nargs='*',
    default='my default values'
)

args = my_parser.parse_args()

print(args.input)

"""
$ python nargs_example_2.py me us ehsc
['me', 'us', 'ehsc']

$ python nargs_example_2.py
my default values
"""