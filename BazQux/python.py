def func(x):
    if x % 15 == 0:
        return 'BazQux'
    if x % 3 == 0:
        return 'Baz'
    if x % 5 == 0:
        return 'Qux'
    return str(x)
one = [i for i in range(1, 101)]
s = ' '.join(map(lambda tmp: str(tmp), one))
t = ' '.join(map(func, one))
print(s)
print(t)
