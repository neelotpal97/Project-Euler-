
# coding: utf-8

# # 10001st prime
# ## Problem 7
# 
# ### By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# ### What is the 10 001st prime number?
# 

# In[1]:

def is_prime(n):
	for i in range(2,n):
		if n%i == 0:
			return False
	return True

natural_number = 3
n = [2]
while(len(n) < 10001):
	if is_prime(natural_number):
		n.append(natural_number)
		natural_number += 1 
	natural_number += 1

print(n)
print(len(n))

