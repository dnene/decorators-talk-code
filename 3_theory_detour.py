# When only some of the arguments of a function are specified
# the result is another function which can accept the remainder
# of arguments. This is called a partially applied function

def add5(a,b,c,d,e):
    return a + b + c + d + e

print(add5(1,3,5,7,9))

from functools import partial
add79to = partial(add5,d=7,e=9)
print(add79to(1,3,5))

# While functools.partial is very flexible, there is an alternative
# way of partially applying functions, using nested functions

def nested_add(a,b):
    def add_remainder(c,d,e):
        return a + b + c + d + e
    return add_remainder

print(nested_add(1,3)(5,7,9))

# a particularly specific form is a special case of partial application
# called currying which applies one argument at a time.
# There is no built in support for currying in python though one 
# could write a curried equivalent

def curried_add(a):
    def add_4(b):
        def add_3(c):
            def add_2(d):
                def add_1(e):
                    return a + b + c + d + e
                return add_1
            return add_2
        return add_3
    return add_4

print(curried_add(1)(3)(5)(7)(9))

