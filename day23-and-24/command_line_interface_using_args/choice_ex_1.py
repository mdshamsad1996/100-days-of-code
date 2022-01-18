import argparse

my_parse = argparse.ArgumentParser()

my_parse.add_argument('-a', action='store', type=int, choices=range(1, 5))

args = my_parse.parse_args()

print(vars(args))

"""
$ python choice_ex_1.py -a 4
{'a': 4}

$ python choice_ex_1.py -a 5
usage: choice_ex_1.py [-h] [-a {1,2,3,4}]
choice_ex_1.py: error: argument -a: invalid choice: 5 (choose from 1, 2, 3, 4)

"""