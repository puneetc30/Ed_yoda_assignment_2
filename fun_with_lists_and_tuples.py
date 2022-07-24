size = int(input("Enter the size of the list: "))
# This will take input from user for the size of list.
lst = []
for i in range(size):
    lst1 = []
    # then this will take input from user to add two elements in each tuple in the list of tuples.
    ele1 = int(input("Enter first element: "))
    lst1.append(ele1)
    ele2 = int(input("Enter second element: "))
    lst1.append(ele2)
    t = tuple(lst1)
    lst.append(t)
print(lst)
for i in range(size):
    lst[i] = list(lst[i])
    lst[i].reverse()
lst.sort()
for i in range(size):
    lst[i].reverse()
    lst[i] = tuple(lst[i])
print(lst)
