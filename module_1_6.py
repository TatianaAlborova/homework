my_dict = {'Tatiana': 1999, 'Ivan': 1992}
print(my_dict)
print(my_dict['Ivan'])
print(my_dict.get('Mari'))
my_dict.update({'Sasha': 1987, 'Maxim':1995})
a = my_dict.pop('Tatiana')
print(a)
print(my_dict)
my_set = {2,2,3,5,5,True,'keys','keys'}
print(my_set)
my_set.add(7)
my_set.add(4.87)
my_set.discard(2)
print(my_set)