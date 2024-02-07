"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

"""

Approach :
We observe that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center, and there are only 2n - 1 such centers.
You might be asking why there are 2n - 1 but not n centers? The reason is the center of a palindrome can be in between two letters. Such palindromes have even number of letters (such as "abba") and its center are between the two 'b's.'
Since expanding a palindrome around its center could take O(n) time, the overall complexity is O(n^2).
Algorithm :
At starting we have maz_str = s[0] and max_len = 1 as every single character is a palindrome.
Now, we will iterate over the string and for every character we will expand around its center.
For odd length palindrome, we will consider the current character as the center and expand around it.
For even length palindrome, we will consider the current character and the next character as the center and expand around it.
We will keep track of the maximum length and the maximum substring.
Print the maximum substring.
Complexity Analysis
Time complexity : ***O(n^2)***. Since expanding a palindrome around its center could take O(n) time, the overall complexity is O(n^2).

Space complexity : ***O(1)***.
"""



def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def find(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        res = ""right
        for i in range(len(s)):
            len1 = find(i,i)
            len2 = find(i,i+1)
            if len(len1) >+ len(res):
                res = len1
            if len(len2) > len(res):
                res = len2
        return res
