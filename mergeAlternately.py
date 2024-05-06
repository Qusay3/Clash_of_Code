''' You are given two strings word1 and word2. Merge the strings by adding letters
    in alternating order, starting with word1. If a string is longer than the other, 
    append the additional letters onto the end of the merged string.
    Return the merged string.

    Input: word1 = "abc", word2 = "pqr"
    Output: "apbqcr"
    Explanation: The merged string will be merged as so:
    word1:  a   b   c
    word2:    p   q   r
    merged: a p b q c r
 
    Constraints:

    1 <= word1.length, word2.length <= 100
    word1 and word2 consist of lowercase English letters.

'''

def mergeAlternately(word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1 = str.lower(input("Enter the first word:  "))
        word2 = str.lower(input("Enter  the Second word:  "))
        
        count = ""
        if len(word1) == len(word2): 
            
            for i in range (0, len(word1)):
                for j in range (0, len(word2)):

                    merged = print((word1[i]) + str(word2[j]))

                    count += 1
        return merged
mergeAlternately("aaaa", "cccc")
