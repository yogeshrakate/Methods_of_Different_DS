#Methods of list

#append(object)
L=[1,2,3]
L.append(4)
print('1',L)
L.append('Hi')
print('2',L)
L.append(3.14)
print('3',L)
L.append((5,8))#tuple can be added to list
print('4',L)
#L.append(7,8)
#print(L)this will give TypeError as 2 arguments can't be given


#clear()
L.clear()
print('5',L)
L.append([14,'yog',(4,),3.7])
print('6',L)


#extend(iterable)
L.extend('Hello')
print('7',L)


#count(value)
L1=[14, 4, (4,), 14, 3.7, 'H', 'e', 'l', 'l', 'o']
print('8',L1.count('l'))
print('9',L1.count(14))
print('10',L1.count('H'))
print('11',L1.index(4))
print('12',L1.index(14))
print('13',L1.index(14,1))
#print(L.index(14,3))-----gives ValueError


#index(value,start=0,stop=2147483647)
L2=[10,10,20,30,50,10,20]
print('14',L2.index(10))
print('15',L2.index(10,1))
print('16',L2.index(10,2))
#print(L2.index(10,6))-----gives ValueError
#print(L2.index(40))-----gives ValueError


#insert(index,object)
L=[10,10,20,30,50,10,20]
L.insert(2,'Hi')
print('17',L)
L.insert(-1,'bye')
print('18',L)#value will be inserted and original value at mentioned place will be right shifted


#pop(index=-1)
L=[10,10,20,30,50,10,20]
print('19',L.pop())
print('20',L.pop())
print('21',L.pop(3))
#print(L.pop(7))-----gives IndexError
L1=[]
#print(L1.pop())-----gives IndexError(pop from empty list not possible)


#remove(value)
L=[10,10,20,30,50,10,20]
print('22',L.remove(10))#This will perform the action but won't return
L.remove(10)
print('23',L)#So 2 10s will be removed here
L.remove(50)
print('24',L)
#L.remove(70)
#print(L)-----ValueError: list.remove(x): x not in list


#reverse()
L=[10,10,20,30,50,10,20]
L.reverse()
print('25',L)


#sort(key=None, reverse=False)
L=[10,10,20,30,50,10,20]
L.sort()
print('26',L)
L.sort(reverse=True)
print('27',L)

L1=[10,'Hi',20,30,'Bye',10,' ',20]
L1.sort(key=str)
print('28',L1)#output in ASCII forms
L1.sort(key=str,reverse=True)
print('29',L1)

L2=['a','b','g','b','t','c']
L2.sort(key=str)
print('30',L2)




