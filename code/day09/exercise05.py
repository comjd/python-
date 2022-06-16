"""
    for item in MyRange(5) #0 1 2 3 4
"""


def myrange(stop_number):
    number = 0
    while stop_number > number:
        yield number
        number += 1


for item in myrange(5):
    print(item)
