integer1= input("enter first number:\n")
integer2=input("enter second number\n")

integer1=int(integer1)
integer2=int(integer2)
sum =integer1+integer2
print("sum is ",sum)


integer1 =input("enter first number: ")
integer2= input("enter second number: ")
integer1 = int (integer1)
integer2 = int (integer2)
sum = integer1+integer2

print(id(integer1), type(integer1), integer1)
print(id(integer2), type(integer2), integer2)
print(id(sum), type(sum), sum)

print(integer2/integer1)
print(integer2**integer1)
print(integer2%integer1)

print(3//5)  #floor division.
# when using double slash ensure
# that numbers are in their floating
# forms before manipulation
print(3/5)    #real division
print(3.0/5.0)    #real division
print(3.0/5)   #real division
