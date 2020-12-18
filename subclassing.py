
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"Date: d={self.day}, m={self.month}, y={self.year}"

class Holiday(Date):
    # if we don't do anything special, parent doesn't get initialized!!!!
    def __init__(self, day, month, year, name):
        print("init Holiday")
        super().__init__(day, month, year)
        self.name = name

    def __str__(self):
        return "Holiday on " + super().__str__() + " called " + self.name

h = Holiday(1, 1, 2021, "new year's day")
print(type(h))
print(h)
