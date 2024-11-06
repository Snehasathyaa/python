
list = input("Enter numbers : ")


List = [int(num) for num in list.split()]
print("list is:",List)

total = sum(List)

print("The sum of the list is:", total)
