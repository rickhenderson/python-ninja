values = [1,2,3,4]
needle = 4
#  Works with 2 exit conditions checked for:
# * stop if needle is found
# * stop before you reach out of bounds

def lin_search(values, needle):
    n = len (values)
    pos = 0
    found = False
    count = 0
    
    # continue while not found and not at end of list 
    while found != True and pos != n:
        if values [pos] != needle:
            pos = pos + 1
        else:
            found = True

    if found:
        result = pos
    else:
        result = -1
        
    return result


ans = lin_search(values, needle)
print ("Found at position: {}.".format (ans))
