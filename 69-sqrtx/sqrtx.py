class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # 0 -> 0, 1 -> 1

        left, right = 1, x // 2
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid

            if sq == x:
                return mid
            elif sq < x:
                ans = mid       # mid^2 < x, candidate
                left = mid + 1  # search right half
            else:
                right = mid - 1 # search left half

        return ans  # floor(sqrt(x))
