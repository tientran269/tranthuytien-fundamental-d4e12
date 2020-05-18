a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))

delta = b**2 - 4*a*c

if delta < 0:
    print('zero root')
elif delta == 0:
    x= -b / 2**a
    print('co nghiem kep',x)
else:
    x_1 = (-b + delta**(1/2)) / 2*a
    x_2 = (-b - delta**(1/2)) / 2*a
    print('x1=',x_1)
    print('x2=',x_2)