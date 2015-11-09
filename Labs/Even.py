def even(f):
    def odd(x):
        if x < 0:
            return f(-x)
        return f(x)
    return odd
def identity(x):
    return x

triangle = even(identity)