#creating n empty list
my_list =[]

#Append elements to my list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert 15 to the second position
my_list.insert(1,15)

#Extend my_list with another list
my_list.extend([50, 60, 70])

#remove the last element
my_list.pop()

#sort my_list in ascending order
my_list.sort()

#find and print the index of the value 30
index_of_30 = my_list.index(30)
print('index of 30:', index_of_30)

#final output of  my_list
print('Final my_list :', my_list)