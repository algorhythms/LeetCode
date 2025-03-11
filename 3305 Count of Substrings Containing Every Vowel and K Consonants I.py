"""
You are given a string word and a non-negative integer k.

Return the total number of 
substrings
 of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

 

Example 1:

Input: word = "aeioqq", k = 1

Output: 0

Explanation:

There is no substring with every vowel.

Example 2:

Input: word = "aeiou", k = 0

Output: 1

Explanation:

The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

Example 3:

Input: word = "ieaouqqieaouqq", k = 1

Output: 3

Explanation:

The substrings with every vowel and one consonant are:

word[0..5], which is "ieaouq".
word[6..11], which is "qieaou".
word[7..12], which is "ieaouq".
 

Constraints:

5 <= word.length <= 250
word consists only of lowercase English letters.
0 <= k <= word.length - 5
"""

from collections import defaultdict


class Solution:
    def countOfSubstrings_error(self, word: str, k: int) -> int:
        """
        sliding window of i, j
        counter of aeiou and consonants counter
        O(N)

        Edge case: "iqeaouqi"
        """
        cons_cnt = 0
        vowel_cnt = defaultdict(int)
        vowels = set([c for c in "aeiou"])
        
        ret = 0
        i = -1  # A[:i]
        j = 0
        for j in range(len(word)):
            char = word[j]
            if char in vowels:
                vowel_cnt[char] += 1
            else:
                cons_cnt += 1

            while i < j and cons_cnt > k:
                i += 1
                remove = word[i]
                if remove in vowels:
                    vowel_cnt[remove] -= 1
                    if vowel_cnt[remove] == 0:
                        del vowel_cnt[remove]
                else:
                    cons_cnt -= 1
            
            if cons_cnt == k and len(vowel_cnt) == 5:
                ret += 1
            
            while i < j and cons_cnt == k:
                i += 1
                remove = word[i]
                if remove in vowels and vowel_cnt[remove] > 1 and len(vowel_cnt) == 5:
                    vowel_cnt[remove] -= 1
                    ret += 1
                else:
                    i -= 1
                    break

        return ret
    
    def countOfSubstrings(self, word: str, k: int) -> int:
        """
        count by number of substrings
        ret += (i - original_i + 1)
        """
        cons_cnt = 0
        vowel_cnt = defaultdict(int)
        vowels = set([c for c in "aeiou"])
        
        ret = 0
        i = -1  # A[:i]
        original_i = -1
        for j in range(len(word)):
            char = word[j]
            if char in vowels:
                vowel_cnt[char] += 1
            else:
                cons_cnt += 1
            
            while i < j and cons_cnt > k:
                i += 1
                remove = word[i]
                if remove in vowels:
                    vowel_cnt[remove] -= 1
                    if vowel_cnt[remove] == 0:
                        del vowel_cnt[remove]
                else:
                    cons_cnt -= 1
                original_i = i

            while i < j and cons_cnt == k:
                i += 1
                remove = word[i]
                if remove in vowels and vowel_cnt[remove] > 1:
                    vowel_cnt[remove] -= 1
                else:
                    i -= 1  # restore
                    break
            
            if cons_cnt == k and len(vowel_cnt) == 5:
                ret += (i - original_i + 1)

        return ret
  