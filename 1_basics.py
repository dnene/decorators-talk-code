# Functions are values
# Here a is a binding to a value

a = 3
print(a)

# b is also a binding to a value
# in this case the value happens to be a function

def greet(name): return "Hello {0}".format(name)

b = greet

print(b("Dhananjay"))

# You can pass in functions

names = []
def register(name, greeting):
    names.append(name)
    print(greeting(name))
    
register("Nene", greet)

# You can even return functions

names = []
def spanish_greeting(name): return "Hola {0}".format(name)

def greeter(lang):
    return spanish_greeting if lang == "spanish" else greet

print(greeter("spanish")("gnunify"))
print(greeter("english")("gnunify"))

# Functions can be nested
def greeter2(lang):
    def spanish_greeting(name): 
        return "Hola2 {0}".format(name)
    
    def default_greeting(name): 
        return "Hello2 {0}".format(name)
    
    return spanish_greeting if lang == "spanish" else default_greeting
    
print(greeter2("spanish")("gnunify"))
print(greeter2("english")("gnunify"))

# This capabilities of 
# a. treating functions as values
# b. passing in and returning functions
# c. nesting functions
# will be used to create decorators
