from sys import stdout, stdin


def main():
    n = int(stdin.readline())
    nums = [int(i) for i in stdin.readline().split()]
    counting_val = [0] * 10

    for i in range(n):
        counting_val[nums[i] - 1] += 1

    for i in range(1, 10):
        counting_val[i] += counting_val[i - 1]

    sorted_values = [0] * n
    for i in range(n - 1, -1, -1):
        sorted_values[counting_val[nums[i] - 1] - 1] = nums[i]
        counting_val[nums[i] - 1] -= 1

    stdout.write(' '.join([str(i) for i in sorted_values]))


main()


'''
5
2 3 9 2 9

'''