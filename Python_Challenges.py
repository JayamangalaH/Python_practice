'''
Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.

Your function should return the number of people who are online.
'''

statuses = {"Alice": "online", "Bob": "offline", "Eve": "online"}
def online_count(dict1):
    c = 0
    for key,value in dict1.items():
        if dict1[key] == "online":
            c = c + 1
    return c

print(online_count(statuses))

'''
Define a function named count that takes a single parameter. The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these:

"ho-tel"
"cat"
"met-a-phor"
"ter-min-a-tor"
Your function should count the number of syllables and return it.

For example, the call count("ho-tel") should return 2.
'''

def count(c):
    return len(c.split(sep='-'))

print(count('ho-tel'))


'''
Anagrams
Two strings are anagrams if you can make one from the other by rearranging the letters.

Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.

For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.
'''


'''
Flatten a list
Write a function that takes a list of lists and flattens it into a one-dimensional list.

Name your function flatten. It should take a single parameter and return a list.

For example, calling:

flatten([[1, 2], [3, 4]])
Should return the list:

[1, 2, 3, 4]
'''

l2=[1,2,3,4,[5,6]]

def flatten(_list):
    flattened_list = list()
    for i in _list:
    # print("inside i")
        if isinstance(i, int): 
            # print(i)
            flattened_list.append(i)
        if isinstance(i, list):  
            for j in i:
            #   print("inside j")
                # print(j)
                flattened_list.append(j)
    return flattened_list
  
res = flatten(l2)
print(str(res))

'''
Min-maxing
Define a function named largest_difference that takes a list of numbers as its only parameter.

Your function should compute and return the difference between the largest and smallest number in the list.

For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.

You may assume that no numbers are smaller or larger than -100 and 100.

'''
min_max_List = [2,5,3,10]

def largest_difference(_list):
    min_max_list_local = list(_list)
    _max = max(min_max_list_local)
    _min = min(min_max_list_local)
    return (_max-_min)

print(largest_difference(min_max_List))


# divisible by 3 or not


def div_3(number):
    if number % 3 == 0:
        return True
    else:
        return False
    
print(div_3(6))

# palindrome

s = 'abc'
def palindrome(text):
    rev = s[::-1]
    if rev == s:
        return(True)
    else:
        return(False)
        
print(palindrome(s))



'''
Consecutive zeros
The goal of this challenge is to analyze a binary string consisting of only zeros and ones. 
Your code should find the biggest number of consecutive zeros in the string. For example, given the string:

"1001101000110"
The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones.
Your function should return the number described above.
'''

number = "1001101000110"
def consecutive_zeros(text_one_zero):
    l1 = text_one_zero.split('1')
    return(len(max(l1)))

print(consecutive_zeros(number))