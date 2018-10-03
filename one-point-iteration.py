def g(x):
    return (x+6)**0.5

x=0.5
count=0

print(g(x))

while(abs(g(x)-x>0.0001)):
    x=g(x)
    count+=1
    print('x is ',x)
print('the root is ' , x )
print('No. of steps is', count)
