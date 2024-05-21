

## Chapter 3 - Graded App
3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.



```py
# Prompt the user for hours and rate per hour
hrs = input("Enter Hours: ")
rate = input("Enter Rate per Hour: ")

# Convert the input strings to float
h = float(hrs)
r = float(rate)

# Calculate the gross pay
if h <= 40:
    gross_pay = h * r
else:
    # For hours above 40, pay 1.5 times the hourly rate
    overtime_hours = h - 40
    gross_pay = (40 * r) + (overtime_hours * r * 1.5)

# Print the gross pay
# print("Gross Pay:", gross_pay)
print(gross_pay)
```

### Explanation:
The program prompts the user to input the number of hours worked (hrs) and the hourly rate (rate).
- It converts these input values from strings to floating-point numbers using float().
- The program then checks if the hours worked (h) are less than or equal to 40. If so, it calculates the gross pay by multiplying the hours by the hourly rate.
- If the hours worked are more than 40, it calculates the overtime hours and pays 1.5 times the hourly rate for those hours. The total gross pay is the sum of the regular pay (for the first 40 hours) and the overtime pay.
- Finally, it prints the gross pay.

When tested with 45 hours and a rate of 10.50 per hour, the output will be 498.75, as expected.


## Assignment 3.3

3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.


```py
# Prompt the user for a score
score_input = input("Enter a score between 0.0 and 1.0: ")

try:
    # Convert the input string to a float
    score = float(score_input)
    
    # Check if the score is within the valid range
    if score < 0.0 or score > 1.0:
        print("Error: Score is out of range.")
    else:
        # Determine the grade based on the score
        if score >= 0.9:
            grade = 'A'
        elif score >= 0.8:
            grade = 'B'
        elif score >= 0.7:
            grade = 'C'
        elif score >= 0.6:
            grade = 'D'
        else:
            grade = 'F'
        
        # Print the grade
        #print("Grade:", grade)
        print(grade)
except ValueError:
    print("Error: Invalid input. Please enter a numerical value.")
```

### Explanation:
The program prompts the user to input a score between 0.0 and 1.0.

- It attempts to convert the input string to a float within a try block to catch any ValueError that may arise from invalid input (non-numeric values).
- It checks if the score is within the valid range (0.0 to 1.0). If not, it prints an error message.
- If the score is within the valid range, the program determines the corresponding grade using a series of if-elif-else statements.
- Finally, it prints the grade.

When tested with a score of 0.85, the output will be Grade: B.



## Assignment 4.6

4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.


```py
def computepay(h, r):
    if h <= 40:
        pay = h * r
    else:
        overtime_hours = h - 40
        pay = (40 * r) + (overtime_hours * r * 1.5)
    return pay

# Prompt the user for hours and rate per hour
hrs = input("Enter Hours: ")
rate = input("Enter Rate per Hour: ")

# Convert the input strings to float
h = float(hrs)
r = float(rate)

# Call the computepay function to calculate the gross pay
pay = computepay(h, r)

# Print the gross pay
#print("Pay:", pay)
print("Pay", pay)
```

### Explanation:
1. The computepay() function takes two arguments: h for hours and r for rate per hour.
2. Inside the function, it checks if the hours worked are less than or equal to 40. If so, it calculates the pay by multiplying hours by the rate.
3. If the hours worked are more than 40, it calculates the overtime hours and pays 1.5 times the hourly rate for those hours. The total pay is the sum of the regular pay (for the first 40 hours) and the overtime pay.
4. The function returns the computed pay.
5. The main program prompts the user to input the number of hours worked and the hourly rate.
6. It converts these input values to floating-point numbers.
7. The main program calls the computepay() function with these values and stores the result in the variable pay.
8. Finally, it prints the computed pay.
9. When tested with 45 hours and a rate of 10.50 per hour, the output will be Pay: 498.75, as expected.



## Assignment 5.2
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

```py
largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        number = int(num)
    except ValueError:
        print("Invalid input")
        continue
    
    if largest is None or number > largest:
        largest = number
    if smallest is None or number < smallest:
        smallest = number

print("Maximum is", largest)
print("Minimum is", smallest)
```