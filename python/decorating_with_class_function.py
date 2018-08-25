#!/usr/bin/python

class Foo:
    def timer(orig_func):
        import time
        def wrapper():
            start_time = time.time()
            result = orig_func()
            end_time = time.time()
            delta_time = end_time - start_time
            print "{} ran for {} seconds".format(orig_func.__name__, delta_time)
        return wrapper
    stat=staticmethod(timer)

# this is equivalent to (second one is more pythonic) :

class Foo:
    @staticmethod
    def timer(orig_func):
        import time
        def wrapper():
            start_time = time.time()
            result = orig_func()
            end_time = time.time()
            delta_time = end_time - start_time
            print "{} ran for {} seconds".format(orig_func.__name__, delta_time)
        return wrapper

@Foo.timer
def display():
    import time
    print "Display Function"
    time.sleep(1)

display()
