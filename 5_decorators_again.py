from functools import wraps

def trace(func) :
    @wraps(func)
    def wrapper(*args, **kwargs) :
        print("Entering {} with arguments {} {}".format(
                                        func.__name__, args, kwargs))
        ret = func(*args, **kwargs)
        print("Leaving {} with result {}".format(func.__name__, ret))
        return ret
    return wrapper

# Can you pass arguments to the decorators ?
# Yes. Lets say you wanted to parameterise some message text

# The key thing is that you need to write a function which 
# takes in the argument and returns what you currently
# recognise to be a decorator (a function that takes a function)

def trace_message(entering_text, leaving_text):
    def trace(func) :
        @wraps(func)
        def wrapper(*args, **kwargs) :
            print("{} {} with arguments {} {}".format(
                    entering_text, func.__name__, args, kwargs))
            ret = func(*args, **kwargs)
            print("{} {} with result {}".format(leaving_text, func.__name__, ret))
            return ret
        return wrapper
    return trace

@trace_message("Starting", "Stopping")
def add(a,b):
    return a + b

@trace_message("Beginning", "Ending")
def sub(a,b):
    return a - b

add(3,5)
sub(7,4)

