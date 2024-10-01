# Ashley Criger
# UWYO COSC 1010
# Submission Date
# Lab 03 
# Lab Section: 10
# Sources, people worked with, help given to: Kaylee Esgar and TA (Austin Barner)
# your
# comments
# here



# This is your second lab section. It will primarily be about working with lists
# Complete all sections of this assignment 
max_temps = [
    32, 24, 22, 25, 37, 33, 34, 40, 40, 42,
    35, 35, 47, 49, 37, 37, 35, 23, 26, 25,
    21, 26, 24, 23, 21, 26, 30, 30, 7, -2,
    18, 35, 35, 41, 37, 50, 31, 33, 36, 21,
    34, 50, 36, 47, 32, 13, 14, 38, 46, 35,
    40, 47, 26, 28, 32, 42, 48, 40, 32, 28,
    35, 35, 39, 38, 34, 32, 31, 37, 49, 45,
    39, 46, 50, 53, 32, 28, 34, 43, 40, 42,
    37, 39, 39, 28, 30, 22, 43, 54, 55, 35,
    49, 53, 42, 24, 28, 36, 54, 56, 57, 66,
    71, 71, 63, 33, 38, 56, 62, 62, 40, 39,
    37, 37, 49, 57, 48, 58, 58, 50, 65, 66,
    70, 67, 71, 64, 62, 58, 59, 61, 67, 61,
    52, 48, 52, 58, 61, 69, 70, 63, 60, 70,
    71, 75, 74, 67, 74, 72, 75, 71, 74, 77,
    77, 67, 60, 60, 58, 67, 73, 69, 65, 68,
    67, 63, 61, 62, 69, 62, 61, 66, 75, 81,
    79, 76, 74, 80, 73, 77, 84, 83, 83, 77,
    63, 76, 79, 84, 73, 67, 69, 69, 73, 78,
    83, 85, 85, 85, 81, 81, 86, 93, 86, 82,
    74, 79, 85, 87, 89, 87, 86, 88, 85, 85,
    88, 88, 81, 77, 79, 79, 77, 71, 73, 73,
    76, 83, 84, 83, 68, 77, 88, 89, 89, 86,
    85, 87, 90, 85, 85, 80, 59, 72, 77, 73,
    77, 86, 85, 87, 81, 80, 76, 68, 80, 78,
    82, 78, 67, 66, 72, 75, 55, 64, 72, 77,
    75, 70, 72, 71, 70, 62, 71, 75, 79, 79,
    80, 76, 80, 77, 71, 55, 58, 61, 56, 67,
    70, 69, 68, 67, 42, 43, 51, 59, 69, 74,
    65, 72, 77, 75, 69, 71, 63, 67, 63, 54,
    32, 26, 42, 52, 58, 57, 59, 62, 64, 59,
    50, 41, 41, 50, 51, 57, 63, 60, 61, 55,
    56, 55, 47, 36, 50, 59, 36, 20, 24, 32,
    38, 48, 50, 34, 37, 32, 36, 48, 52, 57,
    48, 34, 29, 39, 44, 39, 33, 40, 44, 55,
    51, 55, 55, 54, 53, 51, 43, 23, 20, 30,
    35, 32, 41, 48, 44
]


