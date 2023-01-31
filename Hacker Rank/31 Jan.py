# // Hello World
if __name__ == '__main__':
    print("Hello, World!")

# // Python If/Else
#!/bin/python3

import math
import os
import random
import re
import sys

def is_even(item):
    return item % 2 == 0

def is_weird(n):
    if not is_even(n):
        print("Weird")
        return
    elif 2 <= n <= 5:
        print("Not Weird")
	return
    elif 6 <= n <= 20:
        print("Weird")
	return
    elif 20 < n:
        print("Not Weird")
        return
if __name__ == '__main__':
    n = int(input().strip())
    is_weird(n)

# // Print Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

# // Leap year test
def is_leap(year):    
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 100 == 0 and year % 400 == 0:
                return True
            elif year % 100 == 0 and year % 400 != 0:
                return False
            else:
                return False
        return True
    else:
        return False

# // Print number from string
if __name__ == '__main__':
    n = int(input())
    string = ""
    for i in range(n):
        string += str(i + 1)
    print(string)

# // Designer Door Mat
n,m=map(int,input().split()) # // Get the inputs

for i in range(1,n,2):
    print((i*'.|.').center(m,'-')) # // Print the top

print('WELCOME'.center(m,'-')) # // Print the Welcome message

for i in range(n-2,-1,-2):
    print((i*'.|.').center(m,'-')) # // Loop through the bottom, it starts high and gets low

# // Runner up score
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    maxi = arr[n-1]
    mini = arr[0]
    for i in range(n-1, 0, -1):
        if arr[i] < maxi:
            mini = arr[i]
            break
    print(mini)

# //Nested List second runner up
if __name__ == '__main__':
    records = []
    minimum = 0
    for _ in range(int(input())):
        name = input()
        score = float(input())        
        records.append([name,score])
    records.sort(key = lambda x:x[1])
    minimum = records[0][1]
    for i in records: # get second minimum
        if i[1] > minimum:
            minimum = i[1]
            break
    names = [i[0] for i in records if i[1] == minimum]
    for i in sorted(names):
        print(i)

# // Average student score
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum_of_marks = sum(student_marks[query_name])/len(student_marks[query_name])
    print('%.2f' % sum_of_marks)

# regex replacement. DOESNT WORK. IT NEEDS TO BE FIXED. Regex is pain.
#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
lst1 = []
lst2 = []
lst3 = []
for row in matrix:
    lst1.append(row[0])
    lst2.append(row[1])
    lst3.append(row[2])
lst1.extend(lst2)
lst1.extend(lst3)
lst1 = "".join(lst1)
result = re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9\s]+(?=[a-zA-Z0-9])', " ", lst1)
print(result)

# List Comprehension
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
        
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n])

# List Split
def split_and_join(line):
    line = line.split(" ")
    return "-".join(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# String mutation
def mutate_string(string, position, character):
    return f'{string[:position]}{character}{string[position+1:]}'

#Count Substring
def count_substring(string, sub_string):
    cnt = 0
    if sub_string not in string:
        return cnt
    else:
        for i,char in enumerate(string):
            if char == sub_string[0]:
                if string[i:i+len(sub_string)] == sub_string:
                    cnt+=1
        return cnt

# String Validators
if __name__ == '__main__':
    s = input()
    print(True in [c.isalnum() for c in s])
    print(True in [c.isalpha() for c in s])
    print(True in [c.isdigit() for c in s])
    print(True in [c.islower() for c in s])
    print(True in [c.isupper() for c in s])

#Swap Cases
def swap_case(s):
    return "".join([c.upper() if c.islower() else c.lower() for c in s])

# Text justification
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Text Wrap
def wrap(string, max_width):
    wrapped = textwrap.fill(string,max_width)
    return wrapped