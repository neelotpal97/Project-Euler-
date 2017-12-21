
# coding: utf-8

# # Largest prime factor
# ## Problem 3
# 
# ### The prime factors of 13195 are 5, 7, 13 and 29.
# 
# ### What is the largest prime factor of the number 600851475143 ?
# 

# In[1]:

num = 600851475143
factor = 2 
while num > 1:
    while num % factor == 0:
        num = num//factor
    factor+=1

print(factor - 1)
# This is a very elegant solution I found on the internet. My approach was a computation nightmare.