min_temps = [
    23, 14, 7, 11, 13, 22, 15, 21, 23, 31,
    19, 12, 18, 30, 23, 20, 15, 2, 7, -2,
    2, 3, -2, -8, 5, 8, 16, 1, -8, -26, -26,
    11, 5, 16, 22, 25, 15, 11, 16, 2, -4, 
    13, 15, 13, 11, -4, -16, -1, 18, 16, 26,
    21, -21, -23, 2, 11, 23, 22, 14, 8, 7,
    15, 9, 16, 9, 14, 19, 17, 22, 21, 13,
    28, 28, 32, 8, -1, 3, 5, 24, 19, 20,
    20, 20, 14, 9, 8, 8, 21, 19, 20, 21,
    25, 22, 3, 2, 10, 13, 24, 26, 26, 33,
    35, 32, 25, 19, 22, 28, 31, 20, 18, 18,
    14, 15, 20, 34, 25, 29, 24, 30, 31, 29,
    40, 34, 34, 31, 28, 30, 31, 30, 38, 41,
    40, 39, 42, 38, 39, 36, 44, 41, 36, 36,
    37, 40, 42, 41, 44, 41, 36, 37, 38, 38,
    45, 45, 45, 49, 46, 41, 43, 43, 44, 44,
    41, 47, 46, 42, 46, 46, 40, 45, 48, 50,
    39, 51, 48, 42, 38, 44, 45, 44, 48, 43,
    42, 49, 45, 49, 49, 47, 42, 48, 46, 49,
    47, 48, 52, 49, 46, 48, 47, 56, 57, 48,
    43, 47, 52, 54, 52, 53, 50, 54, 50, 52,
    53, 55, 54, 51, 50, 47, 41, 41, 46, 43,
    48, 51, 53, 43, 35, 40, 50, 51, 58, 56,
    58, 50, 54, 48, 57, 51, 50, 49, 46, 43,
    52, 49, 49, 48, 50, 49, 45, 40, 44, 39,
    41, 47, 40, 34, 37, 45, 37, 33, 34, 40,
    45, 40, 41, 40, 37, 32, 31, 31, 35, 39,
    38, 38, 41, 32, 35, 30, 30, 30, 25, 29,
    30, 34, 40, 29, 29, 24, 28, 32, 39, 36,
    36, 39, 32, 36, 33, 31, 31, 20, 16, 19,
    3, 2, 14, 29, 29, 42, 33, 34, 29, 35,
    16, 15, 14, 23, 27, 19, 36, 30, 28, 26,
    25, 25, 22, 18, 17, 20, 9, 2, 7, 7,
    18, 16, 17, 13, 17, 21, 31, 30, 27, 23,
    17, 12, 18, 25, 24, 24, 14, 10, 20, 19,
    17, 28, 23, 25, 23, 23, -3, -15, 19, 5,
    -1, -1, 11, 13
]

# The above two lists are datasets for the maximum and minimum temperatures for Laramie in 2023.
# Each of these lists has the same length, indicating that they both have the same index positions.
# Write a single for loop to calculate both the average maximum temperature and the average minimum temperature.
min_max = min_temps[0] # Sets a starting point for the loop
max_max = max_temps[0] # Sets a starting point for the loop
min_total = 0 # Starts the loop at 0 when adding the other values
max_total = 0 # Starts the loop at 0 when adding the other values
for i in range(0,len(min_temps)): # Starts the loop for the length of the list
    min_total = min_total + min_temps[i] # Adds the values together with the starting point being 0 and going through all points in the list
    if min_temps[i] > min_max: # Goes through the minimum list
        min_max = min_temps[i] 
    max_total = max_total + max_temps[i] # Adds the values together with the starting point being 0 and going through all points in the list
    if max_temps[i] > max_max: # goes through the max list
        max_max = max_temps[i] 
average_max = (max_total)/len(max_temps)
average_min = (min_total)/len(min_temps)
# You cannot use any pre-existing functions (like mean()) and must perform the calculations manually.
# Output the results of both calculations.
print(f"The average max temperature is {average_max} degrees and the average minimum temp is {average_min} degrees") # Prints the values of averages
# For the next part, determine the highest and lowest recorded temperatures.
# HINT: You can find this information without using any logic or looping.
min1 = min(min_temps) # Minimum point for min_temps
max1 = max(max_temps) # Maximum point for max_temps
min2 = min(max_temps) # Minimum point for max_temps
max2 = max(min_temps) # Maximum point for min_temps

if min1 <= min2: # Finds which value is larger
    print(f"The minimum temperature is {min1}") # Prints the value if min1 is smaller
    else
    print(f"The minimum temperature is {min2}") # Prints the value if min2 is smaller
if max1 >= max2:
    print(f"The maximum temperature is {max1}") # Prints the value if max1 is larger
    else
    print(f"The maximum temperature is {max2}") # Prints the value if max2 is larger
