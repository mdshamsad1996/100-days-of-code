import argparse
from ast import Store

# my_parser = argparse.ArgumentParser()
my_parser = argparse.ArgumentParser(allow_abbrev=False)
my_parser.add_argument('--input', action='store', type=int, required=True)
my_parser.add_argument('--id', action='store', type=int)

args = my_parser.parse_args()

print(args.input)