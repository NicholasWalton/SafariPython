def show_date(day, month, year=2020):
    print(f"day = {day}, month = {month} year = {year}")

def do_stuff(a, b = 99, c = "Unspecified"):
    print(f"a is {a} b is {b} c is {c}")

do_stuff(1, "hello", [1, 2, 3])
do_stuff(1, "hello")
do_stuff(1, c = "real")

show_date(month=12, day=18)

def show_many(a, b, *c, **kwargs):
    """
    This is the documentation for this function
    :param a:
    :param b:
    :param c:
    :param kwargs:
    :return:
    """
    print(f"a is {a}, b is {b}")
    print(type(c))
    print(c)
    for v in c:
        print(f"-- {v}")
    print(type(kwargs))
    print(kwargs)
    for t in kwargs.items():
        print(f"a key is {t[0]}, it's value is {t[1]}")


show_many(1, 2, 9, 8, 7, 6)

args=[1, 2, 3, 4, 5, 6, 7, 8]
show_many(*args)

# 1, 2, are positional args
# 3, 4 are varargs -- map to *c or more conventionally *args
# name, dob are "keyword" args (map convetionslly to **kwargs)
show_many(1, 2, 3, 4, name="Alfred", dob=(1, 1, 1920))

print(show_many.__doc__)

def nowt():
    return 99

print(nowt())

# lambda...

# def add(a, b):
#     return a + b
#

# Python lambdas are anonymous *single*line* functions..
add = lambda a, b: a + b

print("This time, with a lambda")
print(add(1, 2))

addup = add

print(type(addup))

print(addup(9, 1))

def add_to(v):
    def internal(w):
        return v + w
    return internal

add_two = add_to(2)

print(add_two(3))
