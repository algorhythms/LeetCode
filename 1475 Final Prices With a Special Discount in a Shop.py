"""
You are given an integer array prices where prices[i] is the price of the ith item in a shop.

There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.

 

Example 1:

Input: prices = [8,4,6,2,3]
Output: [4,2,4,2,3]
Explanation: 
For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
For items 3 and 4 you will not receive any discount at all.
Example 2:

Input: prices = [1,2,3,4,5]
Output: [1,2,3,4,5]
Explanation: In this case, for all items, you will not receive any discount at all.
Example 3:

Input: prices = [10,1,1,6]
Output: [9,0,1,6]
 

Constraints:

1 <= prices.length <= 500
1 <= prices[i] <= 1000
"""
class Solution:
    def finalPrices_error(self, A: List[int]) -> List[int]:
        """
        Brute force O(N^2)

        Maintain a stack from the right, keep the earliest minmum value at the top of the stk
        Stk is monotonic decreasing
        """
        R = []
        N = len(A)
        stk = []
        for i in range(N-1, -1, -1):
            if not stk or A[stk[-1]] > A[i]:
                stk.append(i)
        
        for i in range(N):
            while stk and stk[-1] <= i:
                stk.pop()
            price = A[i]
            if stk and A[stk[-1]] < A[i]:
                price -= A[stk[-1]]
            R.append(price)

        return R
    
    def finalPrices(self, A: List[int]) -> List[int]:
        """
        Brute force O(N^2)

        Find the next closest smaller element 
          -> Find the previous closest larger element
        """
        N = len(A)
        R = [0 for _ in range(N)]
        stk = []  # store the previous, monotonic increasing
        for i in range(N):
            while stk and A[stk[-1]] >= A[i]:
                prev = stk.pop()
                R[prev] = A[prev] - A[i]
            stk.append(i)
        
        for i in stk:
            R[i] = A[i]

        return R

