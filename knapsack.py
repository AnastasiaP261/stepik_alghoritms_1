def main():
    max_w, items_num = map(int, input().split())
    weights = list(map(int, input().split()))

    knapsack = [[0 for _ in range(max_w + 1)] for _ in range(items_num + 1)]

    for i in range(1, items_num + 1):
        for j in range(1, max_w + 1):
            knapsack[i][j] = knapsack[i - 1][j]
            if weights[i - 1] <= j:
                knapsack[i][j] = max(knapsack[i][j], knapsack[i - 1][j - weights[i - 1]] + weights[i - 1])

    print(knapsack[-1][-1])


if __name__ == '__main__':
    main()

'''
10 4
6 3 4 2

'''