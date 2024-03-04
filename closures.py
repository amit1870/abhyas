# closures : close over
# closures : a function that retains access to variables from the outer (enclosing) scope
# closures : even after the outer function has finished executing.
# closures : captures the variables it needs from its surrounding environment,
# closures : allowing you to maintain state information in a way that's both elegant and efficient.
# closures : how it works ?
# closures : outerfunction(Enclosing Function):
# closures : innerfunction(Nested Function)
# closures : Variable Capture: When an innerfunction references a variable from its enclosing scope (outerfunction scope),
# closures : Python "captures" or retains that variable's value, allowing it to be used later, even when the outer function has returned.
# closures : a powerful tool for managing state and creating flexible, reusable code.
# closures : variable 'factor' from outerfunction(multiplier) is being attached to innerfunction(multiply).

def calculator(a,b):
    def add():
        return a + b

    def sub():
        return a - b

    def mul():
        return a * b

    def div():
        return a / b

    return sub

sub = calculator(10,20)
print(sub())



def multiplier(factor):
    def multiply(x):
        return x * factor

    return multiply

duble = multiplier(2)
triple = multiplier(3)
half = multiplier(0.5)

dubbled = duble(20)
trippled = triple(30)
halfed = half(100)

print('dubbled' , dubbled)
print('trippled' , trippled)
print('halfed' , halfed)
