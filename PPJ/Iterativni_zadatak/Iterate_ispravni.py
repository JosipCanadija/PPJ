def iterate(s, isDone, transform):
    if isDone(s):
        return s
    else:
        s1 = transform(s)
        return iterate(s1, isDone, transform)

def rangeList(a, b, step):
    result = []
    
    def isDone(x):
        return x > b

    def transform(x):
        result.append(x)
        return x + step

    iterate(a, isDone, transform)
    return result

print(*rangeList(1, 20, 4))  # Vraća 1 5 9 13 17
