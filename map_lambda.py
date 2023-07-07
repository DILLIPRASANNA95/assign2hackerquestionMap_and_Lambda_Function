def fib(n):
    a=0
    b=1
  
    l=[]
    l.append(a)
    l.append(b)
    for i in range(2,n):
      if True:
        c=a+b
        a=b
        b=c
      l.append(c) 
    result = []
    for i in l:
      result.append(i*i*i)
    
    return result
  
    
n=int(input())
fib(n)


lst = []
cube = lambda x: x**3 
    # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    for x in range(n):
        if x == 0 or x == 1:
           lst.append(x)
        else:
            lst.append(lst[-2]+lst[-1])
    return lst
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))