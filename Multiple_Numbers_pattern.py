for i in range(1,11):
  print("  ",i,end="")
print()
for i in range(1,11):
  print(i,end=" ")
  for j in range(1,11):
    print("%2d"%(i*j),end="  ")
  print()