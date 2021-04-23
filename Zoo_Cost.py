cost=0
print('Enter the ages of members :')
while True:
    n=input()
    if n=="":
        break
    elif int(n)<=2:
        continue
    elif int(n)>=3 and int(n)<=12:
        cost=cost+14
    elif int(n)>=65:
        cost=cost+18
    else:
        cost = cost+23

if cost==0:
	print('Invalid input!!!')
else:
	print('Total cost =  %.2f'%(cost))