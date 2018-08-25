#!/usr/bin/python

from functools import wraps

def time_measure(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = orig_func(*args, **kwargs)
        end_time = time.time()
        delta_time = end_time - start_time
        print "{} function ran for {} seconds".format(orig_func.__name__, delta_time)
        return result
    return wrapper

def log_call_to_specific_file(file_name):
    def log_call_to_file(orig_func):
        import logging
        logging.basicConfig(filename=file_name, level=logging.INFO)

        @wraps(orig_func)
        def wrapper(*args, **kwargs):
            logging.info("Function <{}> ran with args:{} and kwargs:{}"
                .format(orig_func.__name__,args,kwargs))
            return orig_func(*args, **kwargs)
        return wrapper
    return log_call_to_file


@log_call_to_specific_file("logging.txt")
@time_measure
def display(name, age):
    import time
    time.sleep(1)
    print "display function called with arguments({} {})".format(name,age)

display("John", 22)

# This is equivalent to:

def display(name, age):
    import time
    time.sleep(1)
    print "display function called with arguments({} {})".format(name,age)

display = log_call_to_specific_file("logging.txt")(time_measure(display))

display("John",22)
