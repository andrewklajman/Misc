import timeit
print('ListTest')
print(timeit.timeit('''
NUM = 20

def gentest():
    for c1 in range(NUM):
        for c2 in range(NUM):
            for c3 in range(NUM):
                yield (c1, c2, c3)

def listtest():
    tmp = []
    for c1 in range(NUM):
        for c2 in range(NUM):
            for c3 in range(NUM):
                tmp.append((c1, c2, c3))
    return tmp

lists = listtest()

''', number = 5000))
            
print('GenTest')
print(timeit.timeit('''
NUM = 20

def gentest():
    for c1 in range(NUM):
        for c2 in range(NUM):
            for c3 in range(NUM):
                yield (c1, c2, c3)

def listtest():
    tmp = []
    for c1 in range(NUM):
        for c2 in range(NUM):
            for c3 in range(NUM):
                tmp.append((c1, c2, c3))
    return tmp

lists = gentest()

''', number = 5000))
            
        
