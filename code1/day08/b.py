int('f2:', b)


def f3(d):
    print('f3:', d)


func_list = [f1, f2, f3]
p_list = []

for f in func_list:
    p = Process(target=f, args=(1,))
    p_list.append(p)
    p.start()

for a in p_list:
    a.join()
