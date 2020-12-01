# 1.2 Write a Python program to implement your own myfilter() function which works exactly
# like Python's built-in function filter()

def myfilter(input):
    '''This function will filter numbers from list which are multiples of 5 '''
    x = []
    for i in input:
        if (i%5 ==0):
            x.append(i) 
    return x      
input_list = [3,6,9,10,12,15,18,20]
print(myfilter(input_list))

    
