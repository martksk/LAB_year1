def checkmax():
    checkmax = ("The maximum number entered is "+str(max(numlist)))
    return checkmax
def checkmin():   
    checkmin = ("The minimum number entered is "+str(min(numlist)))
    return checkmin



ele = int(input("Enter number of elements : "))
numlist = []
for i in range (0,ele):
    num = int(input())
    numlist.append(num)
print("The entered list is "+str(numlist))
print(checkmax())
print(checkmin())
