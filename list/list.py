#list
l1 = []

# to add an element
l1.append(1)
l1.append(2)
print(l1)
# to remove certain element
l1.remove(1)
print(l1)
# to remove the last element 
l1.pop()
l1.append(3)
l1.append(2)
# to check how much time the element has occurred
print(l1.count(1))
# this is slicing
# it has [:::] - first is start / second stop / 3rd is step 
l1[:] = [1,2]
print(l1)
#list comprehensive
l2 = [(x,y) for x in range(2) for y in range(3)]
print(l2)



