
import time

## Efficiency Code Test

SQUARE_RANGE = range(1, 1000)

print("\nEfficiency Code Test:\n")

## The Good
start_time = time.time()
squares = [x**2 for x in SQUARE_RANGE]
end_time = time.time()

print("Efficient Squares:", "Execution Time (in ms):", format((end_time - start_time) * 1000, '.5f'));

## The Bad
start_time = time.time()
squares = []
for x in SQUARE_RANGE:
    squares.append(x**2)
end_time = time.time()

print("Inefficient Squares:", "Execution Time (in ms):", format((end_time - start_time) * 1000, '.5f'));

## Extensibility Code Test

print("\nExtensibility Code Test:\n")

# More Extensible Approach
class Animal:
    def speak(self):
        raise NotImplementedError()

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
    

def make_sound(animal: Animal) -> str:
    return animal.speak();

pets = [Dog(), Cat()]
print ("Animal Sounds with Polymorphism:", [make_sound(pet) for pet in pets])
# Adding a new animal type only requires creating a new subclass of Animal. Wi

# Less Extensible Approach
def get_animal_sound_from_type(type) -> str:
    if type == "dog":
        return Dog().speak()
    elif type == "cat":
        return Cat().speak()
    else:
        return "Unknown animal type"

print("Animal Sound from function:", get_animal_sound_from_type("dog"))
print("Animal Sound from function (with unknown type):", get_animal_sound_from_type("monkey"))
# Adding a new animal type requires modifying the function and/or every place where an animal specific behavior is needed, which is less extensible.

## Regularity Code Test

print("\nRegularity Code Test:\n")

## Consistent syntax and structure
## len() function is used to get the length of different data structures
my_list = [1, 2, 3, 4, 5]
my_string = "Hello"
print("Starting list (" + str(len(my_list)) + "):" , my_list)
print("Starting string (" + str(len(my_string)) + "):", my_string)

## Violates regularity
## Different methods are used to append elements to different data structures
my_list.append(6)
my_string += " World"

print("Appended list (" + str(len(my_list)) + "):" , my_list)
print("Appended string (" + str(len(my_string)) + "):", my_string)
# Lists use the append() method, while strings use concatenation with +=, which is less regular.



## Security Code Test
print("\nSecurity Code Test:\n")

# Violates Security: eval() with input()
# user_code = input("Enter something: ")
# result = eval(user_code) # Dangerous: lets user run arbitrary code!
# print(result)

# Safely evaluate Python literals using ast.literal_eval
import ast
user_input = "[1, 2, 3]"  # Example input
try:
    value = ast.literal_eval(user_input)
    print("Safely evaluated:", value, "of type", type(value))
except Exception as e:
    print("Invalid input:", e)

