l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
  
# output list
output = []
  
# function used for removing nested 
# lists in python. 
def reemovNestings(l):
    for i in l:
        if type(i) == list:
            print(i)
        else:
            output.append([i])
    print(output)

  
# Driver code
print ('The original list: ', l)
reemovNestings(l)
print ('The list after removing nesting: ', output)




