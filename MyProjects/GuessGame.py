
num=9;




number=input("guess the number")
number=int(number)
if(number==num):
    print("true")

elif(number!=num):print("false")

while(number!=num):
    # print("false")
    number=input("guess the number")
    number=int(number)
    if(number==num):print("true")
