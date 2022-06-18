"""
https://www.tutorialspoint.com/program-to-find-sum-of-minimum-trees-from-the-list-of-leaves-in-python
Purpose : find the sum of minimum trees from the list of leaves in python
"""
class Solution:
   def solve(self, nums):
      res = sum(nums)
      while len(nums) > 1:
         i = nums.index(min(nums))
         left = nums[i - 1] if i > 0 else float("inf")
         right = nums[i + 1] if i < len(nums) - 1 else float("inf")
         res += min(left, right) * nums.pop(i)

      return res

ob = Solution()
nums = [3, 5, 10]
print(ob.solve(nums))