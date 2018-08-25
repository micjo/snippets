#!/usr/bin/python

def time_decorator(orig_function):
    def wrapper(*args, **kwargs):
        return orig_function(*args, **kwargs)
    return wrapper


@time_decorator
def display(name, age):
    print "display function called with arguments({} {})".format(name,age)

display("John", 22)
