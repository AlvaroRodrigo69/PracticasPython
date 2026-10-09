def aumenta(x):
    print(id(x))
    x+=[1]
    print(id(x))
    return x

a=[3]
print(id(3),id(4))
print(id(a))
print(aumenta(a))
print(a)
print(id(a))