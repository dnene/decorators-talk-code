# bindings declared in an outer scope remain valid
# even after the the function in which these were declared
# is over, especially if an inner function was returned

def increment():
    step1 = 7
    step2 = 4
    def inner(b):
        return step1 + step2 + b
    return inner

incrementer = increment()

# Note - the function increment completed its work.
# Usually any local variables would've gone out of scope
print(incrementer(3))

# However in this case a function escaped
# And that function carried the values
print(incrementer)
for v in incrementer.__closure__ :
    print(v.cell_contents)
    
# This is how bindings in a outer function / decorators scope
# remain visible to the wrapped function




