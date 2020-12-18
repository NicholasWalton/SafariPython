# x = True
# x = [3]
x = 3
print(bool(x))

if x == 3:
    print("it is three")
    print("still going")
    # print("still going")
elif x == 5:
    print("it's five")
else:
    print("it's not")
# if x == 3:
#     print("it is three")
#     print("still going")
#     # print("still going")
# else:
#     if x == 5:
#         print("it's five")
#     else:
#         print("it's not")

# Python does NOT have "switch/case"

x = 4
while x > 0:
    print(x)
    x -= 1

print("loop completed")

x = ["Fred", "Jim", "Sheila"]
for n in x:
    print(f"{n} is one of the names")

for c in "Hello World":
    print(c)

x = range(1, 10, 2)
print(type(x))
print(x)
# for v in range(1, 10, 2):
for v in x:
    print(v, end="")
    # print(v, sep=", ", end="END")

print("Hello", "Bonjour", sep="", end="")
print("goodbye")

x = 0
while x < 10:
    print(f"x is {x}")
    x += 1
    # if x > 3:
    #     break
else:
    print("in the else")

