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
# mixed=[10,"apple",3.14,[1,2],[3,4]]
# print("mixed:",mixed[3][0])
# 2
# a=[[1,2],[3,4]]
# b=[[5,6],[7,8]]
# c=[[0,0],[0,0]]
# for i in range(2):
#     for j in range(2):
#         c[i][j] += a[i][j] * b[i][j]
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
# largest=max(student1[1],student2[2],student3[0])
# print("mark of the topper student:",largest)
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
# search=2
# count=0
# for num in numbers:
#     if num == search:
#          count+=1
# print("searching:",search, "| repeated:",count,"times")
# 10
# numbers=[12,45,7,89,23]
# largest=numbers[0]
# secondlargest=numbers[0]
# for i in numbers:
#     if i>largest:
#         largest=i
# for i in numbers:
#     if i>secondlargest and i!=largest:
#         secondlargest=i
# print("second largest:",secondlargest)
# 3.c
# 1
# inventory={'pen':50,'book':20,'pencil':100}
# inventory['note']=45
# inventory.pop('pen')
# print(inventory)
# 2
# marks={'raja':95,'john':45,'mary':78,'david':30}
# count=0
# for mark in marks.values():
#     if mark>=50:
#         count+=1
# print("number of students passed:",count)
# 3
# items=['apple','banana','apple','orange','banana','apple']
# freq={}
# for num in items:
#     if num in freq:
#         freq[num]+=1
#     else:
#         freq[num]=1
# print(freq)
# 4
# python_students={"bobby","john","mary","david"}
# java_students={"mary","david","sam","peter"}
# print("both course:",python_students.intersection(java_students))
# print("python course:",python_students.difference(java_students))
# print("java course:",java_students.difference(python_students))
# print("all the course:",python_students.union(java_students)) 
# 5
# dict1={"a":1,"b":2,"c":3}
# dict2={"b":4,"d":5}
# dict1.update(dict2)
# print(dict1)
# 6
# courses=["python","java","python","c","java"]
# unique=tuple(set(courses))
# print(unique)
# 7
# students={"joe":[85,90,95],"john":[70,75,80],"mary":[92,94,96]}
# highest=""
# max=0
# for i in students:
#     avg=sum(students[i])/len(students[i])
#     if avg>max:
#         max=avg
#         highest=i
# print("highest average:",highest)
# print("average:",max)
# 8
# words=["cat","apple","dog","banana","bat","car"]
# result={}
# for word in words:
#     length=len(word)
#     if length not in result:
#         result[length]=[]
#     result[length].append(word)
# print(result)
# 9
# sentence="god is good god is powerful god is love"
# words=sentence.lower().split()
# count={}
# for i in words:
#     if i in count:
#         count[i]+=1
#     else:
#         count[i]=1
# maxi=max(count,key=count.get)
# print("most frequent word:",maxi)
# print("count:",count[maxi])
# 10
# phone_book={}
# while True:
#
#     print("menu choice \n 1:add\n 2:search \n 3:delete \n 4:display \n 5:exit")

#     choice=int(input("enter your choice:"))
#     match choice:

#         case 1:
#             name=input("enter name:")
#             number=input("enter phone number:")
#             phone_book[name]=number
#             print("contact added successfully!")
#         case 2:
#             name=input("enter name to search:")
#             if name in phone_book:
#                 ptint(name,":", phone_book[name])
#             else:
#                 print("contact not found")
#         case 3:
#             name=input("enter name to delete:")
#             if name in phone_book:
#                 del phone_book[name]
#                 print("contact deleted successfully")
#             else:
#                 print("contact not found")
#         case 4:
#             if len(phone_book)==0:
#                 print("phonebook is empty")
#             else:
#                 print("\ncontacts:")
#                 for name, number in phone_book.items():
#                     print(name, ":", number)
#         case 5:
#             print("existing phonebook...")
#             break
#         case _:
#             print("invalid choice, please try again")