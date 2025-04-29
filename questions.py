# For REVERSE A NUMBER 
num=int(input("enter the num"))
revnum=0
while(num>0):
    digit=num%10
    revnum=revnum*10+digit
    num=num//10

print(num)
print(revnum)

# CHECK A NUMBER IS PALINDROME OR NOT 

def ispalindrome(num):
    temp=num
    revnum=0
    while(num>0):
        digit=num%10
        revnum=revnum*10+digit
        num=num//10
        
    if(temp==revnum):
        return True
    else:
        return False
print(ispalindrome(121))

# ADDING A NUMBER USING LAMBDA FUNCTION
def add(a,b):
    return a+b

x=lambda a,b : a+b
print(x(5,6))
print(add(5,6))


# CALCULATE A AREA OF SQ. USING LAMBDA FUNCTION 
def area (l,b):
    return l*b
x=lambda l,b: l*b
print(area (6,7))
