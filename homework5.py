immutable_var = 1,2,3,4,5
print(immutable_var)
#кортеж изменить нельзя, можно добавить лист, лист изменять можно
immutable_var = ([1,2,3], 4,5)
print(immutable_var)
immutable_var [0][0]= 6
print(immutable_var)
mutable_list = [1,2,3]
mutable_list [0]=4
print(mutable_list)