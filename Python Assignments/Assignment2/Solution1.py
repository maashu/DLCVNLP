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
