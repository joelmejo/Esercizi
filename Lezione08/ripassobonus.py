## 1
# The Number of Beautiful Subsets: write a function with an array nums of positive integers and a positive
#  integer k given as inputs. A subset of nums is beautiful if it does not contain two integers with an absolute
#  difference equal to k. Return the number of non-empty beautiful subsets of the array nums. A subset of nums
#  is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different
#  if and only if the chosen indices to delete are different.

# Example 1:
# Input: nums = [2,4,6], k = 2
# Output: 4

# Example 2:
# Input: nums = [1], k = 1
# Output: 1


## 2
# Combinations: given two integers n and k, return all possible combinations of k numbers chosen from the
#  range [1, n]. You may return the answer in any order.

# Example 1:
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]


## 3
# Generate Parentheses: Given n pairs of parentheses, write a function to generate all combinations of
#  well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]

def well_parentheses(n: int) -> list[str]:
    if n <= 0:
        print("why")
    parentheses: list[str]= ['(', ')']
    results: list= []

    
    list_result: list= []
    for k in range(n):
        list_result.append(parentheses[0])
        list_result.append(parentheses[1])

    result: str= ''.join(list_result)
    results.append(result)
        
well_parentheses(1)