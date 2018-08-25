#!/usr/bin/python

def time_this(orig_func):
    import time
    def wrapper():
        start_time = time.time()
        result = orig_func()
        end_time = time.time()
        delta_time = end_time - start_time
        print "{} ran in {} seconds".format(orig_func.__name__, delta_time)
        return result
    return wrapper

def time_all_class_methods(Decoratee):
    class Decorator(object):
        def __init__(self):
            self.oInstance = Decoratee()

        def __getattribute__(self,s):
            #check if attribute exists in non-overwritten function and return this one
            #If you dont do this you will be stuck in infinite recursion
            try:
                x = super(Decorator,self).__getattribute__(s)
            except AttributeError:
                x = self.oInstance.__getattribute__(s)

            if callable(x):
                return time_this(x)
            else:
                return x

    return Decorator

@time_all_class_methods
class Animal(object):
    def __init__(self):
        pass

    def walk(self):
        print "Walking"



a = Animal()
a.walk()

