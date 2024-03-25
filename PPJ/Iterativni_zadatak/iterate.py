def iterate(s):
    if is_done(s):
        return s
    else:
        s1 = transform(s)
        return iterate(s1)

def is_done(s):
    return s >= b

def transform(s):
    print(s)
    return s + 4

a, b = map(int, input().split())

iterate(a)