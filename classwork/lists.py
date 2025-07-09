l = ['hi',1,'helo']                #creating list
a = list(['hii','hello','think'])    # creating list with list() function
b = [['hi','hel'],[1,2,3],['key',11]]     # creating nested lists 
d = [11,5,3,55,6,8,77,98]
print(a.append("how"))             # appending at last of list
print(a.pop())                     # remove the last element
print(a.sort())                    # sort the list
print(a.sort(reverse  = True))  # sorted list reversed list True
print(a[1])                        # returns first element in list
print(a[-1])
print(a[0])
print(a[::-1])                        # returns slicing in list
print(a[:2:])
print(a[1:])
a[2]="hell"
print(a[2])
a.append(1)
a.insert(10,3)
a.remove(1)
print(a)
a.pop()
a.clear()
fruits = ['apple','banana','pine','grape','guava','avacado','papaya']
for i in fruits:
    print(i)
print(fruits.sort(reverse= True))      