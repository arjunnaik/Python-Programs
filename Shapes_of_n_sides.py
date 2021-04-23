def findShape(n):
    if n==3:
        print("Triangle")
    elif n==4:
        print("Quadrilateral")
    elif n==5:
        print("Pentagon")
    elif n==6:
        print("Hexagon")
    elif n==7:
        print("Heptagon")
    elif n==8:
        print("Octagon")
    elif n==9:
        print("Nonagon")
    elif n==10:
        print("Decagon")
    else:
        print("Invalid Input Try Again")
while True:
    var = input("\n\nEnter Sides (Enter Stop To End) :\n")
    if var.lower()=="stop":
        exit()
    else:
        findShape(int(var))
