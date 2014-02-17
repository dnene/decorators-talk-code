# specify constraints, annotate requests, impose conditions etc.

def supports(type_):
    def deco(func):
        def wrapper(request):
            method = request["method"]
            if request["method"] in type_ :
                return func(request)
            else :
                raise Exception("Invalid method {0}".format(method))
        return wrapper
    return deco
            
@supports(["GET"])
def process(request):
    # It can be assumed that the request is only a get request
    print("Processed {0}".format(request["name"]))
    
process({"method": "GET", "name": "foo"})
# process({"method": "POST", "name": "foo"})

# introduce aspects ie. before/after behaviour - eg. tracing

# markers, metadata, housekeeping (- not explaining much here)

# autoregistration

func_table = {}
def operator(symbol):
    def deco(func):
        def wrapper(first, second):
            return func(first, second)
        func_table[symbol] = wrapper
    return deco

@operator("+")
def add(a,b): 
    return a + b

@operator("-")
def sub(a,b):
    return a - b

@operator("*")
def mult(a,b):
    return a * b

def evaluate(expr):
    tokens = expr.split()
    if len(tokens) != 3 :
        raise Exception("Need exactly 3 tokens")
    return func_table[tokens[1]](int(tokens[0]), int(tokens[2]))
    
print(evaluate("3 + 4"))
print(evaluate("5 - 2"))
print(evaluate("4 * 5"))


# Memoisation

def memoise(func):
    cache = {}
    def wrap(*args):
        if args in cache :
            print("Cache hit")
            return cache[args]
        else :
            result = func(*args)
            cache[args] = result
            return result
    return wrap

@memoise
def foo(a,b):
    # some long computation
    return (a * 73 - b * 25) / (a+b)

print(foo(3,4))
print(foo(4,5))
print(foo(5,6))
print(foo(4,5))