class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        Generate the FizzBuzz sequence from 1 to n.

        Problem:
            For each integer from 1 to n:
            - If divisible by 3 and 5, add "FizzBuzz" to the list.
            - If divisible by 3 only, add "Fizz".
            - If divisible by 5 only, add "Buzz".
            - Otherwise, add the number itself as a string.

        Approach:
            Iterate through numbers from 1 to n.
            Use modulo operations to check divisibility by 3 and 5.
            Append the appropriate string to the result list for each number.

        Time Complexity:
            O(n) — each number from 1 to n is processed exactly once.

        Space Complexity:
            O(n) — storing n strings in the output list.
        """
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer
