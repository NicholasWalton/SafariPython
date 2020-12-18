# names = ["Fred", "Jim", 99]
names = ["Fred", "Jim", "Sheila"]
print(type(names))
print(names)
print(names[2])
names[0] = "Frederick"
print(names)
# slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ]
print(numbers)
print(numbers[3:10:2])
print(numbers[::-1])
print(numbers)
# "Pythonic" => good python style
numbers[3:5] = [101, 102, 103, 104, 105, 106]
print(numbers)

print(500 in numbers)
print(1 in numbers)

x = 1, 2, 3, "Hello"
print(type(x))
print(x)
print(("a", "b", "c"))

print(x[1:4])

# Tuples are "immutable"
# x[0] = "new Value"
# print(x)

x = {"Fred": "Jones", "Alice": "Wonderland"}
print(type(x))
print(x)

print(x["Fred"])
x["Alice"] = "Very special"
print(x)
del x["Fred"]
x["Frederic"] = "Jones"
print(x)

print(x.items())
print(x.keys())
print(x.values())

print("Frederic" in x)
print("Jones" in x.values())

# Complex numbers!
print(1j)
print(1j*1j)

print(True and False)
print(True or False)
# bitwise xor , also "library" xor more correct for boolean
print(True ^ True)
# bitwise operators
print(3 & 1)
print(3 | 5)
