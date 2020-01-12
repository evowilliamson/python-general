def foo():
    """ Python performs a lexical scan on the function and if it sees a yield, it 
    tags the functions as a generator and generates according code for it
    """

    print("begin")
    for i in range(3):
        print("before yield", i)
        if 1 == 1:
            yield i
        print("after yield", i)
    print("end")

def foo2():
    """ But what happens if more yields are there with different structure? """
    print("begin")
    for i in range(3):
        print("before yield", i)
        if i == 1:
            yield i
        elif i == 2:
            yield i, i
        else:
            yield i, i, i
        print("after yield", i)

    print("end")

""" Generator is an iterator, but do not worry about the protocol
When the function is called, Python actually scans the source code for the
presence of the yield keyword. If it finds it, it doesn't actually execute the
function but it creates an iterator object and returns i 
"""

f = foo()
print(next(f))
print(next(f))
print(next(f))

g = foo2()
print(next(g))
print(next(g))
print(next(g))


    