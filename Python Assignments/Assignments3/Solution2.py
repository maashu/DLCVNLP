#Implement List comprehensions to produce the following lists.
#Write List comprehensions to produce the following Lists






input_value1 = ['x','y','z']
output1 = [i*n for i in input_value for n in range(1,5)]
output2 = [i*n for n in range(1,5) for i in input_value ]
print(output1) ## # ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
print(output2) ## # ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']

input_list1 = [2,3,4]
output3 = [[i +n ] for i in input_list1 for n in range(0,3)]
print(output3)  # [[2], [3], [4], [3], [4], [5], [4], [5], [6]] 

input_list2 = [2,3,4,5]
output4 = [[(i +n) for n in range(0,4)] for i in input_list2]
print(output4) # # [[2, 3, 4, 5], [3, 4, 5, 6],[4, 5, 6, 7], [5, 6, 7, 8]]

input_list3 = [1,2,3]
output5 = [(i,n) for n in range(1,4) for i in input_list3]
print(output5) # # [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
