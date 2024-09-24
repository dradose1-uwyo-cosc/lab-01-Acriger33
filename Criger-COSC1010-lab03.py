# Ashley Criger
# UWYO COSC 1010
# 9/29/2024
# Lab 03 
# Lab Section: 10
# Sources, people worked with, help given to: Kaylee Esgar adn TA (Austin Barner)
# your
# comments
# here



# This is your second lab section. It will primarily be based on the Introducing Lists lecture, reference it if you need
# Complete all sections of this assignment 


print("Part One------------------------------------------------------------------------")
#We are going to start with the basics. Declare a list  states that contains the elements: Wyoming, Colorado, Montana in that order 
#Note this is the ONLY point where you need to declare the states list
states = ["Wyoming", "Colorado", "Montana"] # Creates a list with states as the variable


#print the entire list
print(states) # Prints the list for states

#now print the first element in the list
print(states[0]) # 0 is the first element in the list and will print the first element out

#Print the last element using the syntax shown in class to access the final element (hint, think negatives)
print(states[-1]) # will print the last element using -1

#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided
print(f"{states[1].upper()} is south of {states[0].upper()}") # Using .uppper() to capitalize list elemets and f string to show the statement wanted



print("Part Two------------------------------------------------------------------------")
#Append the following states to your list: Washington, Oregon, California and print your list
states.append("Washington") # Append will add an element to the list one by one
states.append("Oregon")
states.append("California")
print(states) 
#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 
states[-2] = "Maine" # this will replace the second to last element and show it as Maine
print(states)
#Insert the state Texas to be the third element in the list, again printing your list
states.insert(2,"Texas") # Add Texas into our list with it being the second element
print(states)
#Using the `del` statement remove the fourth item from the list, print your list 
del states[3] # removes the fourth item by using del
print(states)
#Remove Texas using its value, print the list
states.remove("Texas") # Will remove Texas from the list
print(states)

print("Part Three----------------------------------------------------------------------")
#Temporarily sort your list, print it both sorted and unsorted 
print(states)
print(sorted(states)) # sorts the states temporairly

#Permanently sort your list in reverse order, printing it out
states.sort(reverse=True) # Permanently sorts the order alphabetically and then will reverse the order
print(states)
#Using the reverse method reverse the list and print it
states.reverse() # Reverses the order to be correct alphabetically again
print(states)