#!/usr/bin/python

def time_all_class_methods(Decoratee):
    class Decorator(object):
        def __init__(self):
            self.oInstance = Decoratee

        def __getattribute__(self,s):
            print "trala"

            #check if attribute exists in non-overwritten function
            x = super(Decorator,self).__getattribute__(s)
            if ( x ):
                return x
            else:
                return self.oInstance.s

    return Decorator

class Animal(object):
    def __init__(self):
        pass

    def walk(self):
        print "Walking"


Animal = time_all_class_methods(Animal)

a = Animal()
a.walk()

