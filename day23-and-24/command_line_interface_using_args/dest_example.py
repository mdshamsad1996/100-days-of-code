import argparse

my_parser = argparse.ArgumentParser()

my_parser.add_argument(
    '-v',
    '--verbosity',
    action='store',
    type= int,
    dest='my_verbosity_level'
)

args = my_parser.parse_args()

print(vars(args))

"""
$ python dest_example.py -v 656
{'my_verbosity_level': 656}

"""