#                                                loops 

#QUESTION NO : 1
#PRINT TABLE:
# n = int(input("enter number : "))
# for i in range(1,11):
#     print(f"{n} * {i} = {n * i}")


# QUESTION 2:
# factorial
# n = int(input("enter number : "))
# fact = 1
# for i in range(n,0,-1):
#     fact *= i
# print(fact)

# question 3
# Sum upto n terms
# n = int(input("enter number : "))
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(sum)

# Question 4
# find factors and strong number
# n = int(input("enter number : "))
# sum = 0
# for i in range(1,n):
#     if n % i == 0:
#         sum += i
# if sum == n:
#     print(f"{n}  is strong")
# else:
#     print(f"{n}  is not strong...")


# Question 5
# prime number
# n = int(input("enter number : "))
# count = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         count += 1
# if count > 2:
#     print(f"{n} is a not prime number")
# else:
#     print(f"{n} is a prime number")

# Question 6
# print each number in a new line like
# 123
# 3
# 2
# 1
# n = int(input('ENTER YOUR NUMBER: '))
# while n > 0:
#     print(n%10)
#     n = n//10

# Question 7
# POLLINDROME

# n = int(input('ENTER YOUR NUMBER: '))
# rev = 0
# copy = n
# while n > 0:
#     z= n % 10
#     rev = rev * 10 + z
#     n= n//10
   
# if rev == copy:
#     print("Number is Pollindrome")
# else:
#     print("not pollindrome")

