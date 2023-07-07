# task1
unformated_str = "My name is %s, I am %d, years old and I am from USA."
name = "John"
age = 25
country = "Germany"
formated_str = unformated_str % (name,age)
x = formated_str.replace("USA",country)
print(x)

# task2
str = "The sky is blue and the ocean is blue."
x = str.replace("blue","red",1)
print(x)

# task3
txt1 = input("Write the text: ")
word = input("Write a word: ")
index = txt1.find(word)
count = txt1.count(word)
print(f'The word {word} is found at index {index} and it appears {count} times in this sentence.')

#task4
file_name = input("Enter a file name: ")
if file_name.startswith("file_") and file_name.endswith(".txt"):
    message = "The file name is valid."
else:
    message = "The file name is not valid."
print(message)

#task 5
text = input("make your list: ") 
print(text.replace(",","-"))