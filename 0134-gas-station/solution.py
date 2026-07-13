class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        current_tank = 0
        start = 0

        for i in range(len(gas)):
            difference = gas[i] - cost[i]

            total_gas += difference
            current_tank += difference

            if current_tank < 0:
                start = i + 1
                current_tank = 0

        return start if total_gas >= 0 else -1
        


