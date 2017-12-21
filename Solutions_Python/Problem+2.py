
# coding: utf-8

# # Even Fibonacci numbers
# ## Problem 2
# 
# ### Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 
# ### 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 
# ### By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
# 

# In[2]:

def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)

answer = 0
for i in range(1,100):
    if(fib(i) > 4000000):
        break
    elif(fib(i)%2 == 0):
        answer += fib(i)
    else:
        continue

print(answer)

        

