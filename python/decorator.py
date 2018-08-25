#!/usr/bin/python

def time_decorator(orig_function):
    print "> start: time_decorator"
    def wrapper():
        print ">> start: wrapper"
        result = orig_function()
        print ">> end: wrapper"
    print "> end: time_decorator"
    return wrapper


print "start: Decorating display function"
@time_decorator
def display():
    print ">>> This is a simple display function"
print "end: Decorating display function"


display()
