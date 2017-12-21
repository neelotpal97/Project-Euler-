
# coding: utf-8

# # Sum square difference
# ## Problem 6
# 
# ### The sum of the squares of the first ten natural numbers is,
# ### 12 + 22 + ... + 102 = 385
# 
# ### The square of the sum of the first ten natural numbers is,
# ### (1 + 2 + ... + 10)2 = 552 = 3025
# 
# ### Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# 
# ### Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# 
# 

# In[7]:

def sum_of_square(n):
    answer = 0
    for i in range(1,n + 1):
        answer = answer + i**2
    return answer

def square_of_sum(n):
    answer = (n * (n + 1)) / 2
    return int(answer**2)

print(square_of_sum(100) - sum_of_square(100))

