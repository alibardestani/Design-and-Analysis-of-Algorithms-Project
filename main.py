import time


def DP(wt, val, W, n):
    dp_table = [[0] * (W + 1) for _ in range(2)]

    for i in range(1, n + 1):
        current_row = i % 2
        previous_row = 1 - current_row

        for w in range(W + 1):
            if wt[i - 1] <= w:
                dp_table[current_row][w] = max(
                    val[i - 1] + dp_table[previous_row][w - wt[i - 1]],
                    dp_table[previous_row][w]
                )
            else:
                dp_table[current_row][w] = dp_table[previous_row][w]

    max_value = dp_table[n % 2][W]
    return max_value


def knapsack_memoization(wt, val, W, n):
    memo = [[-1] * (W + 1) for _ in range(n + 1)]

    def knapsack_recursive(W, n):
        if n == 0 or W == 0:
            return 0, []

        if memo[n][W] != -1:
            return memo[n][W]

        if wt[n - 1] <= W:
            include_item_value, include_items = knapsack_recursive(W - wt[n - 1], n - 1)
            include_item_value += val[n - 1]
            include_items = include_items + [n] if include_items else [n]

            exclude_item_value, exclude_items = knapsack_recursive(W, n - 1)

            if include_item_value > exclude_item_value:
                memo[n][W] = include_item_value, include_items
            else:
                memo[n][W] = exclude_item_value, exclude_items

            return memo[n][W]
        else:
            memo[n][W] = knapsack_recursive(W, n - 1)
            return memo[n][W]

    max_value, selected_items = knapsack_recursive(W, n)
    selected_items_str = " - ".join(map(str, selected_items))
    return max_value, selected_items_str


def knapsack_greedy_by_ratio(wt, val, W, n):
    ratios = [(val[i] / wt[i], i + 1) for i in range(n)]
    ratios.sort(reverse=True)

    max_value = 0
    selected_items = []

    for ratio, item_id in ratios:
        if wt[item_id - 1] <= W:
            selected_items.append(item_id)
            max_value += val[item_id - 1]
            W -= wt[item_id - 1]
    return max_value, selected_items


def knapsack_greedy_by_difference(wt, val, W, n):
    differences = [(val[i] - wt[i], i + 1) for i in range(n)]
    differences.sort(reverse=True)

    max_value = 0
    selected_items = []

    for diff, item_id in differences:
        if wt[item_id - 1] <= W:
            selected_items.append(item_id)
            max_value += val[item_id - 1]
            W -= wt[item_id - 1]
    return max_value, selected_items


def knapsack_greedy_by_weight(wt, val, W, n):
    weights = [(wt[i], i + 1) for i in range(n)]
    weights.sort()

    max_value = 0
    selected_items = []

    for weight, item_id in weights:
        if weight <= W:
            selected_items.append(item_id)
            max_value += val[item_id - 1]
            W -= weight
    return max_value, selected_items


def knapsack_greedy_by_value(wt, val, W, n):
    values = [(val[i], i + 1) for i in range(n)]
    values.sort(reverse=True)

    max_value = 0
    selected_items = []

    for value, item_id in values:
        if wt[item_id - 1] <= W:
            selected_items.append(item_id)
            max_value += val[item_id - 1]
            W -= wt[item_id - 1]
    return max_value, selected_items


def PrintFunc(resultV, resultI):
    resultI_str = " - ".join(map(str, resultI))

    print(f"The maximum value that can be obtained is: {resultV}")
    print(resultI_str)


def GetInput():
    n = int(input())

    wt = []
    val = []
    for i in range(n):
        data = list(map(int, input().split()))
        wt.append(data[1])
        val.append(data[2])

    W = int(input())
    return wt, val, W, n


wt, val, W, n = GetInput()

print("Knapsack Greedy by Ratio")
start_time = time.time()
resultV, resultI = knapsack_greedy_by_ratio(wt, val, W, n)
end_time = time.time()
PrintFunc(resultV, resultI)
print(f"Elapsed time: {end_time - start_time} seconds\n\n")

print("Knapsack Greedy by Difference")
start_time = time.time()
resultV, resultI = knapsack_greedy_by_difference(wt, val, W, n)
end_time = time.time()
PrintFunc(resultV, resultI)
print(f"Elapsed time: {end_time - start_time} seconds\n\n")

print("Knapsack Greedy by Weight")
start_time = time.time()
resultV, resultI = knapsack_greedy_by_weight(wt, val, W, n)
end_time = time.time()
PrintFunc(resultV, resultI)
print(f"Elapsed time: {end_time - start_time} seconds\n\n")

print("Knapsack Greedy by Value")
start_time = time.time()
resultV, resultI = knapsack_greedy_by_value(wt, val, W, n)
end_time = time.time()
PrintFunc(resultV, resultI)
print(f"Elapsed time: {end_time - start_time} seconds\n\n")

print("Knapsack Memoization")
start_time = time.time()
resultV, resultI = knapsack_memoization(wt, val, W, n)
end_time = time.time()
PrintFunc(resultV, resultI)
print(f"Elapsed time: {end_time - start_time} seconds\n\n")

print("DP")
start_time = time.time()
resultV, resultI = DP(wt, val, W, n)
end_time = time.time()
elapsed_time = end_time - start_time
PrintFunc(resultV, resultI)
print(f"Elapsed time: {elapsed_time} seconds\n\n")

