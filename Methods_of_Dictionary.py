#Methods of Dictionary

#clear()
d={'a':10,'b':20,'c':30}
d.clear()
print('1',d)


#get(key,default=None)
d={'a':10,'b':20,'c':30}
print('2',d.get('a'))
print('3',d.get('e'))
print('4',d.get('f','not present'))
print('5',d.get('b','Hello'))#key is present,so it will ignore default

#setdefault(key,default=None)
d.setdefault('e',15)
print('6',d)
d.setdefault('f')
print('7',d)
d.setdefault('b','Hello')#key is present,so it will ignore default
print('8',d)

#pop(key,default)
d1={'a':10,'b':20,'c':30}
print('9',d1.pop('b'))
print('10',d1.pop('f','Not available'))
#print(d1.pop('e'))------this will give keyError

#popitem()
d2={'a':10,'b':20,'c':30}
print('11',d2.popitem())
print('12',d2.popitem())
print('13',d2.popitem())
#print(d2.popitem())------this will give keyError

#update(dict2)
d3={'a':10,'b':20,'c':30}
d4={'b':'Hi','f':20,'e':30}
d3.update(d4)
print('14',d3)#this will be updated
print('15',d4)#as it is
d3={'a':10,'b':20,'c':30}
d4={'b':'Hi','f':20,'e':30}
d4.update(d3)
print('16',d3)#as it is
print('17',d4)#this will be updated


#keys(), values(), items()
d={'a':10,'b':20,'c':30,'d':'Hello'}
print('18',d.keys())#gives list of keys
print('19',d.values())#gives list of values
print('20',d.items())#gives list of 2-tuples of key:value pair
for k,v in d.items():
    print('21',f'Key:{k},Value:{v}')


#fromkeys(iterable, value=None)
s='abc'
d={}.fromkeys(s)
print('22',d)
d={}.fromkeys(s,2)
print('23',d)

