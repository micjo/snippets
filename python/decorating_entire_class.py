#!/usr/bin/python

def time_all_class_methods(Decoratee):
    class Decorator(object):
        def __init__(self):
            self.oInstance = Decoratee

        def __getattribute__(self,s):

            #check if attribute exists in non-overwritten function
            try:
                x = super(Decorator,self).__getattribute__(s)
                return x
            except:
                return self.oInstance.__getattribute__(s)

    return Decorator

class Animal(object):
    def __init__(self):
        pass

    def walk(self):
        print "Walking"


Animal = time_all_class_methods(Animal)

a = Animal()
a.walk()

