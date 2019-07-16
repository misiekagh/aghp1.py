def my_in(lst, val):
    while (len(lst)):
        if lst.pop()==val:
            return True
    return False

def my_index(lst, val):
    orglen=len(lst)
    while(len(lst)):
        if lst.pop(0)==val:
            return orglen-len(lst)
    return -1

def my_max2(val1, val2):
    if val1 > val2: return val1
    else: return val2

def my_max(lst):
    if (len(lst)<2):
        return my_max2(lst[0],lst[1])
    else:
        my_max(lst[1:])

def my_min(lst):
    pass


l=[4,5,8,4,6,8]
print(my_in(l,4))
print(my_in(l,10))
print(my_index(l,8))
print(my_max(l))
