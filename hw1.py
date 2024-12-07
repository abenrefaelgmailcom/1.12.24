
#
# #1
# '''Ex 1:
# Write a for loop that prints the numbers from 12 to 24.'''
#
# for number in range (12, 25):
#     print(number, end=" ")
#
#
# #2
# '''Ex 2:
# Write a for loop that prints the ODD numbers from 7 to 31 '''
# for odd_number in range(7, 32):
#     if odd_number % 2 != 0:
#         print(odd_number, end=" ")
#
#
# #3
# '''Ex 3:
# Write a for loop that prints the EVEN numbers from 10 to -20. '''
# for even in range(7, 32):
#     if even % 2 == 0:
#         print(even, end=" ")
#
# #4
# '''Ex 4:
# Write a for loop that iterates through all numbers from 1 to 45. Print the
# following:
# ● For each number that multiples of 3 print “Fizz”
# ● For each number that multiples of 5 print “Buzz”
# ● For each number that multiples of 3 and 5 print “FizzBuzz”'''
#
# for number in range(1, 46):
#
#     if number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#     else:
#         print(number)
#
# #5
# '''Ex 5:
# Write a function that receives an array as a parameter and calculates the sum
# of all the numbers in the given array (don’t use sum() function).
# For example if the given array is: [1,13,22,123,49,34,5,24,57,45]
# The result should be 373 '''
#
# def calculate_sum(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total
#
#
# numbers = [1, 13, 22, 123, 49, 34, 5, 24, 57, 45]
# result = calculate_sum(numbers)
# print(result)  # 373
#
#
#
#
# #6
# '''Ex 6:
# Write a function that receives an array of objects.
# Each object should represent a student with the properties:
# ● id
# ● first name
# ● last name
# ● age
# ● country
# ● city
# In addition, the function should receive a property to change.
# 1 - The function should check for each property in each object in the array if
# the given property exists and if it does, the function should delete it from the
# object.
# 2 - Write a function that prints each property of each object in the given array.
# 3 - Write a function that sorts the array by the students age from the oldest to
# the youngest and return the sorted array. '''
#
#
# students = [
#     {"id": 1, "first_name": "Adam", "last_name": "Bil", "age": 35, "country": "USA", "city": "New York"},
#     {"id": 2, "first_name": "Bar", "last_name": "Ber", "age": 33, "country": "Canada", "city": "Toronto"},
#     {"id": 3, "first_name": "Alex", "last_name": "Bal", "age": 25, "country": "UK", "city": "London"}
# ]
#
# def remove_property(students, prop):
#     for student in students:
#         if prop in student:
#             del student[prop]
#
# def print_students(students):
#     for student in students:
#         for key, value in student.items():
#             print(f"{key}: {value}")
#         print()
#
# def sort_students_by_age(students):
#     return sorted(students, key=lambda x: x["age"], reverse=True)
#
# remove_property(students, "country")
# print_students(students)
# sorted_students = sort_students_by_age(students)
# print_students(sorted_students)
#
# #7
# '''Ex 7:
#
# 1 - Write a function that receives the array shown above and prints only
# animalType: cat.
# 2 - Write a function that receives the array shown above and the animal type.
# The function should print all names of that animal type if this type exists in the
# object.
# 3 - Write a function that that receives the array shown above and animal name
# The function should add the specified animal name to each ‘names’ array in
# each animal_type if that name does not exist in the ‘names’ array.
# '''
#
#
# our_pets = [
#     {"animal_type": "cat", "names": ["Meowzer", "Fluffy", "Kit-Cat"]},
#     {"animal_type": "dog", "names": ["Spot", "Bowser", "Frankie"]}
# ]
#
# def print_animal_type(pets, animal_type):
#     for pet in pets:
#         if pet["animal_type"] == animal_type:
#             print(pet)
#
# def print_names_of_animal(pets, animal_type):
#     for pet in pets:
#         if pet["animal_type"] == animal_type:
#             print(", ".join(pet["names"]))
#
# def add_name_to_all(pets, new_name):
#     for pet in pets:
#         if new_name not in pet["names"]:
#             pet["names"].append(new_name)
#
#
# #8
# student = {
# 'name': 'Adam',
# 'age': 20,
# 'hobbies': ['reading', 'games', 'coding'],
# }
#
# '''printing all students info'''
# def student_data(student):
#     for key, value in student.items():
#         print(f'{key},{value}')
#
# '''add hobby value'''
# def student_hobby(student, hobby):
#     if hobby not in student['hobbies']:
#         student['hobbies'].append(hobby)
#
# '''remove data'''
# def student_hobby_remove(student, hobby):
#     if hobby not in student['hobbies']:
#         student['hobbies'].remove(hobby)
#
#
# student_hobby(student, "swimming")
# print("After adding hobby:")
# print(student_data(student))
#
# #################
# student_hobby_remove(student, 'games')
# print('\nafter remove games')
# print(student_data(student))
#
# student["family_name"] = "Ben Refael"
# print("\nAfter adding family_name:")
# print(student_data(student))
#
#
#
# #9
# '''Write a function that prints all the elements of a 2D array using nested for
# loops. '''
#
# matrix = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
#
# def print_matrix(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             print(matrix[i][j], end=' ')
#     print()
# print(print_matrix(matrix))
# ################why it prints none
#
#
# #10
# '''Write a function to count how many numbers of zeros appear in a 2D matrix
# using nested for loops and increment operation. '''
#
#
# matrix = [
#     [0, 1, 1],
#     [0, 1, 0],
#     [1, 0, 0]
# ]
#
# def zero_count_with_indices(matrix):
#     count = 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == 0:
#                 count += 1
#     return count
#
#
# print(zero_count_with_indices(matrix))
#
#
#
# #11
# '''Write a function to return an array of all the elements that are repeated more
# than once in a given array.'''
#
# numbers: list[int] = [4,2,34,4,1,12,1,4]
#
# dict_count: dict[int, int] = dict()
# for num in numbers:
#     dict_count[num] = dict_count.get(num, 0) + 1
#     # if num in dict_count:
#     #     dict_count[num] += 1
#     # else:
#     #     dict_count[num] = 1
# print(dict_count)
#
# #12
# '''Write a function using a for loop that gets an array and returns a new array
# with the elements from the given array appearing in reverse order. (Don’t use
# array reverse() method) '''
#
# #
# def reverse_array_alt(arr):
#     reversed_arr = []
#     for i in range(len(arr)):
#         reversed_arr.insert(0, arr[i])
#     return reversed_arr
#
# arr = [43, "what", 9, True, "cannot", False, "be", 3, True]
# print(reverse_array_alt(arr))

