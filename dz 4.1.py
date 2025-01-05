my_list = [0,9,0,8,0,6,9,0,9,8,9,0]
number_zero = 0

zero = my_list.count(number_zero)
my_list = [i for i in my_list if i != number_zero]
my_list.extend([number_zero] * zero)
print(my_list)
