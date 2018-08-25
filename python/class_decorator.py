#!/usr/bin/python

class Timer(object):

    def __init__(self, orig_func):
        self.orig_func = orig_func

    def __call__(self, *args, **kwargs):
        # This means importing time has to happen each time you call the function.
        # Seems to me this is done more elegantly in the decorators without classes.
        import time
        start_time = time.time()
        result = self.orig_func(*args, **kwargs)
        end_time = time.time()
        delta_time = end_time - start_time
        print "{} ran for {} seconds".format(self.orig_func.__name__, delta_time)
        return result


@Timer
def display(name, age):
    print "display called with args ({}, {})".format(name,age)


display("Jack",30)


