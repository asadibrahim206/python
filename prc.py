# 7. Replace 'not'...'poor' with 'good'.

# Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'



def replace_substring(str):


    snot = str.find("not")
    spoor = str.find("poor")

    if snot < spoor and snot > 0 and spoor > 0:
        str.replace(str[snot:spoor+4],"GOOD")
        return (str.replace(str[snot:spoor+4],"GOOD"))
    else:
        return (str)


print(replace_substring("The lyrics is not that poor!"))
