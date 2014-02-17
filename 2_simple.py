# Very basic decorator - tracing a function call
# Note: I am prefixing function names with "traced_" for emphasis
# You would not usually do that

def trace(func) :
    def wrapper(*args, **kwargs) :
        print("Entering {} with arguments {} {}".format(
                                        func.__name__, args, kwargs))
        ret = func(*args, **kwargs)
        print("Leaving {} with result {}".format(func.__name__, ret))
        return ret
    return wrapper

def add(a, b):
    return a + b

@trace
def traced_add(a,b):
    return a+b

@trace
def traced_subtract(a,b):
    return a-b

add(3,4)
traced_add(6,7)
traced_subtract(9,3)

# You can use decorators to inject code around a function
# ie. before and/or after a function 

