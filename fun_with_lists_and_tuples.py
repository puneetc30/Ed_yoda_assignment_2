size = int(input("Enter the size of the list: "))
lst = []
for i in range(size):
    lst1 = []
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