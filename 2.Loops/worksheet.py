# 2.a
#1
# num=int(input("enter a number:"))
# if num%2==0:
#     print("even")
# else:
#     print("odd")

# 2
# marks=int(input("enter your marks:"))
# if marks>=40:
#     print("pass")
# else:
#     print("fail")

#3
# marks=int(input("enter your marks:"))
# if marks >=90:
#     print("A")
# elif marks >=80:
#     print("B")
# elif marks >=70:
#     print("C")
# elif marks >=60:
#     print("D")
# else :
#     print("F")

# 4
# num=int(input("type your number (1 to 7):"))
# if num ==7:
#     print("saturday")
# elif num==6:
#     print("friday")
# elif num==5:
#     print("thursday")
# elif num==4:
#     print("wednesday")
# elif num==3:
#     print("tuesday")
# elif num==2:
#     print("monday")
# elif num==1:
#     print("sunday")
# else :
#     print("invalid")

# 5
# age=int(input("enter your age:"))
# if age >=18:
#     print("your are not eligible")
# elif citizenship == "yes":
#     print("you are eligible")
# elif  :
# print("you are not eligible because you are not a indian")
# else :
# print("you are noteligible to vote because you are under 18")

# 5
# age=int(input("Enter your age:"))
# citizenship=input("Are you an Indian citizen?: ")
# if age >= 18:
#     if citizenship=="yes":
#         print("You are eligible to vote in India.")
#     else:
#         print("You are not eligible to vote because you are not an Indian citizen.")
# else:
#     print("You are not eligible to vote because you are under 18 years of age.")

# 6
# amount=int(input("enter your amount to be withdrawn:"))
# balance=10000
# pin=int(input("enter your pin:"))
# if balance>=amount:
#     if pin==2610:
#         print("withdrawal done")
#     else :
#         print("incorrect pin")
# else:
#     print("insufficient balance")

# 6
# amount=int(input("enter your amount to be withdrawn:"))
# balance=10000
# pin=int(input("enter your pin:"))
# if balance>=amount:
#     if pin==2610:
#         print("withdrawal done")
#         newbal=balance-amount
#         print("your new balance is:", newbal)
#     else :
#         print("incorrect pin")
# else:
#     print("insufficient balance")

# 2.b
# 1
# for i in range(1,11):
#     print(i)

# 2
# num=int(input("enter a number:"))
# for i in range(1,11):
#     print(f"{num} * {i} = {num*i}")

# 3
# num=int(input("enter a number:"))
# for i in range(1,21):
#     print(i)
#     if i==num==13:
#         break
    
# 4
# for i in range(1,21):
#     if i%3==0:
#        continue
#     print(i)

# 5
# N=int(input("enter a positive integer N:"))
# for i in range(1,N+1):
#     print(i)

#  2.c
# 1
# secert=int(input("enter the secret number:"))
# match secert:
#     case 7:
#         print("congratulations! you guessed it")
#     case _:
#         print("Try again!")

# 2
# x=1
# even=0
# odd=0
# while x<=10:
#     n=int(input("enter an integer:"))
#     if n%2==0:
#         even+=1
#     else:
#         odd+=1
#     x+=1
# print("number of even numbers:",even) 
# print("number of odd numbers:",odd)   

# 3
# n=int(input("enter a positive integer:"))
# x=0
# while n>0:
#     x+=1
#     n=n//10
# print("number of digits:",x)

# 4
# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# operator=input("enter a operator:")
# match operator:
#     case "+":
#         print("result=",a+b)
#     case "-":
#         print("result=",a-b)
#     case "*":
#         print("result=",a*b)
#     case "/":
#         print("result=",a/b)
#     case _:
#         print("enter a valid number!")