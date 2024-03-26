

my_dict = {0:[8,5,2],3:[0,3,6],1:[0,3,6],2:[8,5,2]}
result = [(key, value) for key, values in my_dict.items() for value in values]
print(result)