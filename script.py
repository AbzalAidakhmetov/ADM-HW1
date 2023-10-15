#Problem 1
#Say "Hello, World!" With Python
print("Hello, World!")

#Python If-Else

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

if n % 2 == 1:
    print('Weird')
elif n % 2 == 0 and 2 <= n <= 5:
    print('Not Weird')
elif n % 2 == 0 and 6 <= n <= 20:
    print('Weird')
elif n % 2 == 0 and n >= 21:
    print('Not Weird')

#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a+b)
print(a-b)
print(a*b)

#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a//b)
print(a/b)

#Write a function
def is_leap(year):
    leap = False

    # Check if the year is evenly divisible by 4
    if year % 4 == 0:
        leap = True

        # Check if the year is evenly divisible by 100
        if year % 100 == 0:
            leap = False

            # Check if the year is evenly divisible by 400
            if year % 400 == 0:
                leap = True

    return leap


year = int(input())
print(is_leap(year))

#Print Function
if __name__ == '__main__':
    n = int(input())
    
out = str()
for i in range(n+1):
    out += str(i)
print(int(out))

#sWAP cASE
def swap_case(s):
    return

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#No Idea!
# Read input values
n, m = map(int, input().split())  # Read n and m
arr = list(map(int, input().split()))  # Read the array as a list

like_set = set(map(int, input().split()))  # Read the "like" set
dislike_set = set(map(int, input().split()))  # Read the "dislike" set

happiness = 0

# Calculate the happiness by iterating through the array
for num in arr:
    if num in like_set:
        happiness += 1
    elif num in dislike_set:
        happiness -= 1

print(happiness)

#Problem 2
#Birthday-cake candles
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    max_num = max(candles)
    return candles.count(max_num)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


#Number Line Jumps

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    deltax = x1 - x2
    deltav = v2 - v1

    if deltav == 0:
        if deltax == 0:
            return 'YES'  
        else:
            return 'NO'   

    if deltax % deltav == 0 and deltax // deltav >= 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#Viral Advertising
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    likes = 0
    people = 5
    for i in range(n):
        daylikes = math.floor(people/2)
        likes += daylikes
        people = daylikes * 3
    return likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


#Recursive Digit Sum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    s = 0
    for j in n:
        s += int(j)
    s = s*k
    
    if len(str(s)) == 1:
        return int(s)
    else:
        return superDigit(str(s), 1)
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


#Insertion Sort - Part 1
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Initialize the index for the element to be inserted and the key to be inserted.
    j = n - 1
    key = arr[j]
    
    # Start comparing elements to find the correct position for the key.
    i = j - 1
    while i >= 0 and arr[i] > key:
        # Shift elements to the right if they are greater than the key.
        arr[i + 1] = arr[i]
        i = i - 1
        
        # Display the array at each step for visualization.
        print(" ".join(map(str, arr)))
    
    # Insert the key into the appropriate position in the array.
    arr[i + 1] = key
    
    # Print the array after inserting the key.
    print(" ".join(map(str, arr)))



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


#Insertion Sort - Part 2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Iterate through the elements of the array.
    for j in range(1, n):
        # Get the current element as the key.
        key = arr[j]
        
        # Start comparing with elements to the left of the key.
        i = j - 1
        while i >= 0 and arr[i] > key:
            # Shift elements to the right if they are greater than the key.
            arr[i + 1] = arr[i]
            i = i - 1
        
        # Insert the key into the appropriate position.
        arr[i + 1] = key
        
        # Display the array at each step for visualization.
        print(" ".join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
