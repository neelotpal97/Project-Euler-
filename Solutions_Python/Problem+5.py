
# coding: utf-8

# # Smallest multiple
# ## Problem 5
# 
# ### 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# ### What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# 

# In[23]:

def find_multiples(n):
    ans = []
    for j in n:
        for i in range(1,j+1):
            if j%i == 0:
                ans.append(i)
    return ans

        
arr = [x for x in range(1,11)]
ans = (find_multiples(num))
print(ans)

# This was my first approack and you can see that it wrong.


# In[28]:

def check(n):
    for i in range(11,21):
        if n % i == 0:
            continue
        else:
            return False
    return True

num = 2520
while(check(num) == False):
    num+=2520
print(num)

# This is a much more elegant solution.

