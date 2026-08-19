class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]: 
            return arr[0:k]
        elif x >= arr[-1]: 
            return arr[len(arr) - k:]
        else: 
            low = 0
            high = len(arr) - 1
            point = -1

            while low < high: 
                mid = (high + low) // 2 
                if arr[mid] == x: 
                    point = mid
                    break
                elif low + 1 == high: 
                    if abs(arr[low] - x) <= abs(arr[high] - x):
                        point = low
                    else:
                        point = high
                    break
                elif x > arr[mid]: 
                    low = mid
                else: 
                    high = mid
            
            p1 = max(point - k + 1, 0)
            p2 = p1 + k - 1
            best = float('inf')
            ret_p1 = -1
            ret_p2 = -1
            
            while p2 < len(arr) and p1 <= point: 
                total_dif = 0
                for i in range(p1, p2 + 1): 
                    total_dif += abs(arr[i] - x)
                
                if total_dif < best:  
                    best = total_dif
                    ret_p1 = p1
                    ret_p2 = p2 

                p2 += 1
                p1 += 1
            
            return arr[ret_p1:ret_p2 + 1]

