my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print(my_dict['Vasya'])
print(my_dict.get('Max'))
my_dict.update({'Kamila': 1981,
                'Artem': 1915})
my_dict.pop('Kamila')
print(my_dict['Artem'])
print(my_dict)

my_set = {1, 'Яблоко', 42.314, 1, 'Яблоко', 42.314}
print(my_set)
my_set.update({5, 6})
print(my_set.discard(5))
print(my_set)
