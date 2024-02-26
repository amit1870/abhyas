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
