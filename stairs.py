def calc_of_amount(stairs):
    if len(stairs) == 1:
        return stairs[0]

    prev1 = 0
    prev2 = stairs[0]
    cur = stairs[1]

    for i in range(1, len(stairs)):
        cur = stairs[i]
        cur += max(prev1, prev2)
        prev1 = prev2
        prev2 = cur

    return cur


def main():
    n = int(input())
    stairs = list(map(int, input().split()))

    print(calc_of_amount(stairs))


def test():
    assert -63 == calc_of_amount([-2, -16, -13, -9, -48]), 'test 1'
    assert 2 == calc_of_amount([1, 1, -2, -4, -6, 2, 2]), 'test 2'
    assert -73 == calc_of_amount([-64, -16, -13, -9, -48]), 'test 3'
    assert 5 == calc_of_amount([0, 0, 0, 4, 6, -5]), 'test 4'
    assert -9 == calc_of_amount([-6, 4, -16, -13, -9, 0]), 'test 5'
    assert -18 == calc_of_amount([-6, 4, -16, -13, -9]), 'test 6'
    assert 21 == calc_of_amount([3, 4, 10, 10, 0, -6, -10, 0]), 'test 7'
    assert 3 == calc_of_amount([1, 2]), 'test 8'
    assert 1 == calc_of_amount([2, -1]), 'test 9'
    assert 3 == calc_of_amount([-1, 2, 1]), 'test 10'
    assert 2 == calc_of_amount([2]), 'test 11'
    assert -2 == calc_of_amount([-2]), 'test 12'
    assert 1 == calc_of_amount([2, -1, -1]), 'test 13'
    assert -2 == calc_of_amount([-1, -1, -1]), 'test 14'
    assert -1000 == calc_of_amount([-100, -1000]), 'test 15'
    assert 65 == calc_of_amount([1, 2, 8, -6, 4, -1, 2, 3, 6, 7, -5, 4, 3, 3, 4, -1, 8, 9, -1, 1]), 'test 16'
    assert 2 == calc_of_amount([1, 1, -2, -4, -6, 2, 2]), 'test 17'
    assert -12 == calc_of_amount([-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]), 'test 18'
    assert -205 == calc_of_amount([-5, -10, -100, -100, -100]), 'test 19'
    assert 15 == calc_of_amount([1, 2, 3, 4, 5]), 'test 20'
    assert 0 == calc_of_amount([1, 2, 3, 4, 5, -15]), 'test 21'


if __name__ == "__main__":
    main()

'''
3
2 -1 -1

3
-1 -1 -1

8
3 4 10 10 0 -6 -10 0

20
1 2 8 -6 4 -1 2 3 6 7 -5 4 3 3 4 -1 8 9 -1 1

5
-2 -16 -13 -9 -48

7
1 1 -2 -4 -6 2 2

5
-64 -16 -13 -9 -48

'''