def first(x):
    x += 8
    def second(y):
        print('second')
        return x + y
    print('first')
    return second