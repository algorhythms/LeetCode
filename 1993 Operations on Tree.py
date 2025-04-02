"""
You are given a tree with n nodes numbered from 0 to n - 1 in the form of a parent array parent where parent[i] is the parent of the ith node. The root of the tree is node 0, so parent[0] = -1 since it has no parent. You want to design a data structure that allows users to lock, unlock, and upgrade nodes in the tree.

The data structure should support the following functions:

Lock: Locks the given node for the given user and prevents other users from locking the same node. You may only lock a node using this function if the node is unlocked.
Unlock: Unlocks the given node for the given user. You may only unlock a node using this function if it is currently locked by the same user.
Upgrade: Locks the given node for the given user and unlocks all of its descendants regardless of who locked it. You may only upgrade a node if all 3 conditions are true:
The node is unlocked,
It has at least one locked descendant (by any user), and
It does not have any locked ancestors.
Implement the LockingTree class:

LockingTree(int[] parent) initializes the data structure with the parent array.
lock(int num, int user) returns true if it is possible for the user with id user to lock the node num, or false otherwise. If it is possible, the node num will become locked by the user with id user.
unlock(int num, int user) returns true if it is possible for the user with id user to unlock the node num, or false otherwise. If it is possible, the node num will become unlocked.
upgrade(int num, int user) returns true if it is possible for the user with id user to upgrade the node num, or false otherwise. If it is possible, the node num will be upgraded.
 

Example 1:


Input
["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
[[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]
Output
[null, true, false, true, true, true, false]

Explanation
LockingTree lockingTree = new LockingTree([-1, 0, 0, 1, 1, 2, 2]);
lockingTree.lock(2, 2);    // return true because node 2 is unlocked.
                           // Node 2 will now be locked by user 2.
lockingTree.unlock(2, 3);  // return false because user 3 cannot unlock a node locked by user 2.
lockingTree.unlock(2, 2);  // return true because node 2 was previously locked by user 2.
                           // Node 2 will now be unlocked.
lockingTree.lock(4, 5);    // return true because node 4 is unlocked.
                           // Node 4 will now be locked by user 5.
lockingTree.upgrade(0, 1); // return true because node 0 is unlocked and has at least one locked descendant (node 4).
                           // Node 0 will now be locked by user 1 and node 4 will now be unlocked.
lockingTree.lock(0, 1);    // return false because node 0 is already locked.
 

Constraints:

n == parent.length
2 <= n <= 2000
0 <= parent[i] <= n - 1 for i != 0
parent[0] == -1
0 <= num <= n - 1
1 <= user <= 10^4
parent represents a valid tree.
At most 2000 calls in total will be made to lock, unlock, and upgrade.
"""
from collections import defaultdict


class LockingTree:
    def __init__(self, parent: List[int]):
        self.G = defaultdict(list)
        self.P = defaultdict(int)
        for i, p in enumerate(parent):
            if i != 0:
                self.G[p].append(i)
                self.P[i] = p

        self.locks = defaultdict(int)

    def lock(self, num: int, user: int) -> bool:
        if num in self.locks:
            return False
        
        self.locks[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if num in self.locks and self.locks[num] == user:
            del self.locks[num]
            return True

        return False
        
    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locks:
            return False 

        cur = num
        while cur in self.P:
            if self.P[cur] in self.locks:
                return False
            cur = self.P[cur]
        
        for c in self.G[num]:
            if self.dfs(c):
                break  # break for-else statement
        else:
            return False 
        
        self.locks[num] = user
        for c in self.G[num]:
            self.dfs_unlock(c)
            
        return True 

    def dfs(self, cur):
        if cur in self.locks:
            return True
        
        for c in self.G[cur]:
            if self.dfs(c):
                return True
        
        return False

    def dfs_unlock(self, cur):
        if cur in self.locks:
            del self.locks[cur]
        
        for c in self.G[cur]:
            self.dfs_unlock(c)


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)