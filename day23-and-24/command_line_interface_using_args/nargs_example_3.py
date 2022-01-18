import argparse

my_parse = argparse.ArgumentParser()

my_parse.add_argument('input', action='store', nargs='+')

args = my_parse.parse_args()

print(args.input)

"""
$ python nargs_example_3.py me you us
['me', 'you', 'us']
$ python nargs_example_3.py 45
['45']
$ python nargs_example_3.py
usage: nargs_example_3.py [-h] input [input ...]
nargs_example_3.py: error: the following arguments are required: input

"""