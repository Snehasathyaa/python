count = int(input("How much colors :"))
colors=[]
for i in range(count):
    colors.append(input("Color : "))
print("List of colours are:",colors)
print("First and last colour are ",[colors[0],colors[-1]])
