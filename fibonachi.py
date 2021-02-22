def fib(n):
    fib_list = []
    fib_list.append(0)
    fib_list.append(1)
    if n > 1:
        i = 2
        while i <= n:
            fib_list.append(fib_list[i-1] + fib_list[i-2])
            i += 1
    return fib_list[n]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
