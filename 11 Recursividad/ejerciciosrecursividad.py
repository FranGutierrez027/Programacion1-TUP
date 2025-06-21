def sum_list(lst):
    if len(lst) == 0:
        return 0 
    else:
        return lst[0] + sum_list(lst[1:])
    
lista=[1,2,3,4,5]

print(f'El valor total de la lista es {sum_list(lista)}')
    
