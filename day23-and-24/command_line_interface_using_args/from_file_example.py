# Setting Prefix Chars for Files That Contain Arguments to Be Included

import argparse

my_parse = argparse.ArgumentParser(fromfile_prefix_chars='@')

my_parse.add_argument('a',
                      help='a first argumen')

my_parse.add_argument('b',
                      help='a second argument')

my_parse.add_argument('c',
                      help='a third argument')

my_parse.add_argument('d',
                      help='a fourth argument')

my_parse.add_argument('e',
                      help='a fifth argument')

my_parse.add_argument('-v',
                      '--verbose',
                      action='store_true',
                      help='an optional argument')

# Execute the parse_args()
args = my_parse.parse_args()

print('If you read this line it means that you have provided '
      'all the parameters')

#  python from_file_example.py @args.txt