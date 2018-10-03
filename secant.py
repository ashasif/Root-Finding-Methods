def y(x):

    return  x**2 - 5*x + 6

    #  return x**3-x**2-26*x-24

    #  return x*(sin(3*x)- 3*sin(3*x)

    #  return 5*e**x -sin(x)-x**2

x1=int(input('x1?'))

x0=x1-1

count=0

print(x0)

print(x1)


while (abs(x1-x0))>0.00000000000000001:

    x2=x1-((x1-x0)*y(x1)/(y(x1)-y(x0)))

    x0=x1

    x1=x2

    count+=1

    print('x2 is',x2)


print('The root is ',x2)

print('steps taken',count)
