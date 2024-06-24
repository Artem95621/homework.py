my_dict = {'Артем': 1995, 'Николай': 1994, 'Ангелина': 1997}
print(my_dict)
print(my_dict['Артем'])
print(my_dict.get('Олег'))
my_dict.update({'Игорь': 1993, 'Артур': 2000})
a = my_dict.pop('Николай')
print(a)
print(my_dict)

my_set = {1, 2, 3.2, 3, 2, 2, 'donut', 23.21, 3, 'donut', 3.2, 23.21}
print(my_set)
my_set.add(4)
my_set.add(4.76)
my_set.discard(3)
print(my_set)