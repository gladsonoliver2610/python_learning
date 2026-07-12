# 1
age=int(input("enter your age:"))
citizenship=input("are you an indian citizen:")
if age>=18:
    if citizenship=="yes":
        print("your are eligible:")
    else :
        print("your are not eligible because your not an indian")
else:
    print("your are not eligible because your under 18")
