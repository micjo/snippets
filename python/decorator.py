#!/usr/bin/python

def time_decorator(orig_function):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = orig_function(*args, **kwargs)
        end_time = time.time()
        delta_time = end_time - start_time
        print "{} function ran for {} seconds".format(orig_function.__name__, delta_time)

        return result
    return wrapper


@time_decorator
def display(name, age):
    import time
    time.sleep(1)
    print "display function called with arguments({} {})".format(name,age)

display("John", 22)
