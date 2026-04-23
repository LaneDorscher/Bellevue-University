# List of strings
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Iterate and print each element

## Great way to iterate through a list of data objects when you don't need the index
for fruit in fruits:
    print(f"Without Index - Fruit: {fruit}")

## A way to iterate through a list of data objects when you need the index and want the element, avoids indexing the list directly (example: list[index])
for (index, fruit) in enumerate(fruits):
    print(f"Using Enumerate - Index {index}: {fruit}")

## A way to iterate through a list with just the index, requires indexing the list directly (example: list[index])
for index in range(len(fruits)):
    print(f"Using Range - Index {index}: {fruits[index]}")
