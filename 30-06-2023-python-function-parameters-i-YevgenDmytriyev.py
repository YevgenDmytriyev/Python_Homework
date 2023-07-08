# 1 Task
def isOdd(num):
    return num % 2 != 0

def isEven(num): 
    return num % 2 == 0

print(isOdd(1), isEven(1))          
print(isOdd(657842), isEven(657842))  
print(isOdd(0), isEven(0)) 

# 2 Task
def getParity(*args, parity):
    if parity == 'odd':
        return [num % 2 == 1 for num in args]
    elif parity == 'even':
        return [num % 2 == 0 for num in args]
    else:
        return "Parity indicated is unknown"

# Test cases
print(getParity(3, 6, 7, 10, parity='odd'))  # Output: [True, False, True, False]
print(getParity(2, 4, 5, 8, parity='even'))  # Output: [True, True, False, True]
print(getParity(2, 3, 4, 7, parity='even'))  # Output: [True, False, True, False]
# print(getParity(-2, 'number'))  # Output: "Parity indicated is unknown"

# 3 Task

import datetime

def greet(*, name, date):
    morning_cutoff = datetime.datetime.strptime('12:00', '%H:%M').time()
    evening_cutoff = datetime.datetime.strptime('18:00', '%H:%M').time()

    if date.time() < morning_cutoff:
        return f"Good Morning, {name}!"
    elif date.time() < evening_cutoff:
        return f"Good Afternoon, {name}!"
    else:
        return f"Good Evening, {name}!"

# Test cases
print(greet(
    name="John",
    date=datetime.datetime(2021, 5, 7, 11, 59, 59)
    ))
print(greet(
    date=datetime.datetime(2021, 5, 7, 12, 0, 1),
    name="John"
    ))

# 4 Task
def sumAll(*lists):
    total_sum = 0
    for sublist in lists:
        total_sum += sum(sublist)
    return total_sum

# Test cases
test1 = [[0, 2, 4, 5]]
test2 = [
    [0, 2, 4, 5],
    [6],
    [0, 2, 4, 5, 1, 4, 3, 2]
]

print(sumAll(*test1))  # Output: 11
print(sumAll(*test2))  # Output: 38

# 5 Task

def pig_latin(*words, suffix="ay", single=False):
    translated_words = []
    
    for word in words:
        # Splitting the input string into words
        word_list = word.split()
        
        # Translating each word according to the rules
        translated_word_list = []
        for w in word_list:
            if w[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                translated_word_list.append(w + suffix)
            else:
                translated_word_list.append(w[1:] + w[0] + suffix)
        
        # Joining the translated words back into a string
        translated_word = " ".join(translated_word_list)
        translated_words.append(translated_word)
    
    # Checking the value of 'single' argument and returning the result accordingly
    if single:
        return " ".join(translated_words)
    else:
        return translated_words

# Test cases
test1_data = ["Word", "Apple"]
test1_config = {}

test2_data = ["Python", "Functions"]
test2_config = {"suffix": "oy"}

test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
test3_config = {"single": True, "suffix": "ep"}

print(pig_latin(*test1_data, **test1_config))  # Output: ['Ordway', 'Appleay']
print(pig_latin(*test2_data, **test2_config))  # Output: ['Ythonpoy', 'Unctionsfoy']
print(pig_latin(*test3_data, **test3_config))  # Output: 'Ifay hetay ordway startsay ithway aay owelay adday hetay suffixay otay hetay ordwayay'



"""In Python, the return statement is used to specify the value that a function should return.
When a return statement is executed in a function, it immediately terminates the function's execution 
and returns the specified value as the result of the function."""
"""
In the isOdd function, the expression num % 2 calculates the remainder when num is divided by 2. 
If this remainder is not equal to 0 (i.e., it is non-zero), then it means that num is an odd number.
In this case, the function returns True. If the remainder is 0, 
it means that num is an even number, and the function returns False.

To put it simply, num % 2 != 0 is a condition that checks if the number num is not divisible evenly by 2,
which indicates that the number is odd.

The isOdd function checks if the remainder of num divided by 2 is not equal to 0. 
If the remainder is non-zero, the number is odd, and the function returns True. 
Otherwise, it returns False.

The isEven function checks if the remainder of num divided by 2 is equal to 0. 
If the remainder is zero, the number is even, and the function returns True. 
Otherwise, it returns False.


"""


