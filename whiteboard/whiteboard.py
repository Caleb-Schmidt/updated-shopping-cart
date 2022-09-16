# Define a function that removes duplicates 
# from an array of numbers and returns 
# it as a result.

# The order of the sequence has 
# to stay the same.

# ex1: ([1]) == [1]
# ex2: ([1, 2]) == [1, 2]
# ex3: ([100,50,76,1,1000,100,50,76,1,999,77,52,100]) 
# == 
# [100,50,76,1,1000,999,77,52]


# Set up your function
# figure out if item is already in list
# if it's not, put into new list
# if it is, continue to next item
# print list once you're done sorting through the list inputed


# with nested loop
def simplify(a_list):
    new_list = []
    for item in a_list:
        if item not in new_list:
            new_list.append(item)
    return new_list

# without nested loop
def simple(a_list):
    new_dict = {}
    new_list = []
    for item in a_list:
        if item not in new_dict:
            new_dict[item] = 1
            new_list.append(item)
        else:
            new_dict[item] += 1
    
    return new_list

print(simple([100,50,76,1,1000,100,50,76,1,999,77,52,100]))






    
