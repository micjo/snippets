#!/usr/bin/python


def time_this(orig_func):
    print "timing"
    def wrapper():
        return orig_func()
    return wrapper

def time_all_class_methods(Decoratee):
    class Decorator(object):
        def __init__(self):
            self.oInstance = Decoratee()

        def __getattribute__(self,s):

            #check if attribute exists in non-overwritten function
            try:
                x = super(Decorator,self).__getattribute__(s)
            except AttributeError:
                x = self.oInstance.__getattribute__(s)

            if callable(x):
                return time_this(x)
            else:
                return x

    return Decorator

class Animal(object):
    def __init__(self):
        pass

    def walk(self):
        print "Walking"


Animal = time_all_class_methods(Animal)

a = Animal()
a.walk()

