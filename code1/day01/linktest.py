def test1():
    count = 0
    while count < 100:
        yield count
        count += 1


for i in test1():
    print(i)
