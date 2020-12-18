x = [1, 3, 5, 7, 9, 11]

# equivalent to MAP
y = [ z * 2 for z in x ]
print(type(y))
print(y)

# "if" provides a "filter" behavior
a = [ z * 2 for z in x if z < 9 ]
print(a)

x2 = [1, 2, 3, 4]
# nested for in creates a "flatMap" kind of effect.
r = [x for y in x2 for x in range(1, y)]
print(r)