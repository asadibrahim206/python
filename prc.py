# 7. Replace 'not'...'poor' with 'good'.

# Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

str =  'google.com'
elem = {}

for i in str:
    keys = elem.keys()
    if i in keys:
        elem[i] += 1
    else:
        elem[i] = 1

print(elem)