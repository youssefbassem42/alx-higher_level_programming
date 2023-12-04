#!/usr/bin/python3
""""
List inheritance
"""


class MyList(list):
    """ Sort List"""
    def print_sorted(self):
        """Sort list"""
        print(sorted(self))
