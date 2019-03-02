#!/usr/bin/python3
"""
Given a list accounts, each element accounts[i] is a list of strings, where the
first element accounts[i][0] is a name, and the rest of the elements are emails
representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to
the same person if there is some email that is common to both accounts. Note
that even if two accounts have the same name, they may belong to different
people as people could have the same name. A person can have any number of
accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the
first element of each account is the name, and the rest of the elements are
emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John",
"johnnybravo@mail.com"], ["John", "johnsmith@mail.com",
"john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com',
'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary",
"mary@mail.com"]]

Explanation:
The first and third John's are the same person as they have the common email
"johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses
are used by other accounts.
We could return these lists in any order, for example the answer [['Mary',
'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']]
would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
"""
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        merge has to be dfs
        account id
        """
        email_to_ids = defaultdict(set)
        for i, v in enumerate(accounts):
            for email in v[1:]:
                email_to_ids[email].add(i)

        # graph nodes by ids, edges by email
        visited = [False for _ in accounts]
        ret = []
        for i, v in enumerate(accounts):
            if not visited[i]:
                emails = set()
                self.dfs(i, accounts, email_to_ids, emails, visited)
                ret.append([v[0]] + sorted(emails))

        return ret

    def dfs(self, i, accounts, email_to_ids, emails, visited):
        visited[i] = True
        for email in accounts[i][1:]:
            emails.add(email)
            for nbr in email_to_ids[email]:
                if not visited[nbr]:
                    self.dfs(nbr, accounts, email_to_ids, emails, visited)


    def accountsMerge_error(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        data structure
        map: email -> id, if exist mapping, then merge
        map: id -> [email]

        mistake: not dfs, search on the first level
        """
        email_id = {}
        id_emails = defaultdict(list)
        for i in range(len(accounts)):
            person = None
            for email in accounts[i][1:]:
                if email in email_id:
                    person = email_id[email]
                    break

            for email in accounts[i][1:]:
                if person is None:
                    person = i
                    email_id[email] = person
                    id_emails[person].append(email)
                elif email not in email_id:
                    email_id[email] = person
                    id_emails[person].append(email)

        ret = []
        for k, v in id_emails.items():
            ret.append([accounts[k][0]] + sorted(v))

        return ret
