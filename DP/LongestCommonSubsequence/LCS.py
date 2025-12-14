
'''
Leetcode #1143. Longest Common Subsequence

1. LCS with Recursion
2. LCS with Memoization
3. LCS with Dyanmic Programming

'''

#1. LCS with Recursion

def LCS_with_Recursion(i, j, A, B):
	
	#Base case: if either string reaches its end, return 0
	if i >= len(A) or j >= len(B):
		return 0
	
	#If the characters match, add 1 and proceed with the next characters in both strings
	if A[i] == B[j]:
		return 1 + LCS_with_Recursion(i+1, j+1, A, B)
	
	#Otherwise, find the maximum by exploring both possbilities
	else:
		return max(LCS_with_Recursion(i+1, j, A, B),
			LCS_with_Recusion(i, j+1, A, B)0

#2. LCS with Memoization

def LSC_with_Memoization(i, j, A, B, memo):
	
	#Check if the result is already computed
	if (i, j) in memo:
		return memo[(i,j)]
	
	if A[i] == B[j]:
		memo[(i,j)] = 1 + LSC_with_Memoization(i+1,j+1, A, B, memo)
	else:
		memo[(i,j)] = max(LSC_with_Memoization(i+1, j, A, B, memo),
				LSC_with_Memoization(i, j+1, A, B, memo)
	
	return memo[(i,j)]

#3. LSC with Dynamic Programming

#When doing 2D DP tables, it is recommended practice for many problems to include an extra 1 to both the row and column. It prevents indexing errors and helps with generalization (this is for 2D and knapsack related problems)

def LSC_with_Dynamic_Programming(string1, string2):	
	row = len(text1)
        column = len(text2)

        dp = [[0] * (column + 1) for _ in range(row + 1)]
        
        for i in range(1, row + 1):
            for j in range(1, column + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        return dp[row][column]
