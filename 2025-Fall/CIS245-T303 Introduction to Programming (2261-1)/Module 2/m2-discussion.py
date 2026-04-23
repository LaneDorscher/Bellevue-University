


# In this module’s assigned readings, you learned about two guidelines for indentation with the IF-ELSE statement. What are the two guidelines? Provide an example of each.
# You also learned about nested decision structures using the IF-ELIF-ELSE statement. Provide an example of how you could implement a nested decision structure using the IF-ELIF-ELSE statement.


# The two guidelines for indentation with the IF-ELSE statement are:

# Make sure the if clause and the else clause are indented at the same level.
# Indent the statements within the if and else clauses one level further than the if and else clauses themselves.
# Example of the first guideline:
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")
# Example of the second guideline:
y = 3
if y > 5:
    print("y is greater than 5")
    if y > 2:
        print("y is greater than 2")
    else:
        print("y is not greater than 2")
else:
    print("y is 5 or less")