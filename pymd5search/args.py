"""
pygitscrum argparse gestion
"""

import argparse
import sys


def compute_args():
    """
    check args and return them
    """
    my_parser = argparse.ArgumentParser(
        description="pymd5search loops and tries to find a string which equals to itself when encoded with the md5 hash function",
        epilog="""
        Full documentation at: <https://github.com/thib1984/pymd5search>.
        Report bugs to <https://github.com/thib1984/pymd5search/issues>.
        MIT Licence.
        Copyright (c) 2021 thib1984.
        This is free software: you are free to change and redistribute it.
        There is NO WARRANTY, to the extent permitted by law.
        Written by thib1984.""",
    )
    my_parser.add_argument(
        "-u",
        "--update",
        action="store_true",
        help="update pymd5search",
    )       
    args = my_parser.parse_args()
    return args
