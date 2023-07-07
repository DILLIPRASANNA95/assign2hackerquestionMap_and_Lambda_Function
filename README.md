# assign2hackerquestionMap_and_Lambda_Function
https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
Let's learn some new Python concepts! You have to generate a list of the first  fibonacci numbers,  being the first number. Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

Concept

The map() function applies a function to every member of an iterable and returns the result. It takes two parameters: first, the function that is to be applied and secondly, the iterables.
Let's say you are given a list of names, and you have to print a list that contains the length of each name.

>> print (list(map(len, ['Tina', 'Raj', 'Tom'])))  
[4, 3, 3]  
Lambda is a single expression anonymous function often used as an inline function. In simple words, it is a function that has only one line in its body. It proves very handy in functional and GUI programming.

>> sum = lambda a, b, c: a + b + c
>> sum(1, 2, 3)
6
Note:

Lambda functions cannot use the return statement and can only have a single expression. Unlike def, which creates a function and assigns it a name, lambda creates a function and returns the function itself. Lambda can be used inside lists and dictionaries.

Input Format

One line of input: an integer .

Constraints


Output Format

A list on a single line containing the cubes of the first  fibonacci numbers.

Sample Input

5
Sample Output

[0, 1, 1, 8, 27]
Explanation

The first 5 fibonacci numbers are[0,1,1,2,3] , and their cubes are[0,1,1,8,27] .
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

    Input (stdin)
5
Expected Output
[0, 1, 1, 8, 27]
