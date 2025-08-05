import math
def add(x,y):
     return x + y
def subtract(x,y):
     return x - y
def multiply(x,y):
     return x*y
def division(x,y):
     if y==0:
         return 'Error: ZeroDivisionError!'
     return x/y
def add_multi():
    x=int(input('enter a number: '))
    sum=0
    while x!=0:
        sum=sum+x
        x=int(input('enter a number : '))
    print('Result=',sum)
def multiply_multi():
    x=int(input('enter a number: '))
    multly=1
    while x!=1:
        multly=multly * x
        x=int(input('enter a number:'))
    print('result/multiplication:',multly)
def power(x,y):
    return x**y
def squar(x):
    return math.sqrt(x)
def sine(x):
    return math.sin(math.radians(x))
def cosine(x):
    return math.cos(math.radians(x))
def tangent(x):
    return math.tan(math.radians(x))
def logorithm(x):
    return math.log(x, base=10)
def factorial(x):
    return math.factorial(x)
def multi_table(x):
    x=int(input('enter a number: '))
    for i in range(1,11):
        c=x*i
        print(x,'*',i,'=',c)
def fibonacci(x):
    #15
    # x=int(input('enter a number: '))
    a=0
    b=1
    count=0
    if x>1:
        print('Fibonacci sequence: ')
        while count<x:
            print(a,end='  ')
            c=a+b
            a=b
            b=c 
            count=count+1
            
def calculator():

    print('*******************calculator********************'.upper())
    print('select operation: ')
    print('\n1. Addition(two num)')
    print('2. subtraction')
    print('3. multiplication')
    print('4. division')
    print('5. Addition(user enter until 0)')
    print('6. multiply multiple numbers(until user enter)')
    print('7. Power')
    print('8. square root')
    print('9. sine')
    print('10. cosine')
    print('11. Tangent')
    print('12. logorithm')
    print('13. Factorial')
    print('14. Multipliction table')
    print('15. Fibonacci')
    print('*************************************************')
    
    choice=input('\nselect choice operations:  ')
    
    if choice in ['1','2','3','4','7']:
        n1=int(input('enter n1 value:'))
        n2=int(input('enter n2 value:'))
        if choice=='1':
            print('Result:',add(n1,n2))
        elif choice=='2':
            print("Result:", subtract(n1,n2))
        elif choice=='3':
            print('Result:',multiply(n1, n2))
        elif choice=='4':
            print('Result:',division(n1,n2))
        elif choice=='7':
            print('Result:',power(n1, n2))
      
    elif choice in ['5','6']:
        if choice=='5':
            add_multi()
        elif choice=='6':
            multiply_multi()
        
    elif choice in ['8','9','10','11','12','13','14','15']:
        n3=int(input('enter n3 value:'))
        if choice=='8':
            print('Result;', squar(n3))
        elif choice=='9':
            print('Result:',sine(n3))
        elif choice=='10':
            print('Result:', cosine(n3))
        elif choice=='11':
            print('Result:',tangent(n3))
        elif choice=='12':
            print('Result:',logorithm(n3))
        elif choice=='13':
            print('Result:',factorial(n3))
        elif choice=='14':
            print('Result:', multi_table(n3))
        elif choice=='15':
            print('Result:',fibonacci(n3))
   
    else:
        print('that is not a valid choice.')

calculator()
        

        
