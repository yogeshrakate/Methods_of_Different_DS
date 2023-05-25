#Methods of String

S="Sagveek.Technologies"
print('1',S.capitalize()) # output ==> "Sagveek.technologies"
print('2',S.lower()) # output ==> "sagveek.technologies"
print('3',S.swapcase()) # output ==> "sAGVEEK.tECHNOLOGIES"
print('4',S.upper()) # output ==> "SAGVEEK.TECHNOLOGIES"
print('5',S.split()) # output ==> ['Sagveek.Technologies']
#split function converts string into list
print('6',S.partition('k')) # output ==> ("Sagvee", "k", ".Technologies")
#partition function converts string into 3 tuple
print('7',S.partition('x')) # output ==> ('Sagveek.Technologies', '', '')
print('8',S.partition('.')) # output ==> ('Sagveek', '.', 'Technologies')
print('9',S.split('.')) # output ==> ['Sagveek', 'Technologies']
print('10',S.split('o')) # output ==> ['Sagveek.Techn', 'l', 'gies']
print('11',S.partition('o')) # output ==> ('Sagveek.Techn', 'o', 'logies')
print('12',S.split('e',maxsplit=3)) # output ==> ['Sagv', '', 'k.T', 'chnologies']
print('13',S.split('e',maxsplit=2)) # output ==> ['Sagv', '', 'k.Technologies']
print('14',S.split('e')) # output ==> ['Sagv', '', 'k.T', 'chnologi', 's']
S1="123456"
print('15',S1.swapcase()) # output ==> '123456'
print('16',list(S1)) # output ==> ['1', '2', '3', '4', '5', '6']
S2="My name is Yogesh Rakate"
print('17',S2.count('a')) # output ==> 3
print('18',list(S2)) # output ==> ['M', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'Y', 'o', 'g', 'e', 's', 'h', ' ', 'R', 'a', 'k', 'a', 't', 'e']
print('19',S2.title()) # output ==> My Name Is Yogesh Rakate
print('20',S2.split()) # output ==> ['My', 'name', 'is', 'Yogesh', 'Rakate']
print('21',S2.endswith('te')) # output ==> True
print('23',S2.endswith('Rakate')) # output ==> True
print('24',S2.startswith('te')) # output ==> False
print('25',S2.startswith('m')) # output ==> False
print('26',S2.startswith('M')) # output ==> True
print('27',S2.startswith('t',-2)) # output ==> True
print('28',S2.startswith('Y',11,17)) # output ==> True
print('29',S2.find('te')) # output ==> 22
print('30',S2.find('Y')) # output ==> 11
print('31',S2.find('a')) # output ==> 4
print('32',S2.find('a',5)) # output ==> 19
print('33',S2.find('MY')) # output ==> -1
print('34',S2.index('Y')) # output ==> 11
print('35',S2.index('M')) # output ==> 0
S3="YogeshRakate"
print('36',S3.isalnum()) # output ==> True
print('37',S3.isalpha()) # output ==> True
print('38',S3.isdigit()) # output ==> False
print('39',S3.isupper()) # output ==> False
print('40',S3.istitle()) # output ==> False
S4="Yogesh Rakate"
print('41',S4.istitle()) # output ==> True
print('42',S4.isalpha()) # output ==> False
S5="12345678"
print('43',S5.isdigit()) # output ==> True
print('44',S5.isalnum()) # output ==> True
print('45',S5.isnumeric()) # output ==> True
S6="12.34"
print('46',S6.isdigit()) # output ==> False
S7="   "
print('47',S7.isspace()) # output ==> True
S8="YOGESH RAKATE"
print('48',S8.isupper()) # output ==> True
print('49',S8.islower()) # output ==> False
S9="yogesh rakate"
print('50',S9.isupper()) # output ==> False
print('51',S9.islower()) # output ==> True
S10="     Yogesh Rakate      "
print('52',S10.lstrip()) # output ==> "Yogesh Rakate      "
print('53',S10.rstrip()) # output ==> "     Yogesh Rakate"
print('54',S10.strip()) # output ==> "Yogesh Rakate"
S11="aabca*#Yogesh Rakateaacdacb@#a"
print('55',S11.lstrip('abc*#')) # output ==> "Yogesh Rakateaacdacb@#a"
print('56',S11.rstrip('abc*#@')) # output ==> "aabca*#Yogesh Rakateaacd"
print('57',S11.strip('abc*#@d')) # output ==> "Yogesh Rakate"
S12="My name is Yogesh Rakate"
print('58',S12.replace('a','@')) # output ==> My n@me is Yogesh R@k@te
print('59',S12.replace('a','@',2)) # output ==> My n@me is Yogesh R@kate
print('60',S12.replace('e','#',2)) # output ==> My nam# is Yog#sh Rakate
name="Yogesh"
age=25
print('61',"The name is %s, age is %d"%(name, age)) # output ==> The name is Yogesh, age is 25
'''By mistake if you give command like
print("The name is %s, age is %d"%(age, name)) 
it will show type error'''
print('62',"The name is {}, age is {}".format(name, age)) # output ==> The name is Yogesh, age is 25
print('63',"The name is {}, age is {}".format(age, name)) # output ==> The name is 25, age is Yogesh
#In above line mistake is there still error won't be there and result will be printed
print('64',f"The name is {name}, age is {age}") # output ==> The name is Yogesh, age is 25
for i in range(1,11):
    print('65',f'The square of {i} is {i*i}')
L=['My', 'name', 'is', 'Yogesh', 'Rakate']
print('66',' '.join(L)) # output ==> "My name is Yogesh Rakate"
#join function converts list into string by joining list elements by space or mentioned element
print('67','.'.join(L)) # output ==> "My.name.is.Yogesh.Rakate"
print('68','@'.join(L)) # output ==> "My@name@is@Yogesh@Rakate"

