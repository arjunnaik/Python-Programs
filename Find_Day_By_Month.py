def findDayByMonth(month):
    if month == "stop":
        exit()
    elif month == "february":
        print("28 or 29")
        print("If days are 29 leap year otherwise not leap year")
    elif month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december":
        print("31")
    elif month == "april" or month == "june" or month == "september" or month == "november":
        print("30")
    else:
        print("Invalid Input, Try again")

while(True):
    month=input("Enter Month (Enter Stop to End) :\n")
    findDayByMonth(month.lower())
