#!/usr/bin/python3
""" MY Int """


class MyInt(int):
    """ My Rebel Int """
    def __eq__(self, __value: object) -> bool:
        return super().__ne__(__value)

    def __ne__(self, __value: object) -> bool:
        return super().__eq__(__value)
