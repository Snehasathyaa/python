def input_integer_list(prompt):
    return list(map(int, input(prompt).split()))

list1 = input_integer_list("Enter the first list of integers : ")
list2 = input_integer_list("Enter the second list of integers  : ")

same_length = len(list1) == len(list2)

same_sum = sum(list1) == sum(list2)

common_values = set(list1) & set(list2)
print("Are the lists of the same length ", same_length)
print("Do the lists sum to the same value ", same_sum)
if common_values:
    print("Common values in both lists: ", common_values)
else:
    print("There are no common values in both lists.")
