#1
# f=open("student.txt","x")
# f.write("Name: Rahul\nAge:21\nCousrse:Python")
# f.close()
#2
# f=open("gladdy_3.txt","r")
# print(f.read())
# f.close()
#3
# f=open("cities.txt","x")
# f.write("Cities:\n Chennai\n Mumbai\n Calcutta")
# f.close()
#4
# f=open("classwork.txt","r")
# content=f.read()
# for i in content[::3]:
#     print(i)
# f.close()
#5
# f=open("classwork.txt","r")
# content=f.read()
# f.close()
# f=open("copy.txt","w")
# f.write(content)
# f.close()
#5b
#1.Create a Python code that reads a text file, counts the occurrences of each word, and prints the word counts to the console. Consider handling cases where words are case-insensitive (e.g.,
# "The" and "the" should be counted as the same word).
# f=open("gladdy_2.txt", "r")
# words = f.read()
# words_1=words.lower()
# words_2=words_1.split()
# count = {}
# for word in words_2:
#     if word in count:
#         count[word] += 1
#     else:
#         count[word] = 1
# for word in count:
#     print(word, ":", count[word])
# f.close()
#2.Write a program that takes user input (e.g., names and ages) and appends this lata to a CSV (Comma Separated Values) file. Ensure that each entry is added as a new line in the file, and new files are created if they don't exist.
# import csv
# name = input("Enter name: ")
# age = input("Enter age: ")
# with open("data.csv", "a", newline="") as f:
#     write = csv.writer(f)
#     write.writerow([name, age])
# print("Data added")
#3.Develop a Python code that reads a text file, replaces all occurrences of a specific word with another word, and writes the modified content back to the same file or a new file
#ai given
# file = open("gladdy.txt", "r")
# text = file.read()
# file.close()
# old_word = input("Enter the word to replace: ")
# new_word = input("Enter the new word: ")
# text = text.replace(old_word, new_word)
# file = open("gladdy.txt", "w")
# file.write(text)
# file.close()
# print("Word replaced successfully!")
#4.Create a Python code that attempts to open a file in read mode. Implement error handling using try-except blocks to catch FileNotFoundError and print a user friendly error message if the file does not exist. Additionally, handle PermissionError in case the program does not have the necessary permissions toread the file
