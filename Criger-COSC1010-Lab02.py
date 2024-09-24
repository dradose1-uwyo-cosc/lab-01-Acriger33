# Ashley Criger
# UWYO COSC 1010
# 9/22/24
# Lab 02 
# Lab Section: 10
# Sources, people worked with, help given to: Kaylee Esgar and TA (Austin Burner)
# your
# comments
# here

your_variable_here = "when you see this, replace it with your code"

## Section ONE

# Complete the following print statement to print out "Hello, COSC1010"
print("Hello, COSC1010") # Statment to store Hello, COSC1010

# Assign the string above to a variable named hello_message and print that variable
hello_message = "Hello, COSC1010" # Creating a variable to store Hello, COSC1010
print(hello_message) # Print the variable hello_message, that's storing Hello, COSC1010

# Assign the string "cowboy joe" to a variable, and print that variable with title casing
CJ = "cowboy joe" # Creating a variable to store cowboy joe
print(CJ.title()) # Prints CJ that is storing cowboy joe, but .title() will capitalize the C and J of Cowboy Joe

# Complete the following f-string print message 
    # You will need to create your own variables and insert them  
    # the final message should read `The University of Wyoming was founded in 1886`
School = "University of Wyoming" # Creating a variable to store University of Wyoming
Year = "1886" # Creating a variable to store the year the school was established
print(f"The {School} was founded in {Year}") # Will print using a f string and the previously created variables

# Now let's do some math with variables 
    # Create two variables x and y and assign them the values 5 and 10 respectively 
    # Complete the following print statements using your variables
    #All math must be done within the braces in the f-strings
x = 5 # Variable created to store the number 5
y = 10 # Variable created to store the number 10
print(f"x + y = {x + y}") # Will print and compute the following equation
print(f"x - y = {x-y}") # Will print and compute the following equation
print(f"x * y = {x*y}") # Will print and compute the following equation
print(f"x / y = {x/y}") # Will print and compute the following equation

# String concatenation 
    # Finally we will take a look at string concatenation
    # String concatenation combines two strings together
    # It is done using the + operator
    # Create three variables:
        # first_name, which is your first name 
        # last_name, which is your last name
        # space, which is a space character 
    # Use string concatenation to print out your full name 
first_name = "Ashley" # variable to store Ashley 
last_name = "Criger" # Variable to store Criger
space = " " # Variable to store space
print(first_name + space + last_name) # Will print name with space