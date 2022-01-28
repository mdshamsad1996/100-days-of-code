import argparse
import pathlib
import sys

from . import __version__
from .rptree import DirectoryTree

def parse_cmd_line_arguments():
    
    """parse command line argument"""
    
    parser = argparse.ArgumentParser(
        prog="tree",
        description="RP tree, a directory tree generator",
        epilog="Thanks for using RP Tree!"
    )
    parser.version = f"RP Tree v{__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        nargs="?",
        default=".",
        help="Generate a full directory tree starting the root directory"
    )
    parser.add_argument(
        "-d",
        "--dir-only",
        action="store_true",
        help="Generate a irectory-tree only"
    )  
    parser.add_argument(
        "-o",
        "--output-file",
        metavar="OUTPUT_FILE",
        nargs="?",
        default=sys.stdout,
        help="Generate a full directory tree and save it to a file"
    )
    return parser.parse_args()


def main():
    """main function"""
    args = parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("The specified root directory does not exist")
        sys.exit()
    tree = DirectoryTree(root_dir, dir_only=args.dir_only, output_file=args.output_file)
    tree.generator()
        