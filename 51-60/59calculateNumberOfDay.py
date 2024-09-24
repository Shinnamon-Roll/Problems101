from datetime import datetime

def daysBetweenDates(date1: str, date2: str) -> int:
    date_format = "%Y-%m-%d"
    d1 = datetime.strptime(date1, date_format).date()
    d2 = datetime.strptime(date2, date_format).date()

    return abs((d2 - d1).days)

def main():
    date1 = input("Enter date one (xxxx-xx-xx) : ")
    date2 = input("Enter date two (xxxx-xx-xx) : ")

    print(daysBetweenDates(date1, date2))

main()
