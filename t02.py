"""
MC Question:
Given: a.join(h), identify a

Options:
A) the source string
B) the source list
C) the string placed between elements of h
D) the string that separates elements of h
Answer: C

=======================
Programming question:

s = "hi my name is bob"
Write a function to separate each word by a comma and a space instead of just a space.

Possible solution:
=======================
"""
def comma(s):
    s = s.split(" ")
    s = ", ".join(s)
    return s
print(comma("hi my name is bob"))
