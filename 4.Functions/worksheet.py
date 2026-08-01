# 4.a
#1
# def even_odd(num):
#     if num%2== 0:
#         print("even")
#     else:
#         print("odd")
# num =int(input("enter a number:"))
# even_odd(num)
#2
# def count_vowels(text):
#     count=0
#     for i in text:
#         if i in ["a","e","i","o","u"]:
#             count+=1
#     return count
# text = input("enter a string:")
# print(count_vowels(text))
#3 (i took this from automation, so i have some doubts uncle)
# def prime_number(num):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 print("not prime")
#                 break
#         else:
#             print("prime")
# num=int(input("enter a number:"))
# prime_number(num)
#3 ( i took this from automation, so i have some doubts uncle)
# def prime_numbers_upto_100():
#     primes = []
#     for num in range(2, 101):
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
#     return primes
# print(prime_numbers_upto_100())
#4
# def palindrome(string):
#     if string==string[::-1]:
#         print("it is a palindrome")
#     else:
#         print("it is not a palindrome")
#     return string
# string=input("enter a string:")
# palindrome(string)
#5 ( uncle i understood how to use function but i dont know how to do this question)
# def reverse_number(num):
#     reversed_num=0
#     while num>0:
#         digit=num%10
#         reversed_num=reversed_num*10+digit
#         num=num//10
#     return reversed_num
# num=int(input("enter a number:"))
# print("reversed number:",reverse_number(num))
#6
# def find_max(numbers):
#     max_num = numbers[0]
#     for num in numbers:
#         if num > max_num:
#             max_num = num
#     return max_num
# numbers=[1,2,3,4,76,0]
# print("maximum number:", find_max(numbers))
#7
# def rotate_list(items,k):
#     k = k % len(items)  
#     return items[-k:] + items[:-k]
# print(rotate_list([1,2,3,4,5], 2))  
#8 ( uncle i cant able to understand this question can u explain it to me in the next class...?)
#9
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(3))
#10
# def list_sum(numbers):
#     total=0
#     for num in numbers:
#         total+=num
#     return total
# print(list_sum([1,2,3,4,5]))
# (hence i have completed the worksheet but still i have some doubts uncle, can u please explain it to me in the next class...?)