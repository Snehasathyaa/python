string=input("Enter a string : ")
vowels=["a","e","i","o","u","A","E","I","O","U"]
indices= ""
for i in string:
    if i in vowels:
        indices+=i
print("vowels in",string,"is",indices)
    
