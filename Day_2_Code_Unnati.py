#!/usr/bin/env python
# coding: utf-8

# In[3]:


num = 5
if num > 0:
    print(num, "is a Positive Number")
print("This statement is True...")


# In[4]:


num = 5
if num > 0:
    print(num, "is a Positive Number")
else:
    print("Negative Number")


# In[5]:


num = 5
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive Number")
else:
    print("Negative Number")


# In[6]:


a=b=c=1
print(id(a))
print(id(b))
print(id(c))


# # 10 - Fibonacci

# In[7]:


#WAPP to print fibonnaci series using recusrsion
def fibonnaci(n):
   if n <= 1:
       return n
   else:
       return(fibonnaci(n-2) + fibonnaci(n-1))

n = int(input("Enter number of terms you want?"))
print("Fibonacci sequence:")
for i in range(n):
  print(fibonnaci(i))


# # 7 - Sum of digits

# In[10]:


#WAPP using recursion to find sum of all digits present in a non negative number
def sum_digit( n ): 
    if n == 0: 
        return 0
    else:
      return (n % 10 + sum_digit(int(n // 10)))  
num = 1024
result = sum_digit(num) 
print("Sum of digits in",num,"is", result)


# # 9 - Palindrome

# In[12]:


#palindrome using recursion
def Rec(st,n,p) :
    if (st[n] != st[p]) : 
        return False 
    if (n < p + 1) : 
        return Rec(st, n + 1, p - 1);
    else:
      return True
  
def isPalindrome(st) : 
    n = len(st)
    if (n == 0) : 
        return True
    else:
      return Rec(string,0, n - 1); 
      
string=input("Enter the number:")
if (isPalindrome(string)) : 
    print("It is a palindrome") 
else : 
    print ("It is not a palindrome")


# # 8 - Reverse Number

# In[16]:


def rev_num(n, d): 
    if n == 0: 
        return d
    else:
        d *= 10
        d += n % 10
        return (rev_num(n // 10, d))

num = 1024
d=0
result = rev_num(num, d) 
print("Reverse of ",num,"is", result)


# # 4 - Case Study of Tuple

# In[15]:


t = (1, 2, 3,4 ,55,67 ,78 ,67.43, 2,46,37, 3)
t1 = (1,2 ,34,52,546 ,56 ,47,56,35, 72)
print(max(t))
print(min(t))
print(t+t1)
t2 = t
print("Original tuple", t)
print("Duplicate tuple", t2)
print(t[5:])
print(type(list(t)))
if t>t1:
    print("t > t1")
else:
    print("t !> t1")
print(list(t))
print(set(t))


# # 1 - Temperature Conversion

# In[17]:


Fahrenheit = int(input("Enter degree in Fahrenheit : "))
celsius = (Fahrenheit-32)*5/9
print(celsius)


# # 2 - Exchange of Variables

# In[18]:


num1 = 10
num2 = 24
print("Value of num1 before swap : ",num1)
print("Value of num2 before swap : ",num2)
num3 = num1
num1 = num2
num2 = num3
print("Value of num1 after swap : ",num1)
print("Value of num1 after swap : ",num2)


# # 6 - Factorial

# In[19]:


num = int(input("Enter a number: "))

factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# # 3 - Distance of two points

# In[ ]:


x1=int(input("enter x1 : "))
x2=int(input("enter x2 : "))
y1=int(input("enter y1 : "))
y2=int(input("enter y2 : "))
result= ((x2-x1)**2 + (y2-y1)**2)**.5
print("distance between",(x1,x2),"and",(y1,y2),"is : ",result)


# # 5 - Square root of two numbers

# In[20]:


from math import sqrt
print(sqrt(25))
print(sqrt(36))


# # 11 - Prime numbers in range

# In[13]:


lower = int(input("Enter the starting number of range  : "))
upper = int(input("Enter the ending number of range : "))
print("Prime numbers between", lower, "and", upper, "are:",end=" ")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num,end=" ")


# # 12 - Max of three nos.

# In[8]:


x=int(input("enter first number:"))
y=int(input("enter second number:"))
z=int(input("enter third number:"))
if x>y:
  if x>z:
    print("x is max.")
  else:
    print("z is max.")
else:
  if y>z:
    print("y is max.")
  else:
    print("z is max.")


# # 13 - Calc

# In[2]:


loop = 1
choice = 0
while loop == 1:
  print("Choose the opertion you want to perform:")
  print("1) Addition")
  print("2) Subtraction")
  print("3) Multiplication")
  print("4) Division")
  print("5) Quit calculator")
  choice =int(input("choose your option: "))
  try:
    if choice == 1:
      add1 =int(input("add this: "))
      add2= int(input("to this: "))
      print(add1, "+", add2, "=", add1+ add2)
    elif choice == 2:
      sub1 = int(input("Subtract this "))
      sub2 =int(input("from this"))
      print(sub1, "-", sub2, "=", sub1 - sub2)
    elif choice == 3:
      mul1 = int(input("Multiply this: "))
      mul2 = int(input("with this: "))
      print(mul1, "x", mul2, "=", mul1 * mul2)
    elif choice == 4:
      div1 = int(input("Divide this: "))
      div2 = int(input("by this: "))
      if div2 == 0:
        print("Error! Cannot divide by zero! ")
      else:
        print(div1, "/", div2, "=", div1 / div2)
    elif choice == 5:
      loop = 0
  except ValueError:
    print("Please enter 1, 2, 3, 4 or 5.")

