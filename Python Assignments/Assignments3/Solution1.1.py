# 1.1 Write a Python Program to implement your own myreduce() function which works exactly
# like Python's built-in function reduce()

def myreduce(iterable,initializer=None):    
    '''This function will return the sum of the list'''
    if initializer is None:
        return sum(iterable)
    else:
        return sum(iterable) + initializer

input_list = [10,20,30,40,50,60]
print(myreduce(input_list,10))
