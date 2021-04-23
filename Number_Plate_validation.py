var = input("Enter Number Plate :")
if len(var)==6:
    var1=var[3:]
    var2 = var[:3]
    if var1.isdigit() and var2.isupper():
        print("License plate is older...")
    else:
        print("Invalid License plate...")
elif len(var)==7:
    var1=var[:4]
    var2=var[4:]
    if var1.isdigit() and var2.isupper():
        print("License plate is Newer...")
    else:
        print("Invalid License plate...")
else:
    print("Invalid License plate...")