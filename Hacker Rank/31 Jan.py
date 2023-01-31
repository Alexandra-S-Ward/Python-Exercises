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