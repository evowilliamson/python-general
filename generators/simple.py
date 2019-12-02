def foo():
    print("begin")
    for i in range(3):
        print("before yield", i)
        if 1 == 1:
            yield i
        print("after yield", i)
    print("end")

""" Generator is an iterator, but do not worry about the protocol
When the function is called, Python actually scans the source code for the
presence of the yield keyword. If it finds it, it doesn't actually execute the
function but it creates an iterator object and returns i 
"""

f = foo()
next(f)
next(f)
next(f)

    