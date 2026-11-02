def knapsack(n, weights, profits, capacity):

    # Create DP table
    dp = [[0 for j in range(capacity + 1)]
          for i in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):

            if weights[i - 1] <= j:
                dp[i][j] = max(
                    profits[i - 1] + dp[i - 1][j - weights[i - 1]],
                    dp[i - 1][j]
                )
            else:
                dp[i][j] = dp[i - 1][j]

    # Display maximum profit
    print("Maximum Profit:", dp[n][capacity])

    # Find selected items
    j = capacity
    print("Selected Items:")

    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            print("Item", i)
            j = j - weights[i - 1]


# Main function
def main():

    n = int(input("Enter number of items: "))

    weights = []
    profits = []

    for i in range(n):
        w = int(input("Enter weight of item: "))
        p = int(input("Enter profit of item: "))

        weights.append(w)
        profits.append(p)

    capacity = int(input("Enter knapsack capacity: "))

    knapsack(n, weights, profits, capacity)


# Function call
main()