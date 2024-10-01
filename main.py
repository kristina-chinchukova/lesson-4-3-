def print_params(a = 1, b = 'строка', c = True) :
    print(a, b, c)

values_list=[1,7,'87']
values_dict={'a' : 78, 'b' : False , 'c' : '37'}
values_list_2=['kristina', 22]

print_params(*values_list_2, 42)
print_params(*values_list)
print_params(**values_dict)
print_params(a=87, c='max')
print_params(b = 25)
print_params(c = [1,2,3])