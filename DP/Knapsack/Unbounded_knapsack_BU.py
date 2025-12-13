def knapsack_unbounded_bottomup(weights, profits, capacity):
    """
    Unbounded Knapsack: Each item can be used unlimited times
    """
    n = len(weights)
    
    # dp[i][w] = max profit using items 0..i-1 with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Option 1: Skip this item type
            dp[i][w] = dp[i-1][w]
            
            # Option 2: Take this item (can take multiple times!)
            if weights[i-1] <= w:
                # Recurrence: dp[i][w] = max(dp[i-1][w], dp[i][w - weights[i-1]] + profits[i-1])
                # KEY DIFFERENCE: dp[i][...] instead of dp[i-1][...] for unbounded
                dp[i][w] = max(dp[i][w], dp[i][w - weights[i-1]] + profits[i-1])
    
    return dp[n][capacity]


# Space-optimized O(capacity) version:
def knapsack_unbounded_optimized(weights, profits, capacity):
    dp = [0] * (capacity + 1)
    
    for i in range(len(weights)):
        # Iterate FORWARDS to allow reusing same item
        for w in range(weights[i], capacity + 1):
            # Recurrence: dp[w] = max(dp[w], dp[w - weights[i]] + profits[i])
            dp[w] = max(dp[w], dp[w - weights[i]] + profits[i])
    
    return dp[capacity]	
