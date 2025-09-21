'''
@ASSESSME.USERID: Faris Karić
@ASSESSME.AUTHOR: author, list of authors
@ASSESSME.DESCRIPTION: Assignment 3.1
@ASSESSME.ANALYZE: YES
'''

import math

def fact(x):
    if x>0:
        return math.factorial(int(x))
    else:
        return 0
    

def root(x):
    if x>0:
        return math.sqrt(float(x))
    else:
        return 0
    

def trunk(x):
    return math.trunc(x)



def main():
   numeric_value = int(input("Enter a numeric value: "))
   print(f"{numeric_value} factorial = {fact(numeric_value)}")

   numeric_value = float(input("Enter a numeric value: "))
   print(f"The square root of {numeric_value} = {root(numeric_value)}")

   numeric_value = float(input("Enter a numeric value: "))
   print(f"{numeric_value} truncated = {trunk(numeric_value)}")



if __name__ == "__main__":
    main()