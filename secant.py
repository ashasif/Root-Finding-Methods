import sympy as sym
import matplotlib.pyplot as plt
a=[]
b=[]
c=[]



def y(x):

    return  (x**2-5*x-6)
    #  return x**3-x**2-26*x-24

    #  return x*(sin(3*x)- 3*sin(3*x)

    #  return 5*e**x -sin(x)-x**2

for i in range (-20,21):
    x1=i
    x0=x1-1
    count=0
    while (abs(x1-x0))>0.00000000000000001:
        p=(y(x1)-y(x0))
        if(p==0):
            break
        else:
            x2=x1-((x1-x0)*y(x1)/(y(x1)-y(x0)))
            x0=x1
            x1=x2
        count+=1
        #print('x2 is',x2)
    print('for i=',i,'The root is ',x2)
    print('steps taken',count)
    #print('i is ',i)
    #print('y is',y)
    #print('steps are',count)

    a.append(i)
    b.append(x2)
    c.append(count)

print('a[]=',a)
print('b[]=',b)
print(c)

plt.plot(a,b)
plt.show()
plt.plot(a,c)
plt.show()

