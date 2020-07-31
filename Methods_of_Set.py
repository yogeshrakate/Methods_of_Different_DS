#Methods of Sets

#add(element)
s={'a','b','c'}
s.add('d')
s.add('a')
print('1',s)


#clear()
s.clear()
print('2',s)



#difference(set 2)(-)
s={'a','b','c'}
s1={'a','b','d','e','g','f'}
print('3',s.difference(s1))
print('4',(s1-s))


#difference_update(set 2)(-=)
s={'a','b','c'}
s1={'a','b','d','e','g','f'}
s1.difference_update(s)
print('5',s1)
s-=s1
print('6',s)


#symmetric_difference(set 2)(^)
s={'a','b','c'}
s1={'a','b','d','e','g','f'}
print('7',s.symmetric_difference(s1))
print('8',(s1^s))


#symmetric_difference_update(set 2)(^=)
s={'a','b','c'}
s1={'a','b','d','e','g','f'}
s.symmetric_difference_update(s1)
print('9',s)
s1^=s
print('10',(s1))


#discard(element)
s={'a','b','c'}
s.discard('a')
print('11',s)
s.discard('f')
print('12',s)


#remove(value)
s={'a','b','c'}
s.remove('a')
print('13',s)
##s.remove('f')
##print('13',s)=====>KeyError: 'f'


#pop()===>arbitrary
s={'a','b','c'}
print('14',s.pop())
print('14',s.pop())
print('14',s.pop())
##print('14',s.pop())====>KeyError: 'pop from an empty set'



#intersection(set 2)(&)
s={'a','b','c'}
s1={'a','b','d','e','g','f'}
print('15',s.intersection(s1))
print('16',(s1&s))



#intersection_update(set 2)(&=)
s={'a','b','c'}
s1={'a','b','d','e','g','f'}
s.intersection_update(s1)
print('17',s)
s1&=s
print('18',(s1))



#isdisjoint(set 2)
s={'a','b','c'}
s1={'a','b','d','e','g','f'}
s2={'x', 'y', 'z'}
print('19',s1.isdisjoint(s2))
print('20',s.isdisjoint(s1))



#issubset(set 2)
s={'a','b','c'}
s1={'a','b','d','e','g','c'}
s2={'x', 'y', 'z'}
print('21',s1.issubset(s2))
print('22',s.issubset(s1))


#issuperset(set 2)
s={'a','b','c'}
s1={'a','b','d','e','g','c'}
s2={'x', 'y', 'z'}
print('23',s1.issuperset(s2))
print('24',s1.issuperset(s))


#union(set 2)(|)
s={'a','b','c'}
s1={'a','b','d','e','g','c'}
print('25',s1.union(s))



#update(set 2)(|=)
s={'a','b','c'}
s1={'a','b','d','e','g','c'}
s1.update(s)
##Or we can use s1|=s
print('26', s1)



