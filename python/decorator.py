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

def log_call_decorator(orig_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_function.__name__), level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info("Function <{}> ran with args:{} and kwargs:{}"
                .format(orig_function.__name__,args,kwargs))
        return orig_function(*args, **kwargs)
    return wrapper

@log_call_decorator
def display(name, age):
    import time
    time.sleep(1)
    print "display function called with arguments({} {})".format(name,age)

display("John", 22)
