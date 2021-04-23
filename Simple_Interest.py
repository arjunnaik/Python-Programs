principleAmount = float(input("Enter principle amount"))
rateOfInterest = float(input("Enter rate of interest"))
timePeriod = float(input("Enter time period"))
si = principleAmount*rateOfInterest*timePeriod/100
print("Interest is",si)
print("Total Amount is",si+principleAmount)

