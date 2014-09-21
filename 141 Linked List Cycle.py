"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""
__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        """
        if extra space available, use hash table
        if not, use the model of Hare and Tortoise
        Algorithm:
        Hare & Tortoise
        Physics, relative velocity.
                                       ___-------___
                                   _-~~             ~~-_
                                _-~                    /~-_
             /^\__/^\         /~  \                   /    \
           /|  O|| O|        /      \_______________/        \
          | |___||__|      /       /                \          \
          |          \    /      /                    \          \
          |   (_______) /______/                        \_________ \
          |         / /         \                      /            \
           \         \^\\         \                  /               \     /
             \         ||           \______________/      _-_       //\__//
               \       ||------_-~~-_ ------------- \ --/~   ~\    || __/
                 ~-----||====/~     |==================|       |/~~~~~
                  (_(__/  ./     /                    \_\      \.
                         (_(___/                         \_____)_)

        :param head: ListNode
        :return: boolean
        """
        hare = head
        tortoise = head
        while hare and hare.next and tortoise:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare==tortoise:
                return True

        return False
