#!/usr/bin/python

class DecoratorClass(object):
    def __init__(self, orig_func):
        self.orig_func = orig_func

    def __call__(self, *args, **kwargs):
        print " >> wrapper Function"
        return self.orig_func(*args, **kwargs)


@DecoratorClass
def display(name, age):
    print "display called with args ({}, {})".format(name,age)


display("Jack",30)


