def multiply(a, b):
    return a * b

def multiplyList(a):
    x = 1
    for i in a:
        x *= i
    return x

print(multiply(2, 3))
print(multiplyList([1, 2, 3]))