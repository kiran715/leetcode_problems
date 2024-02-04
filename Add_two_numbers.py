"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

"""
Approach

Initialization: Initialize a dummy node (dummy) and a current pointer (curr) to keep track of the resulting linked list.

Initialization of Variables: Initialize a carry variable to 0 to account for any carry from the addition of digits.

Traverse Linked Lists: Traverse both linked lists (l1 and l2) simultaneously until we reach the end of both lists.

Obtain Values: In each iteration, obtain the values of the current nodes in l1 and l2. If the nodes exist, use their values; otherwise, use 0.

Calculate Sum: Calculate the sum of the values along with the carry from the previous iteration.

Update Carry and Calculate Digit: Update the carry for the next iteration and calculate the new digit to be added to the result.

Create New Node: Create a new node with the calculated digit and update the current pointer.

Move to Next Nodes: Move to the next nodes in both l1 and l2.

Handle Remaining Carry: After the loop, check if there is any remaining carry. If yes, create a new node with the carry.

Return Result: Return the next node of the dummy node, which is the head of the resulting linked list.
"""

def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = dummy
        
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            tot = val1+val2+carry
            
            carry = tot//10
            cur.next = ListNode(tot%10)
            cur = cur.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
