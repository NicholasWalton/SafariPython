print('Hello "Python" World!', 99, sep="\n")
x=101
print("the value is", x)
# Concatenate Strings--yes :)
name="Fred" + " Jones"
print(name)
# Don't have autoconversion to string with concatenation
# name=7 + "of nine"
# print(name)
name=str(7) + " of nine"
print(name)

x = 10
y = "11"
z = x + int(y)
print(z)

print(" \"hello\" she said ")

x = 10.2
y = 3
print(type(x))
print(type(y))

print(3/2)
print(3//2)
print(3.5//2)

print(2**16)

x = 10
x += 3 # equivalent to x = x + 3
print(x)

# walrus new with 3.8
print(x := 99)
print(x)

x = 9E+300
print(x)

# f = 3E500
# print(f)
f = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# f *= f
# f *= f
# f *= f
# f *= f
# f *= f
# f *= f
# f *= f
x = int(f)
print(x)

print(type(True))

x = "Hello"
y = "Hello"
print(x == y)
print(x is y)

x = "Hello"
y = "He"
y += "llo"
print(x, y)
print(x == y)
print(x is y)


