def knapsack_01_bottomup(weights, profits, capacity):
    """
    0/1 Knapsack: Each item can be used at most once
    """
    n = len(weights)
    
    # dp[i][w] = max profit using items 0..i-1 with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Option 1: Skip item i-1
            dp[i][w] = dp[i-1][w]
            
            # Option 2: Take item i-1 (if it fits)
            if weights[i-1] <= w:
                # Recurrence: dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + profits[i-1])
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + profits[i-1])
    
    return dp[n][capacity]


# Space-optimized O(capacity) version:
def knapsack_01_optimized(weights, profits, capacity):
    dp = [0] * (capacity + 1)
    
    for i in range(len(weights)):
        # Iterate BACKWARDS to avoid using same item twice
        for w in range(capacity, weights[i] - 1, -1):
            # Recurrence: dp[w] = max(dp[w], dp[w - weights[i]] + profits[i])
            dp[w] = max(dp[w], dp[w - weights[i]] + profits[i])
    
    return dp[capacity]
