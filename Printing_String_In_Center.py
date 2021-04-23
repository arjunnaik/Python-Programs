def func(str,n=80):
    for i in range(n):
        print(end=" ")
    print(str)





str1=input("Enter First String...")
str2=input("Enter Second String...")
str3=input("Enter Third String...")
str4=input("Enter Fourth String...")
func(str1)
func(str2,80+len(str1)//2-len(str2)//2)
func(str3,80+len(str1)//2-len(str3)//2)
func(str4,0)

