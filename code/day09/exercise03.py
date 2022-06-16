"""
    for item in MyRange(5) #0 1 2 3 4
"""


class MyRangeIterator:
    def __init__(self, stop_number):
        self.__stop_number = stop_number
        self.__index = -1

    def __next__(self):
        self.__index += 1
        if self.__stop_number <= self.__index:
            raise StopIteration()
        return self.__index


class MyRange:
    def __init__(self, stop_number=0):
        self.__stop_number = stop_number

    def __iter__(self):
        return MyRangeIterator(self.__stop_number)


for item in MyRange(5):
    print(item)
