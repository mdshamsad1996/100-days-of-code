# myls
# Import the argparse library
import argparse

import os
import sys

# 1. Create a parser
# my_parser = argparse.ArgumentParser(description="List the content of Folder")

# --------------------------------------------------------

#1.1 Displaying a Custom Program Usage Help
# my_parser = argparse.ArgumentParser(prog='myls_using_argparse',
#                                     usage='%(prog)s [options] path',
#                                     description="List the content of Folder")

# --------------------------------------------------------

# 1.2 Displaying Text Before and After the Arguments Help
# my_parser = argparse.ArgumentParser(description='List the content of a folder',
#                                    epilog='Enjoy the Program! :)')

# Output
# $ python myls_using_argpars_lib.py -h
# usage: myls_using_argpars_lib.py [-h] path

# List the content of a folder

# positional arguments:
#   path        the path to list

# optional arguments:
#   -h, --help  show this help message and exit

# Enjoy the Program! :)

# --------------------------------------------------------

#  Customizing the Allowed Prefix Chars
my_parser = argparse.ArgumentParser(description='List the content of a folder',
                                   epilog='Enjoy the Program! :)', prefix_chars='/')

# Add the arguments
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to list')

# Execute the parser_args() method
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print("The Path Specified does not exist")
    sys.exit()

print('\n'.join(os.listdir(input_path)))

