

#1
'''Ex 1:
Write a for loop that prints the numbers from 12 to 24.'''

for number in range (15, 25):
    print(number, end=" ")


#2
'''Ex 2: 
Write a for loop that prints the ODD numbers from 7 to 31 '''
for odd_number in range(7, 32):
    if odd_number % 2 != 0:  # Check if the number is odd
        print(odd_number, end=" ")


#3
'''Ex 3: 
Write a for loop that prints the EVEN numbers from 10 to -20. '''
for even in range(7, 32):
    if even % 2 == 0:  # Check if the number is even
        print(even, end=" ")

#4
'''Ex 4: 
Write a for loop that iterates through all numbers from 1 to 45. Print the 
following: 
● For each number that multiples of 3 print “Fizz” 
● For each number that multiples of 5 print “Buzz” 
● For each number that multiples of 3 and 5 print “FizzBuzz”'''

for number in range(1, 46):

    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
    else:
        print(number)

#5
'''Ex 5: 
Write a function that receives an array as a parameter and calculates the sum 
of all the numbers in the given array (don’t use sum() function). 
For example if the given array is: [1,13,22,123,49,34,5,24,57,45] 
The result should be 373 '''

def calculate_sum(array):
    total = 0
    for number in array:
        total += number  # Add each number to the total
    return total

# דוגמה
numbers = [1, 13, 22, 123, 49, 34, 5, 24, 57, 45]
print(calculate_sum(numbers))  # פלט: 373




#6
'''Ex 6: 
Write a function that receives an array of objects. 
Each object should represent a student with the properties: 
● id 
● first name 
● last name 
● age 
● country 
● city 
In addition, the function should receive a property to change. 
1 - The function should check for each property in each object in the array if 
the given property exists and if it does, the function should delete it from the 
object.  
2 - Write a function that prints each property of each object in the given array. 
3 - Write a function that sorts the array by the students age from the oldest to 
the youngest and return the sorted array. '''


students = [
    {"id": 1, "first_name": "Adam", "last_name": "Bil", "age": 35, "country": "USA", "city": "New York"},
    {"id": 2, "first_name": "Bar", "last_name": "Ber", "age": 33, "country": "Canada", "city": "Toronto"},
    {"id": 3, "first_name": "Alex", "last_name": "Bal", "age": 25, "country": "UK", "city": "London"}
]
# פונקציה למחיקת מאפיין
def remove_property(students, prop):
    for student in students:  # מעבר על כל הסטודנטים
        if prop in student:  # בדיקה אם המאפיין קיים
            del student[prop]  # מחיקה אם קיים

# פונקציה להדפסת מאפיינים
def print_students(students):
    for student in students:  # מעבר על כל הסטודנטים
        for key, value in student.items():  # הדפסת כל המאפיינים
            print(f"{key}: {value}")
        print()  # רווח בין סטודנטים

# פונקציה למיון לפי גיל
def sort_students_by_age(students):
    return sorted(students, key=lambda x: x["age"], reverse=True)  # מיון מהמבוגר לצעיר


#7
'''Ex 7: 

1 - Write a function that receives the array shown above and prints only 
animalType: cat. 
2 - Write a function that receives the array shown above and the animal type. 
The function should print all names of that animal type if this type exists in the 
object.  
3 - Write a function that that receives the array shown above and animal name 
The function should add the specified animal name to each ‘names’ array in 
each animal_type if that name does not exist in the ‘names’ array. 
'''


our_pets = [
    {"animal_type": "cat", "names": ["Meowzer", "Fluffy", "Kit-Cat"]},
    {"animal_type": "dog", "names": ["Spot", "Bowser", "Frankie"]}
]

# פונקציה להדפסת סוג חיה מסוים
def print_animal_type(pets, animal_type):
    for pet in pets:
        if pet["animal_type"] == animal_type:
            print(pet)

# פונקציה להדפסת שמות של סוג חיה
def print_names_of_animal(pets, animal_type):
    for pet in pets:
        if pet["animal_type"] == animal_type:
            print(", ".join(pet["names"]))

# פונקציה להוספת שם חדש
def add_name_to_all(pets, new_name):
    for pet in pets:
        if new_name not in pet["names"]:
            pet["names"].append(new_name)