# print dates from a starting to an ending date

import datetime


def getdate():
    print("Input the year")
    year = int(input(" "))
    print("Input the month")
    month = int(input(" "))
    print("Input the day of the month")
    day = int(input(" "))
    return datetime.datetime(year, month, day)


if __name__ == "__main__":
    start_date = getdate()
    print("{0:%F}".format(start_date))


