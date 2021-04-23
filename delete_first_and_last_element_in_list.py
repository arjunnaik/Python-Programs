def chop(lst):
    del lst[0]
    del lst[-1]
    return None

def middle(lst):
    return lst[1:-1]



lst=[1,2,3,4,5,6,7,8,9,10]
new_List=middle(lst)
chop(lst)
print(lst)
print(new_List)