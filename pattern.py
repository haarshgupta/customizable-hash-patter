#def funPatt(value):
    # for i in range (value-1):
    #     print("   |", end="")

value = int(input("Enter an number :"))

for i in range(value*2-1):#this much time it will work (to print rows)
    if i % 2 == 0:
        for j in range(value*2-1):#number of columns (   |   |   )
            if j % 2 ==0:
                print("   ",end="") 
            else:
                print("|",end="")
        print()
    else:
        for j in range(value*2-1):#number of columns (---|---|---)
            if j % 2 ==0:
                print("---",end="") 
            else:
                print("|",end="")
        print()




