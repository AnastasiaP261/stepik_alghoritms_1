''' Дано число 1 <= n <= n**7, необходимо найти последнюю цифру nn-го числа Фибоначчи. '''

def fib_digit(n):
    list = []
    list.append(0)
    list.append(1)
    if n > 1:
        i = 2
        while i <= n:
            num = str(list[i - 1] + list[i - 2])
            list.append(int(num[-1]))
            i += 1
    return list[n]


''' Даны целые числа 1 <= n <= 10**18 и 2 <= m <= 10**5,
необходимо найти остаток от деления nn-го числа Фибоначчи на mm. '''

def fib_mod(n, m):
    period = []
    period.append(0)
    period.append(1)

    i = 2
    while i <= n:
        num = period[i - 1] + period[i - 2]
        period.append(num % m)
        if period[i] == period[1] and period[i-1] == period[0]:
            num_period = len(period) - 2
            return period[n % num_period]
        i += 1
    return period[n]


def main():
    n, m = map(int, input().split())

    print(fib_digit(n))
    print(fib_mod(n, m))

    return 0


if __name__ == "__main__":
    main()