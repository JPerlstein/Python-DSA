class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        """
        Problem: Verifying an Alien Dictionary (LeetCode 953)

        Description:
        You are given a list of strings `words` and a string `order` that represents
        the order of characters in an alien language.

        Your task is to determine if the list of words is sorted lexicographically
        according to this custom alien alphabet.

        Rules:
        - Compare words character by character.
        - The first differing character determines ordering.
        - If all characters match up to the length of the shorter word,
          then the shorter word should come first (prefix rule).

        Approach:
        1. Build a hashmap (rank) that maps each character in `order` to its index.
        2. Compare each adjacent pair of words.
        3. For each pair, compare characters until:
           - A mismatch is found → use rank to decide order.
           - No mismatch → check prefix condition.

        Time Complexity:
        O(N * M)
        - N = number of words
        - M = average length of each word
        - In worst case, compare every character of each adjacent pair.

        Space Complexity:
        O(1)
        - The rank dictionary stores at most 26 characters (constant space).
        """

        # storing each char from alien alphabet as key
        # position in the given order stored as value (its index)
        rank = {}

        # build mapping of character -> its order index
        for i, character in enumerate(order):
            rank[character] = i

        # compare each adjacent pair of words
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            # compare characters one by one
            for j in range(min(len(w1), len(w2))):
                character1 = w1[j]
                character2 = w2[j]

                # if mismatch found, compare their ranks
                if character1 != character2:
                    # wrong order → return False
                    if rank[character1] > rank[character2]:
                        return False
                    # correct order → stop checking this pair
                    break
            else:
                # runs only if loop didn't break (all chars matched)
                # check prefix case: longer word first → invalid
                if len(w1) > len(w2):
                    return False

        # all pairs valid
        return True