#
# #13
#
# def mixed_arrays(first_array, second_array):
#     '''Given two arrays of integers. Add up each element in the same position and
# create a new array containing the sum of each pair.
# Assume both arrays are of the same length. '''
#     result = []
#     for i in range(len(first_array)):
#         result.append(first_array[i] + second_array[i])
#     return result
# first_array = [5 , 6 ,2]
# second_array = [4 , 7 , 3]
# print(mixed_arrays(first_array, second_array))
#
# #14
# def is_palindrome(word):
#     """check if word is palindrom"""
#     word = word.replace(" ", "").lower()
#     return word == word[::-1]
#
# first_str = "racecar"
# second_str = "Java"
# print(is_palindrome(first_str))
# print(is_palindrome(second_str))
#
#
# #15
# def multiply_counter():
#     """ loop that iterates as long as the counter is less than 100, on
# every iteration the counter is multiplied by 2 starting from 1."""
#     counter = 1
#     while counter < 100:
#         print(counter, end=" ")
#         counter *= 2
# multiply_counter()

#
# #16
# def devide_counter():
#
#     counter = 9000
#     while counter > 50:
#         print(counter, end= ' ')
#         counter //= 2
# devide_counter()
#

#
# #17
# def find_duplicates(words):
#
#     word_counter = {}
#     index = 0
#
#     while index < len(words):
#         word = words[index]
#         if word in word_counter:
#             word_counter[word] += 1
#         else:
#             word_counter[word] = 1
#         index += 1
#
#
#     result = []
#     for key, value in word_counter.items():
#         if value > 1:
#             result.append(key)
#
#     return result
#
# arr = ["danny", "apple", "danny", "banana", "apple", "kiwi"]
# print(find_duplicates(arr))
#
#
# #18
# def remove_duplicates(arr):
#
#     unique = []
#     index = 0
#
#     while index < len(arr):
#         item = arr[index]
#         if item not in unique:
#             unique.append(item)
#         index += 1
#
#     return unique
#
# names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']
# print(remove_duplicates(names))
#

#19
def remove_duplicates_skip_pete(arr):
    unique = []
    index = 0

    while index < len(arr):
        item = arr[index]
        if item != 'Pete' and item not in unique:
            unique.append(item)
        index += 1

    return unique

names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']
print(remove_duplicates_skip_pete(names))

#20
def find_repeated_index(boolean_array):

    index = 1

    while index < len(boolean_array):
        if boolean_array[index] == boolean_array[index - 1]:
            return index
        index += 1

    return -1

array1 = [True, False, False, True, True, False]
array2 = [True, False, True, False, True, True]
array3 = [True, False, True, False, True, False]

print(find_repeated_index(array1))
print(find_repeated_index(array2))
print(find_repeated_index(array3))


#21
def get_user_details():
    while True:
        # קבלת שם מלא
        full_name = input("Enter your full name (first name and last name): ")
        if len(full_name.split()) >= 2:
            break
        print("Invalid full name. Please enter at least two words.")

    while True:
        age = input("Enter your age (1-130): ")
        if age.isdigit() and 1 <= int(age) <= 130:
            age = int(age)
            break
        print("Invalid age. Please enter a number between 1 and 130.")

    while True:
        email = input("Enter your email address: ")
        if "@" in email:
            break
        print("Invalid email. Please enter a valid email address containing '@'.")

    print("\nYour details:")
    print(f"Name: {full_name}")
    print(f"Age: {age}")
    print(f"Email: {email}")

get_user_details()
