class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        b1 = None
        b2 = None

        last1 = -1
        last2 = -1

        left = 0
        longest = 0

        for right, fruit in enumerate(fruits):
            if fruit == b1:
                last1 = right

            elif fruit == b2:
                last2 = right

            elif b1 is None:
                b1 = fruit
                last1 = right

            elif b2 is None:
                b2 = fruit
                last2 = right

            else:
                if last1 < last2:
                    left = last1 + 1
                    b1 = fruit
                    last1 = right
                else:
                    left = last2 + 1
                    b2 = fruit
                    last2 = right

            longest = max(longest, right - left + 1)

        return longest
