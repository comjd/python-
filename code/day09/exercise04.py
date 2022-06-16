"""
    for item in MyRange(5) #0 1 2 3 4
"""


class MyRange:
    def __init__(self, stop_number=0):
        self.__stop_number = stop_number

    def __iter__(self):
        number = 0
        while self.__stop_number > number:
            yield number
            number += 1


for item in MyRange(5):
    print(item)
