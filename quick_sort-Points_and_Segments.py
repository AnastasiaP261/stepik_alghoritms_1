"""
Failed test #6 of 25. Wrong answer
Все тесты, приведенные после программы ешаются верно
"""
import random


def partition(arr, l, r):
    rand_i = random.randint(l, r - 2)
    arr[l], arr[rand_i] = arr[rand_i], arr[l]
    pivot = arr[l]
    #print(f'выбран элемент {pivot} под номером {rand_i}')
    equal_right, less_right = l, l

    for i in range(l + 1, r):
        if arr[i] < pivot:
            less_right += 1
            arr[less_right], arr[i] = arr[i], arr[less_right]
        elif arr[i] == pivot:
            equal_right += 1
            less_right += 1
            arr[equal_right], arr[less_right] = arr[less_right], arr[equal_right]
            if less_right != i:
                arr[equal_right], arr[i] = arr[i], arr[equal_right]

    if less_right != equal_right:
        new_equal_right = less_right
        for i in range(equal_right, l - 1, -1):
            arr[i], arr[less_right] = arr[less_right], arr[i]
            less_right -= 1
        return less_right + 1, new_equal_right + 1
    else:
        return l, equal_right + 1


def quick_sort(arr, l, r):
    #print(f'QS от {l} до {r}')
    if l >= r or r - l == 1:
        return
    #print(f'сортируем {arr[l:r]}')
    lm, rm = partition(arr, l, r)
    #print(f'получили массив {arr[l:r]}\nграницы {lm} и {rm}')
    quick_sort(arr, l, lm)
    quick_sort(arr, rm, r)


def points_processing(point, segments, compare):
    if compare == 'for_starts':
        if point < segments[0]:
            #print(f'для точки {point} найдено 0')
            return 0
        elif point >= segments[-1]:
            #print(f'для точки {point} найдено {len(segments)}')
            return len(segments)
    else:
        if point <= segments[0]:
            #print(f'для точки {point} найдено 0')
            return 0
        elif point > segments[-1]:
            #print(f'для точки {point} найдено {len(segments)}')
            return len(segments)

    if compare == 'for_starts':
        code, i = bin_search(point + 1, segments)
        if segments[i] == point:
            i += 1
        #print(f'для точки {point} с кодом {code} найдено {i}')

        while i > 0 and segments[i - 1] == point + 1:
            i -= 1
        #print(f'преобразовали к {i}')
    else:
        code, i = bin_search(point - 1, segments)
        #print(f'для точки {point} с кодом {code} найдено {i}')

        while i < len(segments) and segments[i] < point:
            i += 1
        #print(f'преобразовали к {i}')

    return i


def bin_search(point, segments):
    a = 0
    b = len(segments) - 1

    i_mid = -1
    while a <= b:
        i_mid = int((b + a) / 2)
        if segments[i_mid] == point:
            return 0, i_mid
        if point < segments[i_mid]:
            b = i_mid - 1
            continue
        else:
            a = i_mid + 1
            continue

    return -3, i_mid


def main():
    random.seed()
    n, m = map(int, input().split())        # количество отрезков и точек на прямой

    segments_starts = [-1] * n
    segments_ends = [-1] * n
    for i in range(n):
        start, end = map(int, input().split())
        segments_starts[i] = start
        segments_ends[i] = end

    quick_sort(segments_starts, 0, n)
    quick_sort(segments_ends, 0, n)
    print(segments_starts)
    print(segments_ends)

    str1 = ''
    str2 = ''
    str3 = ''
    for i in input().split():
        point = int(i)
        n1 = points_processing(point, segments_starts, compare='for_starts')
        n2 = points_processing(point, segments_ends, compare='for_ends')
        str1 += str(n1) + ' '
        str2 += str(n2) + ' '
        str3 += str(n1 - n2) + ' '
        """print(points_processing(point, segments_starts, compare='for_starts') -
              points_processing(point, segments_ends, compare='for_ends'), end=' ')"""
    print(str1)
    print(str2)
    print(str3)


main()

'''
20 3
1 2
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
1 1
0 0
0 1 2
правильный: 1 19 1

6 9
0 0
-1 1
-2 2
-3 3
-4 4
-5 5
-5 -4 -3 -1 0 1 3 4 5 
правильный: 1 2 3 5 6 5 3 2 1 

1 1
1 1
2
правильный: 0

19 21
1 5
2 6
2 2
3 6
6 9
13 16
13 13
13 13
13 18
16 19
2 9
1 2
2 2
2 4
4 7
6 8
8 9
14 18
16 16
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
правильный: 0 2 7 5 6 5 6 4 4 3 0 0 0 4 3 3 5 3 3 1 0

8 6
-2 3
0 3
-1 3
-1 3
3 3
0 0
0 0
-2 -2
-3 -1 0 2 3 4
правильный: 0 3 6 4 5 0 

6 7
2 3
2 5
3 5
2 7
5 7
3 7
1 2 3 4 5 6 7
правильный: 0 3 5 4 5 3 3 

6 8
0 3
1 3
2 3
3 4
3 5
3 6
0 1 2 3 4 5 6 7
правильный: 1 2 3 6 3 2 1 0

1 5
1 5
0 1 3 5 6
правильный: 0 1 1 1 0

12 11
5 8
6 7
2 9
4 5
3 4
7 9
2 10
9 10
2 5
7 8
4 6
3 8
1 2 3 4 5 6 7 8 9 10 11
правильный: 0 3 5 7 7 6 7 6 4 2 0

4 4
6 9
6 9
7 10
7 10
8 9 10 11
правильный: 4 4 2 0 

2 3
0 5
7 10
1 6 11
правильный: 1 0 0
'''