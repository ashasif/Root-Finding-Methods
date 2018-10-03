import math

sin=math.sin

e=math.e

def y(x):

    return x**2 - 6*x - 5

#  return x**3-x**2-26*x-24

#  return x*(sin(3*x)- 3*sin(3*x)

#  return 5*e**x -sin(x)-x**2

a=1

b=8


count=0

if y(a) * y(b) >0:

    print("change your input & try again")

else:

    while (abs(b-a)>1e-10):

        c=(a+b)/2

        if y(a) * y(c) > 0:

            a=c

        else:

            b=c

        count+=1

        print(" c is ",c, "and iteration no", count)


print("The Root is")

print(c)

print("Total iteration is")

print(count)
