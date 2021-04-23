def findSeason(month,day):
    if month in ('january', 'february', 'march'):
        if (month == 'march') and (day > 19):
            return 'spring'
        else:
            return 'winter'

    elif month in ('april', 'may', 'june'):
        if (month == 'june') and (day > 20):
            return 'summer'
        else:
            return 'spring'
    elif month in ('july', 'august', 'september'):
        if (month == 'september') and (day > 21):
            return 'Fall'
        else:
            return 'summer'
    elif month == 'december':
        if day > 20:
            return 'winter'
        else:
            return 'Fall'
    else:
        return 'Wrong Month'

month=input("Enter month :\n")
date=int(input("Enter date :\n"))
if date<=31 and date>=1:
    print(findSeason(month.lower(),date))
else:
    print("Invalid Date")
