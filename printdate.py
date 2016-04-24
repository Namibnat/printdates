# print dates from a starting to an ending date

import datetime
import sys


def getdate():
    print("Input the year")
    year = int(input(" "))
    print("Input the month")
    month = int(input(" "))
    print("Input the day of the month")
    day = int(input(" "))
    return datetime.datetime(year, month, day)

def determine_format():
    if len(sys.argv) < 1:
        format = sys.argv[1]
        if format not in ["euro", "usa"]:
            print("Unrecognized format, select from 'euro' or 'usa'")
            return False
    else:
        format = "euro"


if __name__ == "__main__":
    format = determine_format()
    if format:
        start_date = getdate()
        print("{0:%F}".format(start_date))


