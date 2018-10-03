import math

sin=math.sin

e=math.e

def y(x):

        return x*math.sin(x*3.1416/180)-3*math.sin(x*3.1416/180)

    #   return x**2 - 6*x - 5

    #  return x**3-x**2-26*x-24

    #  return x*(sin(3*x)- 3*sin(3*x)

    #  return 5*e**x -sin(x)-x**2

a=float(input('a?'))

b=float(input('b?'))

count=0

if (y(a) * y(b) >0):


        print("change your input & try again")
else:
    while (abs(b-a)>=0.00000001):
        c = (a*(y(b))-b*(y(a)))/(y(b)-y(a))
        if count==100000000:

              break



        elif y(a) * y(b) ==0:

             break


        elif( y(a) * y(c)) >0:

             a=c
        else:

             b=c

      



        count+=1

       

        print (c ,"iteration", count)

print("The root is",c)

print('No.of steps is',count)
