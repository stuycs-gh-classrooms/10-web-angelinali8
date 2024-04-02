"""
MC Question:
What is the difference between for and while loops?

Options:
A) Only while loops can loop through the whole list
B) You can access the index in a while loop, but not a for loop
C) Only for loops iterate through a list/string one element at a time
D) All of the above

Answer: D

=======================
Programming question:

Given a list of integers, use filter to create a new list of the even integers.
Then use reduce to find the sum of the elements in the new list. (The original list is called g)



Possible solution:
=======================
"""
import functools
g = [1, 2, 3, 4, 5, 6, 7, 8]

evens = filter(lambda x: x % 2 == 0, g)
answer = functools.reduce(lambda x0, x1: x0 + x1, evens)
print(answer)

