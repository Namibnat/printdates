# print dates from a starting to an ending date

import datetime
import sys
import os


def getdate():
    print("Input the year", end="")
    year = int(input(" "))
    print("Input the month", end="")
    month = int(input(" "))
    print("Input the day of the month", end="")
    day = int(input(" "))
    return datetime.datetime(year, month, day)

def determine_format():
    if len(sys.argv) > 1:
        format = sys.argv[1]
        if format not in ["euro", "usa"]:
            print("Unrecognized format, select from 'euro' or 'usa'")
            format = False
    else:
        format = "euro"
    return format

class print_dates:
    def __init__(self, format, start_date, end_date):
        self.format = format
        self.start_date = start_date
        self.end_date = end_date

    def printit(self, date):
        if self.format == "euro":
            print("{0:%A, %d %B %Y}\n".format(date))
        else:
            print("{0:%A, %B %d %Y}\n".format(date))

    def p_routine(self):
        date = self.start_date
        os.system("clear")
        while date <= self.end_date:
            self.printit(date)
            date += datetime.timedelta(days=1)

if __name__ == "__main__":
    format = determine_format()
    if format:
        print("Start date")
        start_date = getdate()
        print("End date")
        end_date = getdate()
        if end_date > start_date:
            pdate = print_dates(format, start_date, end_date)
            pdate.p_routine()
        else:
            print("The dates you entered are not correct")


