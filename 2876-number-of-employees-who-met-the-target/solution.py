class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ret = 0
        for employee in hours: 
            if employee >= target: 
                ret += 1
        return ret
        
