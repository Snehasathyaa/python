string=input("Enter string: ")
word=input("Enter the word: ")
a=[]
count=0
a=string.split(" ")
for i in range(0,len(a)):
    if(word==a[i]):
        count=count+1
print("count of the word",word," is : ",count)

