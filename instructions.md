# Control Statements - Project

## Instructions

Below are the instructions for the project. The project is broken into 3 files, each with their own varying tiers of difficulty. It is recommended that you start with simple.py before moving onto the others, however you may tackle this project in any order.

### simple.py

In simple.py, your task will be to print the following patterns using conditional statements and loops. Which conditional statements and loops you use will be at your discretion, as long as it accomplishes the task.

#### Pattern 1

```
##########
##########
###
###
##########
##########
###
###
##########
##########
```

#### Pattern 2

```
#
##
###
####
#####
####
###
##
#
```

#### Pattern 3

```
#######
     # 
    #  
   #   
  #    
 #     
#######
```

### normal.py

#### Task 1: Multiplication Tables
For your first task in normal.py, you will need to make the multiplication table for a number for 0 - 25.

Write the program according to the following specifications:
- Accept input from the user in the form of a number. This number will be used to create the multiplication table.
- Print the product of that number multiplied by the numbers 0 - 25, inclusive.
- Output should appear like the following:
```
>> 27
0 x 27 = 0
1 x 27 = 27
2 x 27 = 54
3 x 27 = 81
4 x 27 = 108
5 x 27 = 135
6 x 27 = 162
7 x 27 = 189
8 x 27 = 216
9 x 27 = 243
10 x 27 = 270
11 x 27 = 297
12 x 27 = 324
13 x 27 = 351
14 x 27 = 378
15 x 27 = 405
16 x 27 = 432
17 x 27 = 459
18 x 27 = 486
19 x 27 = 513
20 x 27 = 540
21 x 27 = 567
22 x 27 = 594
23 x 27 = 621
24 x 27 = 648
25 x 27 = 675
```

#### Task 2: Sentinel-Controlled Iteration
Write the program according to the following specifications:
- Create a program that tracks the changes to a specific number, x. This number x begins at 1.
- Regularly throughout the program, the user will be asked to enter a number. Based on the number, the program should do different things:
  - If the user enters a zero, output the value of x, and exit the program.
  - If the user enters an even number:
    - If the number is negative, add it to x, and save the sum to x.
    - If the number is positive, multiply it with x, and save the product to x.
    - In both cases, output x to the user after modifying it.
  - If the number is an odd number:
    - If the number is negative, subtract it from x, and save the difference to x.
    - If the number is positive, divide x by the number, and save the quotient to x.
    - In both cases, output x to the user after modifying it.

Example Output:
```
x = 0
>> 5

x = 0

```

### complex.py

For complex.py, your job will be to create a program that verifies a password for use on your site. Typically when making an account, the password you create to use with the account has some rules you must follow.

Write the program according to the following specifications:
- The program should accept input from the user in the form of a password.
- Verify the password is at least 8 characters long.
- Verify this password contains:
  - At least one lower-case character.
  - At least one upper-case character.
  - At least one number.
  - At least one special character from the following set of characters:
    - !@#$%^&*()-_=+[];:'",.
  - The following characters are not allowed:
    - {}<>?/\|`~
- After receiving the password, the program should determine if it is valid.
  - If it is not valid, inform the user, and request them to enter the password again.
  - If it is valid, inform the user, and exit the program.

This will require you use a few functions and keywords that you may not be familiar with. To help things along, I've included documentation to some useful things, please take a look:
- `in` keyword: https://www.w3schools.com/python/ref_keyword_in.asp
- `len` function: https://www.w3schools.com/python/ref_func_len.asp
