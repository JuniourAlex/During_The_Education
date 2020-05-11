def sum (a, b):
    while True:
        try:
            return a + b
        except TypeError:
            print ('Enter a number')
            continue

def num (a, b):
    return a - b

def dev(a, b):
    return a/b