#1. Write a program which accepts a sequence of comma-separated numbers from console and generate a list.

a = input("Enter the number in comma seperated formated: ")

b = a.split(',')

output = [int(i) for i in b]
print(output)
print(type(output))



#1. Create the below pattern using nested for loop in Python.

#* 
#* * 
#* * * 
#* * * * 
#* * * * * 
#* * * * 
#* * * 
#* * 
#* 

given_range = 5
for i in range(0,given_range +1,1):
    print('* '* i)
for i in range(given_range -1,0,-1):
    print('* '* i)
