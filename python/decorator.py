#!/usr/bin/python

def time_decorator(orig_function):
    def wrapper():
        return orig_function()
    return wrapper


@time_decorator
def display():
    print ">>> This is a simple display function"

@time_decorator
def display(name, age):
    print ">>> display function called with arguments {} {}".format(name,age)


display()
