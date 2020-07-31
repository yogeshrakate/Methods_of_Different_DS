#METHODS ON TUPLE

#count(value)
t=(1,1,4,3,3,8,5,1,33,36,1,0,1,2)
print('1', t.count(1))
print('2', t.count(6))

#index(value, start=0, stop=2147483647)
print('3',t.index(1))
print('4',t.index(1,3))
#print('4',t.index(3,7))----ValueError: tuple.index(x): x not in tuple
#print('4',t.index(6))----ValueError: tuple.index(x): x not in tuple
print('5', t.index(33,5))
