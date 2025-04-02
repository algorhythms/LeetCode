"""
A kingdom consists of a king, his children, his grandchildren, and so on. Every once in a while, someone in the family dies or a child is born.

The kingdom has a well-defined order of inheritance that consists of the king as the first member. Let's define the recursive function Successor(x, curOrder), which given a person x and the inheritance order so far, returns who should be the next person after x in the order of inheritance.

Successor(x, curOrder):
    if x has no children or all of x's children are in curOrder:
        if x is the king return null
        else return Successor(x's parent, curOrder)
    else return x's oldest child who's not in curOrder
For example, assume we have a kingdom that consists of the king, his children Alice and Bob (Alice is older than Bob), and finally Alice's son Jack.

In the beginning, curOrder will be ["king"].
Calling Successor(king, curOrder) will return Alice, so we append to curOrder to get ["king", "Alice"].
Calling Successor(Alice, curOrder) will return Jack, so we append to curOrder to get ["king", "Alice", "Jack"].
Calling Successor(Jack, curOrder) will return Bob, so we append to curOrder to get ["king", "Alice", "Jack", "Bob"].
Calling Successor(Bob, curOrder) will return null. Thus the order of inheritance will be ["king", "Alice", "Jack", "Bob"].
Using the above function, we can always obtain a unique order of inheritance.

Implement the ThroneInheritance class:

ThroneInheritance(string kingName) Initializes an object of the ThroneInheritance class. The name of the king is given as part of the constructor.
void birth(string parentName, string childName) Indicates that parentName gave birth to childName.
void death(string name) Indicates the death of name. The death of the person doesn't affect the Successor function nor the current inheritance order. You can treat it as just marking the person as dead.
string[] getInheritanceOrder() Returns a list representing the current order of inheritance excluding dead people.
 

Example 1:

Input
["ThroneInheritance", "birth", "birth", "birth", "birth", "birth", "birth", "getInheritanceOrder", "death", "getInheritanceOrder"]
[["king"], ["king", "andy"], ["king", "bob"], ["king", "catherine"], ["andy", "matthew"], ["bob", "alex"], ["bob", "asha"], [null], ["bob"], [null]]
Output
[null, null, null, null, null, null, null, ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"], null, ["king", "andy", "matthew", "alex", "asha", "catherine"]]

Explanation
ThroneInheritance t= new ThroneInheritance("king"); // order: king
t.birth("king", "andy"); // order: king > andy
t.birth("king", "bob"); // order: king > andy > bob
t.birth("king", "catherine"); // order: king > andy > bob > catherine
t.birth("andy", "matthew"); // order: king > andy > matthew > bob > catherine
t.birth("bob", "alex"); // order: king > andy > matthew > bob > alex > catherine
t.birth("bob", "asha"); // order: king > andy > matthew > bob > alex > asha > catherine
t.getInheritanceOrder(); // return ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
t.death("bob"); // order: king > andy > matthew > bob > alex > asha > catherine
t.getInheritanceOrder(); // return ["king", "andy", "matthew", "alex", "asha", "catherine"]
 

Constraints:

1 <= kingName.length, parentName.length, childName.length, name.length <= 15
kingName, parentName, childName, and name consist of lowercase English letters only.
All arguments childName and kingName are distinct.
All name arguments of death will be passed to either the constructor or as childName to birth first.
For each call to birth(parentName, childName), it is guaranteed that parentName is alive.
At most 10^5 calls will be made to birth and death.
At most 10 calls will be made to getInheritanceOrder.
"""
from collections import defaultdict


class ThroneInheritanceBruteForce:

    def __init__(self, kingName: str):
        self.root = kingName
        self.deleted = set()
        self.G = defaultdict(list)
        self.P = defaultdict(str)

    def birth(self, parentName: str, childName: str) -> None:
        self.G[parentName].append(childName)
        self.P[childName] = parentName

    def death(self, name: str) -> None:
        self.deleted.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order = []
        self.succeed(self.root, order, defaultdict(bool))
        
        ret = []
        for e in order:
            if e not in self.deleted:
                ret.append(e)
        
        return ret

    def succeed(self, cur, order, visited):
        if not visited[cur]:
            order.append(cur)
            visited[cur] = True
            
        valid = False
        for c in self.G[cur]:
            if not visited[c]:
                valid = True
                self.succeed(c, order, visited)
        
        if not valid:
            if cur == self.root:
                return
            self.succeed(self.P[cur], order, visited)


class ThroneInheritance:
    def __init__(self, kingName: str):
        self.root = kingName
        self.deleted = set()
        self.G = defaultdict(list)

    def birth(self, parentName: str, childName: str) -> None:
        self.G[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deleted.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order = []
        self.succeed(self.root, order, defaultdict(bool))
        return order

    def succeed(self, cur, order, visited):
        if cur not in self.deleted:
            order.append(cur)

        visited[cur] = True
        for c in self.G[cur]:
            if not visited[c]:
                self.succeed(c, order, visited)

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()