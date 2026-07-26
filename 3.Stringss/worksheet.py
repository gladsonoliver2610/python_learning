# 3.a
# 1
# a="hello world"
# print("original string:",a)
# print("uppercase",a.upper())
# print("lowercase",a.lower())
# print("capitalize",a.capitalize())
# print("title",a.title())
# print("swapcase",a.swapcase())
# print("casefold",a.casefold())
# print("find 'world'",a.find("world"))
# print("rfind",a.rfind("world"))
# print("index",a.index("hello"))
# print("split",a.split())
# print("starts with",a.startswith("world"))
# print("ends with",a.endswith("hello"))
# print("isalpha",a.isalpha())

# 2
# name=input("enter your name:")
# vowels=["a","e","i","o","u"]
# sum=0
# for i in name:
#     if i in vowels:
#         sum+=1
# print(f"the vowels are ",sum) 

# 3
# name=input("enter a name")
# rev=name[::-1]
# print(rev)

# 4
# name="Gladson"
# lower=upper=0
# for i in name:
#     if i.islower():
#         lower+=1
#     elif i.isupper():
#         upper+=1
# print("lowercase letters are:",lower)
# print("uppercase letters are:",upper)

# 5
# name="Gladsaaaaon"
# ch=["a"]
# count=0
# for i in name:
#     if i in ch:
#         count+=1
# print("count=",count)   

# 6
# user=input("enter a string:")
# if user==user[::-1]:
#     print("it is a pallindrome,",user)
# else:
#     print("it is not a pallindrome,",user)  

# 7
# name=input("enter a sentence:")
# words=name.split()
# print("Number of words:",len(words))   

# 8
# longest=" "
# text="Hello Gladson"
# words=text.split()
# for i in words:
#     if len(i)>len(longest):
#         longest=i
# print(longest)

# 9
# input1=input("enter first string:")
# input2=input("enter second string:")
# if input1[-3:]==input2[-3:]:
#     print("two strings end with the same three characters")
# else:
#     print("two strings dosnt end with the same three characters")

# 10
# input1=input("enter a string:")
# input2=input("enter a another string:")
# if input1[::-1]==input2:
#     print("yes it is the reverse of another")
# else:
#     print("no it is not the reverse of another")

# 3.b
# 1
# string_fruit=["apple","banana","orange"]
# print("string:",string_fruit)
# integer=[10,20,30]
# print("integer:",integer)
# mixed=[10,"apple",3.14,]
# print("mixed:",mixed)
# nexted=[[1,2],[3,4],[5,6]]
# print("nexted:",nexted)
# 2
# a=[[1,2],
#    [3,4]]
# b=[[5,6],
#    [7,8]]
# c=[[0,0],[0,0]]
# for i in range(2):
#     for j in range(2):
#         for k in range(2):
#             c[i][j] += a[i][k] * b[k][j]
# print("answer:")
# for row in c:
#     print(row)
# 4
# numbers=[]
# n=int(input("enter number of element:"))
# for i in range(n):
#     num=int(input("enter number:"))
#     numbers.append(num)
# print("list:", numbers)
# print("maximum number:", max(numbers))
# 5
# student1=[80,75,70]
# student2=[75,70,80]
# student3=[70,80,75]
# first=[student1[0],student2[0],student3[0]]
# print("marks of the first subjects:",first)
# 6
# number=[12,45,7,89,23]
# largest=number[0]
# for num in number:
#     if num > largest:
#         largest=num
# print("largest numbers:", largest)
# 7
# numbers=[10,15,22,33,44,51]
# even=0
# odd=0
# for num in numbers:
#     if num % 2==0:
#         even+=1
#     else:
#         odd+=1
# print("even numbers:", even)
# print("odd numbers:", odd)
# 8
# marks=[80,75,90,85,70]
# total=0
# for mark in marks:
#     total+=mark
# average=total/len(marks)
# print("sum:", total)
# print("average:", average)
# 9
# numbers=[2,4,2,5,2,7,8]
# search=4
# count=0
# for num in numbers:
#     if num == search:
#          count+=1
# print(search, "append", count, "time")