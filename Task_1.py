class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'{Date.validate(d.day, "d")}.{Date.validate(d.month, "m")}.{Date.validate(d.year, "y")}'

    @classmethod
    def extract(cls, date_str, delim = '.', start = 0):
        day, month, year = map(int, date_str.split(delim))
        return cls(day, month, year)

    @staticmethod
    def validate(numb, d_type):
        if d_type == 'd':
            if not(1 <= numb <= 31):
                return 'invalid date'
        if d_type == 'm':
            if not(1 <= numb <= 12):
                return 'invalid month'
        return numb

    # def extract_recursion(cls, value, start=0):
    #     if value.find('-', start) == -1 or start > len(value) :
    #         return [int(value[start:len(value)])]
    #     else:
    #         return [int(value[start: value.find('-', start)])] + extract_recursion(value.find('-', start) + 1)

# ======================================================================================================================


d = Date.extract('01-54-2020', '-')
print(d)