# class Thing(object):
class Thing:
    """
    Classes in python do not define "fields" in the conventional way..
    Python does NOT have "private"
    """
    # "dunder" methods are "double underscore"
    def __init__(self, name = "Unknown", address = "Unknown"):
        print("__init__ invoked")
        # self prefix is MANDATORY
        self.name = name
        self.address = address

    def __str__(self):
        return f"Thing with name {self.name} address {self.address}"

    def __repr__(self):
        # return "REPR:" + self.__str__()
        # return "REPR:" + str(self)
        return str(self)

# python doesn't use "new" for construction
# create object (kindof empty map), and then pass it to __init__ function for initialization
t = Thing("Fred", "10 Penny Lane")

print(type(t))
print(t)

things = [t, Thing("Albert", "Over there")]
print(things)

# can, usually, add and manipulate fields "from the outside" -- probably bad style
# t.name = "Fred"
# print(t.name)
# t.address = "Over there"
# del t.name
# print(t.address)
# # print(t.name)
