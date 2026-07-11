"""" Given sn integer array nums and an integer k,
return the kth largest element in the array.

Note that it is the kth largest element in the sorted order,
not the kth distinct element

Solving without sorting.

Example:
Input: nums =[3,2,1,5,6,4], k = 2
Output: 5

Avoid using O(nlogn) solution
Trick/Hint: Use MIN HEAP
"""

# Import heapq so we can use Python's heap operations; 
# alternative: use a regular list and sort it.
import heapq  

# Define a class that groups the solution method; alternative: use a standalone function.
class Solution:  
    def findKthLargest(self, nums, k):  # Define the method that finds the kth largest value; alternative: write the logic outside the class.
        heap = []  # Create an empty list that will act as a min-heap; alternative: use a different data structure such as a sorted list.

        for num in nums:  # Loop through each number in the input array; alternative: use indexing with a range loop.
            heapq.heappush(heap, num)  # Add the current number to the heap so the smallest value stays at the front; alternative: use append() and then heapify().
            if len(heap) > k:  # Keep only the k largest values seen so far; alternative: store all values and sort later.
                heapq.heappop(heap)  # Remove the smallest value when the heap grows larger than k; alternative: use a sorted list and pop the smallest entry.

        return heap[0]  # Return the smallest value in the heap, which is the kth largest element; alternative: return sorted(nums)[-k].

# Better approach: the heap-based solution is better because it runs in O(n log k) time,
# which is more efficient than sorting the whole array in O(n log n) when k is much smaller than n.
# It also uses only O(k) extra space, which is better for large inputs.
#
# Alternative approach:
# def findKthLargestAlternative(nums, k):
#     sorted_nums = sorted(nums)
#     return sorted_nums[-k]
#
# Why this alternative is worse:
# - It sorts the full list, so it takes O(n log n) time.
# - It uses more memory and is slower for large arrays.


