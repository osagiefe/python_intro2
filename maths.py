#print first number

print("enter first number")

firstnumber=float(input())

print("enter second number")

secondnumber=float(input())

print("enter third number")

thirdnumber=float(input())

total=firstnumber+secondnumber+thirdnumber

print("total result " + str(total))

if total>200:

    print("yes it is grearter than 200")

    a=total*50

    print("this is the final result",a)

else:

    

    print("no it is less than 200")

    b=total*3

    print("this is the final result",b)