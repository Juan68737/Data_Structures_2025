def knapsack_unbounded_topdown(weights, profits, capacity):
    """
    Unbounded Knapsack: Each item can be used unlimited times
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
        
        # Option 1: Skip this item type entirely
        skip = dp(i + 1, remain)
        
        # Option 2: Take this item (can take again!)
        take = 0
        if weights[i] <= remain:
            # KEY DIFFERENCE: dp(i, ...) instead of dp(i+1, ...)
            take = profits[i] + dp(i, remain - weights[i])
        
        # Recurrence: max(skip, take)
        memo[(i, remain)] = max(skip, take)
        return memo[(i, remain)]
    
    return dp(0, capacity)
