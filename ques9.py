decimal=int(input("Enter number :"))
binary=0
ctr=0
temp=decimal
while(temp>0):
    binary=((temp%2)*(10**ctr))+binary
    temp=int(temp/2)
    ctr+=1
print("Binary of {x} is: {y}".format(x=decimal,y=binary))

