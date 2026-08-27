# def add_numbers(a=7,b=8):
#     sum=a+b
#     print()


# def customer_bill(bill_value):
#     customer_category=input("special or normal:")
#     if customer_category=="special":
#         discount=20/100*bill_value
#         new_value=bill_value-discount
#         return new_value
#     else:
#         discount=10/100*bill_value
#         new_value=bill_value-discount
#         return new_value
# final_amt=customer_bill(200)
# print("final amt:",final_amt)

# def sum_n(n):
#     if n==0:
#         return 0
#     else:
#         return n+sum_n(n-1)
# print(sum_n(5))

# def print_descend(n):
#     if n==0:
#         return
#     print(n,end=",")
#     return print_descend(n-1)
# n=5
# print_descend(n)

# count=0  # to track the number of times func is called
# def print_descend(n):
#     global count
#     count +=1
#     if n==0: #base case
#         count=0
#         return
#     print(f"call count ={count} n= {n}")
#     print_descend(n-1) #recursive case
#     #location where return stmt start executing
#     count+=1
#     print(f"return count ={count} n={n}")
#     return

# n=5
# print_descend(n)

marks= lambda x: x*100/40
print(marks(35))