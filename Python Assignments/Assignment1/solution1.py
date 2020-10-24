# 1 PROBLEM STATEMENT
# Program to find the number b/w 2000,3200 both included that are divisibe by 7 but not multiple of 5

# # Initialize List
l = list()
LOWER_RANGE = 2000
UPPER_RANGE = 3200
for i in range (LOWER_RANGE,UPPER_RANGE+1):
    if (i%7 == 0 and i%5 != 0):
        l.append(i)
print(l)
