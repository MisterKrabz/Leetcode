class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26

        for task in tasks:
            index = ord(task) - ord("A")
            counts[index] += 1

        max_freq = max(counts)
        max_count = 0

        for count in counts:
            if count == max_freq:
                max_count += 1

        forced_length = (max_freq - 1) * (n + 1) + max_count

        return max(len(tasks), forced_length)
