def search_ls(arr):
    ls = [0] * len(arr)

    for i in range(len(arr)):
        ls[i] = 1
        for j in range(i):
            if arr[i] % arr[j] == 0 and ls[j] + 1 > ls[i]:
                ls[i] = ls[j] + 1
    return max(ls)


def main():
    n = int(input())
    consist = [int(i) for i in input().split()]

    print(search_ls(consist))


if __name__ == "__main__":
    main()

'''
16
3 6 9 8 7 10 6 2 3 12 10 18 17 48 25 240

'''