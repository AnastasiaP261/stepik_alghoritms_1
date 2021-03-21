def rest_of_resp(operations):
    answer = [0 for _ in range(operations[-1][0] + 1)]

    j = len(operations) - 1
    for i in range(len(answer) - 1, -1, -1):
        answer[i] = j + 1
        j = operations[j][1]

    return answer


def calc(n):
    operations = [[0, 0] for _ in range(n)]

    for cur in range(1, n):
        add1 = cur + 1
        mult2 = cur * 2
        mult3 = cur * 3
        
        if operations[add1 - 1] == [0, 0] or operations[add1 - 1][0] > operations[cur - 1][0] + 1:
            operations[add1 - 1][0] = operations[cur - 1][0] + 1
            operations[add1 - 1][1] = cur - 1
        
        if mult2 <= n and \
                (operations[mult2 - 1][0] > operations[cur - 1][0] + 1 or operations[mult2 - 1] == [0, 0]):
            operations[mult2 - 1][0] = operations[cur - 1][0] + 1
            operations[mult2 - 1][1] = cur - 1
        
        if mult3 <= n and \
                (operations[mult3 - 1][0] > operations[cur - 1][0] + 1 or operations[mult3 - 1] == [0, 0]):
            operations[mult3 - 1][0] = operations[cur - 1][0] + 1
            operations[mult3 - 1][1] = cur - 1

    answer = rest_of_resp(operations)
    return operations[-1][0], answer


def main():
    number = int(input())

    num_of_operat, chain = calc(number)
    print(num_of_operat)
    print(' '.join(map(str, chain)))


def test():
    assert 3 == calc(12), 'test 1'
    assert 14 == calc(96234), 'test 2'
    assert 3 == calc(5), 'test 3'
    assert 0 == calc(1), 'test 4'
    assert 9 == calc(71), 'test 5'
    assert 14 == calc(863), 'test 6'
    assert 19 == calc(8639), 'test 7'
    assert 24 == calc(77759), 'test 8'
    assert 3 == calc(10), 'test 9'
    assert 17 == calc(32718), 'test 10'
    assert 18 == calc(98734), 'test 11'
    assert 14 == calc(96234), 'test 12'
    assert 1 == calc(2), 'test 13'
    assert 1 == calc(3), 'test 14'
    assert 2 == calc(4), 'test 15'


if __name__ == "__main__":
    main()