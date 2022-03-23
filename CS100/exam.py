def foo(x, y):
    x  = x + 1
    print("#1:",x, y)
    return x - y
def bar(x, y):
    print ("#2:", x, y)
    return x*y
x = 5
y = 4
print ("#3:", x, y)
x = bar(x, y)
print ("#4:", x, y)
y = foo(x, y)
print ("#5:", x, y)

