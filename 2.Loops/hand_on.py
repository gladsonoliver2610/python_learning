# 1
## loops (for loop) ##
# for i in range(5):
#     print("i=",i,end="")
#     for j in range(3):
#         print("j=",j,end="")
#     print()

# 2
# row=3
# column=4
# for i in range(row):
#     for j in range(column):
#         print(" * ",end="")
#     print()

# 3
# r=4
# for i in range(r+2):
#     for j in range(i):
#         print(" * ",end="")
#     print()

# 4
# i=0 j=0-no print
# i=1 j=0-*
# i=2 j=1-* *
# i=3 j=2-* * *
# i=4 j=3-* * * *

# 5
# tables
# for i in range(1,6):
#     print("table",i)
#     for j in range(1,10):
#      print(i,"*",j,"=", i*j)
#     print()

# 6
# energy=10
# while energy>0:
#     print("jumping")
#     print("energy:",energy)
#     energy-=1
# print("loop finished.")

# 7
# status=(input("enter your day:"))
# match status:
#     case "monday":
#         print("pizza")
#     case "tuesday":
#         print("sandwich")
#     case "wednesday":
#         print("idly")
#     case "thursday":
#         print("chicken")
#     case _ :
#         print("something wrong (please try again)")