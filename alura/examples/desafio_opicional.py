class Data:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year

    def format_date(self):
        print('{0}/{1}/{2}'.format(self.day, self.month, self.year))
        return True


if __name__ == "__main__":
    data = Data(21, 11, 2007)
    data.format_date()
