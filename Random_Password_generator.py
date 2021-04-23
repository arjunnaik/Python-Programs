import random as R
def generate():
    n = R.randint(33,126)
    return chr(n)


obj = R.randint(7, 10)
print('Randomly Generated Password : ',end="")
for _ in range(obj):
    print(generate(), end="")

