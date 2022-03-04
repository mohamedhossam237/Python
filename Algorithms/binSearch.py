def bin_search(ourlist, key):
    left = 0 # I assign left position to zero
    right = len(ourlist)-1 # I assign right position by defining the length of ourlist minus one 
    matched = False
    while(left<=right and not matched): # the loop will continue untill the left element is less or equal to the right element and the matched is True
        mid = (left+right)//2 # I find the position of the middle element
        if ourlist[mid] == key: # if the middle element correponds to the key element
             matched = True
        else: #otherwise 
            if key < ourlist[mid]: # if key element is less than the middle element
                right = mid - 1 #I assign the position of the right element as mid - 1
            else: #otherwise
                left = mid + 1 #left position will become the middle position plus 1
    return matched

print(bin_search([1, 3, 9, 15], 17))
print(bin_search([1, 3, 9, 15], 3))
