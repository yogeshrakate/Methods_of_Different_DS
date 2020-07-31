#Methods of String

S="Sagveek.Technologies"
print('1',S.capitalize())
print('2',S.lower())
print('3',S.swapcase())
print('4',S.upper())
print('5',S.split())
#split function converts string into list
print('6',S.partition('k'))
#partition function converts string into 3 tuple
print('7',S.partition('x'))
print('8',S.partition('.'))
print('9',S.split('.'))
print('10',S.split('o'))
print('11',S.partition('o'))
print('12',S.split('e',maxsplit=3))
print('13',S.split('e',maxsplit=2))
print('14',S.split('e'))
S1="123456"
print('15',S1.swapcase())
print('16',list(S1))
S2="My name is Yogesh Rakate"
print('17',S2.count('a'))
print('18',list(S2))
print('19',S2.title())
print('20',S2.split())
print('21',S2.endswith('te'))
print('23',S2.endswith('Rakate'))
print('24',S2.startswith('te'))
print('25',S2.startswith('m'))
print('26',S2.startswith('M'))
print('27',S2.startswith('t',-2))
print('28',S2.startswith('Y',11,17))
print('29',S2.find('te'))
print('30',S2.find('Y'))
print('31',S2.find('a'))
print('32',S2.find('a',5))
print('33',S2.find('MY'))
print('34',S2.index('Y'))
print('35',S2.index('M'))
S3="YogeshRakate"
print('36',S3.isalnum())
print('37',S3.isalpha())
print('38',S3.isdigit())
print('39',S3.isupper())
print('40',S3.istitle())
S4="Yogesh Rakate"
print('41',S4.istitle())
print('42',S4.isalpha())
S5="12345678"
print('43',S5.isdigit())
print('44',S5.isalnum())
print('45',S5.isnumeric())
S6="12.34"
print('46',S6.isdigit())
S7="   "
print('47',S7.isspace())
S8="YOGESH RAKATE"
print('48',S8.isupper())
print('49',S8.islower())
S9="yogesh rakate"
print('50',S9.isupper())
print('51',S9.islower())
S10="     Yogesh Rakate      "
print('52',S10.lstrip())
print('53',S10.rstrip())
print('54',S10.strip())
S11="aabca*#Yogesh Rakateaacdacb@#a"
print('55',S11.lstrip('abc*#'))
print('56',S11.rstrip('abc*#@'))
print('57',S11.strip('abc*#@d'))
S12="My name is Yogesh Rakate"
print('58',S12.replace('a','@'))
print('59',S12.replace('a','@',2))
print('60',S12.replace('e','#',2))
name="Yogesh"
age=25
print('61',"The name is %s, age is %d"%(name, age))
'''By mistake if you give command like
print("The name is %s, age is %d"%(age, name))
it will show type error'''
print('62',"The name is {}, age is {}".format(name, age))
print('63',"The name is {}, age is {}".format(age, name))
#In above line mistake is there still error won't be there and result will be printed
print('64',f"The name is {name}, age is {age}")
for i in range(1,11):
    print('65',f'The square of {i} is {i*i}')
L=['My', 'name', 'is', 'Yogesh', 'Rakate']
print('66',' '.join(L))
#join function converts list into string by joining list elements by space or mentioned element
print('67','.'.join(L))
print('68','@'.join(L))

