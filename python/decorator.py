#!/usr/bin/python

def time_decorator(orig_function):
    def wrapper():
        result = orig_function()
    return wrapper


@time_decorator
def display():
    print ">>> This is a simple display function"

display()
