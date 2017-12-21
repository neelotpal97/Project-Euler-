
# coding: utf-8

# # Largest palindrome product
# ## Problem 4
# 
# ### A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# ### Find the largest palindrome made from the product of two 3-digit numbers.
# 

# In[20]:

answer = []
for i in range(999,99,-1):
    for j in range(999,99,-1):
        k = str(i*j)
        if k == k[::-1]:
            #print(k)
            answer.append(i*j)
print(max(answer))
"""I got confudes using the max funtion, also, the solution was right all along I just had to sort the array I was getting."""

