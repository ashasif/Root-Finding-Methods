import sympy as sym
import matplotlib.pyplot as plt
a=[]
b=[]
c=[]

i=-20
def f(x):
    return x**2-5*x-6


for i in range (-20,21):
    x=i
    f1 = 2*x - 5
    tol = x 
    y = x - (f(x)/f1)
    count = 0
    #print(i) 
    while(abs(tol)>10**(-5)):
        y = x - (f(x)/f1)
        #print(y) 
        tol = y - x
        x=y
        count+=1
        #print("y:",y)
        if(abs(y) > 10**2):
            print("y is too big for i=",i)
            break
        if(count == 100):
               print('no output or input',i)
               break
        #else:
         #   i = i + 1
    #print("y:",y)
    #print("i:",i)
    print("for i is ", i, " The Root is ", y , "Total iteration",count)
    a.append(i)
    b.append(y)
    c.append(count)


plt.plot(a,b)
plt.show()
plt.plot(a,c)
plt.show()

