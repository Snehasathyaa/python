num = 5

for i in range(1, num + 1):
    for j in range(i):
        
        print("* " ,end=' ')
    print()

for i in range(num - 1, 0, -1):
    for j in range(i):
        print("* " ,end=' ')
    print()
