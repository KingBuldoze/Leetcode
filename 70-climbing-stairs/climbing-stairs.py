class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n <= 2:
            return n
        
        one_step_before = 2   # ways to reach step 2
        two_steps_before = 1  # ways to reach step 1
        
        # DP iteration from step 3 to n
        for _ in range(3, n + 1):
            current = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = current
        
        return one_step_before
