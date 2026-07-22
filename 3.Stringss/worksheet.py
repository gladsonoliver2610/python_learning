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