# create a file
# f=open("gladdy.txt","x")
# f.write("Hello, World!")
# f.close()
# f=open("C:\python_learning\gladdy.txt","r")
# content=f.readlines()
# # print(content[0])
# for i in content:
#     words=i.split()
#     for j in words:
#         if j=="Henry":
#             print("Henry is present in the file")
#             break
# f.close()
# f=open("gladdy_2.txt","w")
# f.write("hello gladson")
# f.close()
with open("gladdy_2.txt","r") as file:
    content=file.readlines(150)
    print(content)
    # for i in content:
    #     words=i.split()
    #     for j in words:
    #         if j=="you":
    #             print("you is present in the file")
    #             break