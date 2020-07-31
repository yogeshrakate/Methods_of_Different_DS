#Methods of frozenset

#difference(set 2)(-)
f=frozenset({'a','b','c'})
f1=frozenset({'a','b','d','e','g','f'})
print('1',f.difference(f1))
print('2',(f1-f))



#symmetric_difference(set 2)(^)
f=frozenset({'a','b','c'})
f1=frozenset({'a','b','d','e','g','f'})
print('3',f.symmetric_difference(f1))
print('4',(f1^f))




#intersection(set 2)(&)
f=frozenset({'a','b','c'})
f1=frozenset({'a','b','d','e','g','f'})
print('5',f.intersection(f1))
print('6',(f1&f))




#isdisjoint(set 2)
f=frozenset({'a','b','c'})
f1=frozenset({'a','b','d','e','g','f'})
f2={'x', 'y', 'z'}
print('7',f1.isdisjoint(f2))
print('8',f.isdisjoint(f1))



#issubset(set 2)
f=frozenset({'a','b','c'})
f1=frozenset({'a','b','d','e','g','c'})
f2={'x', 'y', 'z'}
print('9',f1.issubset(f2))
print('10',f.issubset(f1))


#issuperset(set 2)
f=frozenset({'a','b','c'})
f1=frozenset({'a','b','d','e','g','c'})
f2={'x', 'y', 'z'}
print('11',f1.issuperset(f2))
print('12',f1.issuperset(f))


#union(set 2)(|)
f=frozenset({'a','b','c'})
f1=frozenset({'a','b','d','e','g','c'})
print('13',f1.union(f))



