import argparse

my_parser = argparse.ArgumentParser()

my_parser.add_argument('-a', action='store', choices=['head', 'tail'])

args = my_parser.parse_args()

print(vars(args))

"""
$ python choice_ex.py -a 'head'
{'a': 'head'}

$ python choice_ex.py -a 78
usage: choice_ex.py [-h] [-a {head,tail}]
choice_ex.py: error: argument -a: invalid choice: '78' (choose from 'head', 'tail')
"""