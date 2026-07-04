/*
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Topic: Array, Hash Map
Approach: Store each number's complement in a hash map while scanning once;
          if the current number's complement was already seen, return indices.
Time: O(n)
Space: O(n)
*/

using System;
using System.Collections.Generic;

public class Solution
{
    public int[] TwoSum(int[] nums, int target)
    {
        var seen = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++)
        {
            int complement = target - nums[i];
            if (seen.ContainsKey(complement))
            {
                return new int[] { seen[complement], i };
            }
            seen[nums[i]] = i;
        }
        return Array.Empty<int>();
    }

    public static void Main(string[] args)
    {
        var sol = new Solution();
        int[] nums = { 2, 7, 11, 15 };
        int target = 9;
        int[] result = sol.TwoSum(nums, target);
        Console.WriteLine($"[{result[0]}, {result[1]}]"); // Expected: [0, 1]
    }
}
