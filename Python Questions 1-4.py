#!/usr/bin/env python
# coding: utf-8

# ## Question: 1
# 
# 
# You have an input dictionary given,
# 
# input_dict = {"abc":{"def":{"ghi":{"jkl":{"mno":{"pqr":{"stu":{"vwx":{"yz":"you are finally here !!!"}}}}}}}}}
# 
# Task:  You have to write a Python function that will take this input and print it like that,
# 
# output = {"abc":["def","ghi","jkl","mno","pqr","stu","vwx","yz"],
#  "def":["ghi","jkl","mno","pqr","stu","vwx","yz"],
#  "ghi":["jkl","mno","pqr","stu","vwx","yz"],
#  "jkl":["mno","pqr","stu","vwx","yz"],
#  "mno":["pqr","stu","vwx","yz"],
#  "pqr":["stu","vwx","yz"],
#  "stu":["vwx","yz"],
#  "vwx":["yz"],
#  "yz":["you are finally here !!!"]}

# In[1]:


#Answer -
def flatten_dict(input_dict, parent_key='', output_dict=None):
    if output_dict is None:
        output_dict = {}
    for key, value in input_dict.items():
        new_key = parent_key + key
        if isinstance(value, dict):
            flatten_dict(value, new_key + "/", output_dict)
        else:
            output_dict[new_key] = value
    return output_dict

def construct_output(input_dict):
    flattened_dict = flatten_dict(input_dict)
    output = {}
    for key, value in flattened_dict.items():
        keys_list = key.split("/")[:-1]
        for i in range(len(keys_list)):
            new_key = keys_list[i]
            if new_key not in output:
                output[new_key] = keys_list[i+1:]
            else:
                output[new_key].extend(keys_list[i+1:])
    return output

# Example usage:
input_dict = {
    "abc": {
        "def": {
            "ghi": {
                "jkl": {
                    "mno": {
                        "pqr": {
                            "stu": {
                                "vwx": {
                                    "yz": "you are finally here !!!"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

output = construct_output(input_dict)
print(output)


# ### Question -2 Given an array of length ‘N’, where each element denotes the position of a stall. Now you have ‘N’ stalls and an integer ‘K’ which denotes the number of horses that are mad. To prevent the horses from hurting each other, you need to assign the horses to the stalls, such that the minimum distance between any two of them is as large as possible. Return the largest minimum distance.
# 
# array: 1,2,4,8,9  &  k=3
# 
# O/P: 3
# 
# Explanation: 1st horse at stall 1, 2nd horse at stall 4 and 3rd horse at stall 8
# 

# In[2]:


#Answer
def count_horses(stalls, distance):
    count = 1
    last_stall = stalls[0]
    for stall in stalls:
        if stall - last_stall >= distance:
            count += 1
            last_stall = stall
    return count

def max_min_distance(stalls, k):
    stalls.sort()
    low = 1
    high = stalls[-1] - stalls[0]
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if count_horses(stalls, mid) >= k:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result

# Example usage:
stalls = [1, 2, 4, 8, 9]
k = 3
print(max_min_distance(stalls, k))  # Output: 3


# ### Question -3 Mr. Karthiken works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
# 
#              a) Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
#               b) The design should have ‘WELCOME’ written in the center.
#               c) The design pattern should only use |, . and – characters.

# In[4]:


#Ans-
def print_door_mat(N, M):
    pattern = [('.|.' * (2*i + 1)).center(M, '-') for i in range(N//2)]
    welcome_line = 'WELCOME'.center(M, '-')
    door_mat = pattern + [welcome_line] + pattern[::-1]
    for line in door_mat:
        print(line)

# Example usage:
N = 7
M = 21
print_door_mat(N, M)


# ### Question: 4
# 
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 
#    a) 0 <= a, b, c, d < n
#    b) a, b, c, and d are distinct.
#    c) nums[a] + nums[b] + nums[c] + nums[d] == target

# In[5]:


# Answer
def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return result

# Example usage:
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]


# In[ ]:




