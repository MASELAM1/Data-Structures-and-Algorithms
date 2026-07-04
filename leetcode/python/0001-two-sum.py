"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Topic: Array, Hash Map
Approach: Store each number's complement in a hash map while scanning once;
          if the current number's complement was already seen, return indices.
Time: O(n)
Space: O(n)
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # Expected: [0, 1]
