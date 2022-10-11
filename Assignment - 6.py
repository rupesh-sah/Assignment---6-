'''            Assignment - 6 Full Stack Web Development using Python MySirG

                        Decision Control'''

# (Q.1) Write a python script to check whether a given number is positive or non-positive.
print("negative number" if int(input('Enter the number : '))<0 else 'Positive number')

#(Q.2) Write a python script to check whether a given number is divisible by 5 or not
print("This Number is divisible by 5" if int(input("Enter the number : "))%5==0 else "Number is not divisible by 5")

# (Q.3) Write a python script to check whether a given number is even or odd
print("This is Odd number : " if int(input("plese enter the number "))%2 else "This is Even number")

# (Q.4) Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.
print('enter the two number ')
a,b = int(input()),int(input())
print(a if a>b else b)

# (Q.5) Write a python script to print two given words in dictionary order
print('Enter The two words ')
y,z = input(),input()
print((z,y) if y>z else (y,z))

# (Q.6) Write a python script to check whether a given number is a three digit number or not.
num1 = int(input('Enter the number : '))
if 99<num1<1000:
    print("This number is three digit number")
else:
    print('Not a three digit number ')

#(Q.7) Write a python script to check whether a given number is positive, negative or zero.
x = int(input('Enter the number : '))
if x > 0:
    print("This is Positive number")
elif x==0:
    print("This is Zero number")
else:
    print("This is Negative Number")

#(Q.8) Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots.
print("Enter value of a,b and c of a quadratic equation:")
o,p,q = int(input()),int(input()), int(input())
r = p**2-4*o*q
if r>0:
    print("Real and distinct roots")
elif r==0:
    print('Real and equal roots')
else:
    print("imaginary roots")

#(Q.9) Write a python script to check whether a given year is a leap year or not.
print('Enter year number')
year = int(input())
if year%400==0 or year%100!=0 and year%4==0:
    print("Leap year")
else:
    print("Non Leap Year")

# (Q.10) Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.
print("Enter Three numbers ")
a,b,c = int(input()), int(input()), int(input())
(a if a>c else c) if a>b else (b if b>c else c)

# (Q.11) Write a python script to take the month value in numeric format and display the number of days in it.

print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ")

if month_name == "February":
	print("No. of days: 28/29 days")
elif month_name in ("April", "June", "September", "November"):
	print("No. of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
	print("No. of days: 31 day")
else:
	print("Wrong month name") 

# (Q.12) Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part

#Initialize a complex number
cn = complex(2,3)
print("Complex Number: ",cn)
print("Complex Number - Real part: ",cn.real)
print("Complex Number - Imaginary part: ",cn.imag)
