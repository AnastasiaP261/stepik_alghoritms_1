def bin_search(arr, req_num):
    a = 0
    b = len(arr) - 1
    while a <= b:
        i_mid = int((b + a) / 2)
        if arr[i_mid] == req_num:
            return i_mid + 1
        if req_num < arr[i_mid]:
            b = i_mid - 1
            continue
        else:
            a = i_mid + 1
            continue
    return -1


def main():
    arr = list(map(int, input().split()))                 # длина массива, массив чисел
    n = arr.pop(0)
    required_numbers = list(map(int, input().split()))     # кол-во искомых чисел, массив искомых чисел
    k = required_numbers.pop(0)

    results = [-1] * k
    for i in range(k):
        results[i] = bin_search(arr, required_numbers[i])
    print(" ".join(str(i) for i in results))


main()
