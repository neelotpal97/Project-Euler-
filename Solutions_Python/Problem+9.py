
# coding: utf-8

# # Special Pythagorean triplet
# ## Problem 9
# 
# ### A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# ### a2 + b2 = c2
# 
# ### For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# ### There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# ### Find the product abc.
# 

# In[26]:

def is_pythagorean(n):
    if len(n) != 3:
        return False
    else:
        n.sort()
        if (n[2]**2 == n[1]**2 + n[0]**2):
            return True
        return False


# In[27]:

def looper(a):
    for a in range(a,0,-1):
        for b in range(a-1 ,0,-1):
            for c in range(a-2,0,-1):
                possible_answer = []
                possible_answer.append(c)
                possible_answer.append(b)
                possible_answer.append(a)
                if is_pythagorean(possible_answer) and (possible_answer[0] + possible_answer[1] + possible_answer[2] == 1000):
                    return possible_answer
    return "Not Pair found"

answer = looper(900)
print(answer)
print(answer[0]*answer[1]*answer[2])

