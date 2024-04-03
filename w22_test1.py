list = [1, 2, 3, 4, 5, 6, 7, 8]

# Question 0: Make a function that take a list and replaces every element with "banana".
def banana(list):
    n = 0
    while n<len(list):
        list[n] = 'banana'
        n += 1
    return list
print(banana(list))

# Question 1:Create a function that squares each number in the list using a for loop. If there is a multiple of five in the list, return 'bingo' instead of squaring the number.
#Assume all items in the list are numbers.

def square(list):
    newl = []
    for e in list:
        if list[e]%5 == 0:
            return bingo
        else:
            list[e]**2
        n += 1
    return list
print(square(list))


# Question 2: Let g = [1, 3, 7, 8, 10, 15, 32, 41, 52], using a for loop, make a new list consisting of all the even numbers from the original list.
g = [1, 3, 7, 8, 10, 15, 32, 41, 52]
def evens(g):
    newl = []
    for e in g:
        if e%2 == 0:
            newl.append(e)
    return newl
print(evens(g))

            
# Question 3: Write a function that takes a list of list of strings of lowercase letters that returns the list with every element of every other list capitalized. [['a', 'b', 'c'], ['d', 'e', 'f'], ['j', 'k', 'l']]
g = [['a', 'b', 'c'], ['d', 'e', 'f'], ['j', 'k', 'l']]
'''
def capital(g):
    n = 0
    i = 0
    while n<len(g):
        if n%2 == 0:
            while i<len(g):
                diff = ord('A') - ord('a')
                g[n[i]] = chr(ord(g[n[i]]) + diff)
                i += 1
        n += 1
    return g
print(capital(g))
            '''
