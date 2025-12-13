def knapsack_01_topdown(weights, profits, capacity):
    """
    0/1 Knapsack: Each item can be used at most once
    """
    n = len(weights)
    memo = {}
    
    def dp(i, remain):
        # Base case: no more items
        if i == n:
            return 0
        
        # Base case: no capacity
        if remain <= 0:
            return 0
        
        # Check cache
        if (i, remain) in memo:
            return memo[(i, remain)]
        
        # Option 1: Skip item i
        skip = dp(i + 1, remain)
        
        # Option 2: Take item i (if it fits)
        take = 0
        if weights[i] <= remain:
            take = profits[i] + dp(i + 1, remain - weights[i])
        
        # Recurrence: max(skip, take)
        memo[(i, remain)] = max(skip, take)
        return memo[(i, remain)]
    
    return dp(0, capacity)	
