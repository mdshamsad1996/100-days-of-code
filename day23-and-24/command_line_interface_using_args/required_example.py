import argparse

my_parser = argparse.ArgumentParser()

my_parser.add_argument('-a', action='store',choices=['head', 'tail'], required=True)

args = my_parser.parse_args()

print(vars(args))

"""
$ python required_example.py
usage: required_example.py [-h] -a {head,tail}
required_example.py: error: the following arguments are required: -a

$ python required_example.py -a head
{'a': 'head'}

"""