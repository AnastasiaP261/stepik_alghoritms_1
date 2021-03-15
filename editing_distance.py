infinity = 10 ** 2 + 1


def edit_dist(s1, s2, editd, i, j):
    global infinity
    if editd[i][j] == infinity:
        if i != 0 and j != 0:
            ins = edit_dist(s1, s2, editd, i, j - 1) + 1
            _del = edit_dist(s1, s2, editd, i - 1, j) + 1
            diff = 0 if s1[j - 1] == s2[i - 1] else 1
            sub = edit_dist(s1, s2, editd, i - 1, j - 1) + diff

            editd[i][j] = min(ins, _del, sub)
            # print('\n'.join(str(i) for i in editd) + '\n')
    return editd[i][j]


def main():
    string1 = input()
    string2 = input()
    global infinity
    editd = [[infinity for _ in range(len(string1) + 1)] for _ in range(len(string2) + 1)]

    for j in range(len(string1) + 1):
        editd[0][j] = j
    for i in range(1, len(string2) + 1):
        editd[i][0] = i

    # print('\n'.join(str(i) for i in editd) + '\n')
    print(edit_dist(string1, string2, editd, len(string2), len(string1)))


if __name__ == "__main__":
    main()

"""
editing
distance

"""






