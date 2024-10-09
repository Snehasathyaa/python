List=input("Enter a list item ")
L=[]
for n in List:
    L.append(n)
print("Before swaping List\n",L)
L[0],L[-1]=L[-1],L[0]
print("After swaping List\n",L)
