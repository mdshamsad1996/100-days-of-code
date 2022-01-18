import argparse

my_parse = argparse.ArgumentParser()
my_parse.add_argument('-a', action='store', type=int)

args = my_parse.parse_args()

print(vars(args))

"""
$ python type_example.py -a 45
{'a': 45}

$ python type_example.py -a "That's a string"
usage: type_example.py [-h] [-a A]
type_example.py: error: argument -a: invalid int value: "That's a string"


"""