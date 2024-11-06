list=input("Enter the list : ")
List = [int(n) for n in list.split(' ')]
print("The list is \n",List)

while True:
    print("\n Menu")
    print("1. Greater and Smaller number")
    print("2.Sorting")
    print("3.Even number")
    print("4.Exit")
    choice=input("Enter your coice : ")
    if choice =='1':
        print(" The greatest number is: ",max(List))
        print("\n The smallest number is: ",min(List))
    elif choice =='2':
        print("\n The sorted list is: ",sorted(List))   
    elif choice =='3':
         even = [n for n in List if n % 2 == 0]
         print("The even numbers from the list are:", even)
    elif choice =='4':
        print ("Exit")
        break
    else:
        print("\n Invalid choice")
