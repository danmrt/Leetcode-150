#Leetcode Problem 2 Add two numbers

#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Example 1

#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.

#Example 3

#Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
#Output: [8,9,9,9,0,0,0,1]



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = ListNode()
        current = head
        carry = 0

        while l1 or l2 or carry: #while l1 is NOT NULL or l2 is NOT NULL or carry > 0
            value_l1 = l1.val if l1 else 0
            value_l2 = l2.val if l2 else 0

            #add both values
            combined_values = value_l1 + value_l2 + carry
            carry = combined_values // 10
            combined_values = combined_values % 10
            current.next = ListNode(combined_values)


            #keep going through the linked lists, update the pointers
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next
            
