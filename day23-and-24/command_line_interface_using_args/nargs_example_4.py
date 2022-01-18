import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument(
    'first',
    action='store'
)

my_parser.add_argument(
    'others',
    action='store',
    nargs=argparse.REMAINDER
)

args = my_parser.parse_args()

print('first = %r' % args.first)
print('others= %r' % args.others)

"""
$ python nargs_example_4.py me you us
first = 'me'
others= ['you', 'us']

"""
