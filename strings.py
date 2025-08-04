# Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}



# str = "linkedin.com"
# dict = {}
# for i in str:
#     keys = dict.keys()
#     if i in keys:
#         dict[i] += 1
#     else:
#         dict[i]= 1
    
# print(dict)

# 3. Get string of first and last 2 chars.
# Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

# def string_spilt_bothends(str):
#     if len(str) < 2:
#         return ''
#     else:
#         return str[:2] + str[-2:]

# print(string_spilt_bothends("w3resource"))
# 4. Replace first char occurrences with $.
# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

# def change_string_innextoccurance(str):
#     char = str[0]
#     str = str.replace(char,"$")
#     str = char + str[1:]

#     return str
# print(change_string_innextoccurance("restart"))

# 5. Swap first 2 chars of 2 strings.
# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

# def swap_fistTwo_values(str1,str2):
#     new_str1 = str2[:2] + str1[2:]
#     new_str2 = str1[:2] + str2[2:]
#     return (new_str1 + ' ' + new_str2)

# print(swap_fistTwo_values("abc","xyz"))

# 6.Add ing or ly to a string.
# str = input("enter the string : ")
# if len(str) > 2:
#     if str[-3:]:
#         str += "ly"
#         print(str)
#     else:
#         str += "ing"
# else:
#      print(str)

# 7
# Python: Find the first appearance of the substring 'not' and 'poor' from a given string, 
# if 'not' follows the 'poor', 
# replace the whole 'not'...'poor' substring with 'good'. Return the resulting string

# def replace_notandpoor_withgood(str):

#     snot = str.find("not")
#     spoor = str.find("poor")
#     if snot < spoor and snot > 0 and spoor > 0 :
#         str = str.replace(str[snot:spoor+4],"good")
#         return str
#     else:
#         return str

# print(replace_notandpoor_withgood('The lyrics is not that poor!'))
# print(replace_notandpoor_withgood('The lyrics is poor!'))

# 8. Find longest word in a list.

# Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

word_list = ["php","exercise","backend","Computer Science"]
word_len = []

for i in word_list:
    word_len.append((len(i),i))
    word_len.sort()
    result = word_len[-1][1]
    result_len = word_len[-1][0]

print(f"this is the  longest word : {result}")
print(f"this is the length of the longest word : {result_len}")



    