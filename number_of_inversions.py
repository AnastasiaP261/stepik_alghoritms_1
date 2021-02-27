counter = 0


def merge(part1, part2):
    global counter
    joint_arr = []

    i = 0
    j = 0
    while True:
        if part1[i] > part2[j]:
            counter += len(part1) - i
            joint_arr.append(part2[j])
            j += 1
        else:
            joint_arr.append(part1[i])
            i += 1

        if i == len(part1):
            joint_arr += part2[j:]
            break
        if j == len(part2):
            joint_arr += part1[i:]
            break

    return joint_arr


def merge_sort(arr, left, right):
    if left < right and len(arr) > 1:
        m = int((left + right) / 2)
        arr1 = merge_sort(arr[left:m], 0, len(arr[left:m]))
        arr2 = merge_sort(arr[m:right], 0, len(arr[m:right]))
        arr = merge(arr1, arr2)
    return arr


def main():
    global counter
    n = int(input())
    arr = [int(i) for i in input().split()]

    sorted_arr = merge_sort(arr, 0, n)
    print(counter)


main()