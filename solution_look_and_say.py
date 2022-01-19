num = int(input())
lst = []
value = 1
count = 0
for i in range(num):
    if len(lst)==0:
        lst.append(value)
        print(lst[0])
        continue  
    value = lst[0]
    count = 0
    size = len(lst)
    for j in range(size):
        if value == lst[j]:
            count += 1
        else:
            lst.append(count)
            lst.append(value)
            value = lst[j]
            count = 1
    lst.append(count)
    lst.append(value)
    for k in range(size):
        lst.remove(lst[0])
    lst =[str(i) for i in lst]    
    print(''.join(lst))