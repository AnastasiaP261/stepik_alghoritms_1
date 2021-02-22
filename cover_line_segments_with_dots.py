def conference_room(line_segments, n):
    solution = [line_segments[0]]
    min_r = solution[0][1]

    i = 0
    while i < n:
        if min_r <= line_segments[i][0]:
            solution.append(line_segments[i])
            min_r = line_segments[i][1]
        i += 1

    return solution


def cover(line_segments, n):
    solution = []
    last_point = -1

    i = 0
    while i < n:
        if last_point < line_segments[i][0]:
            last_point = line_segments[i][1]
            solution.append(last_point)
        i += 1

    return solution


def main():
    n = int(input())
    line_segments = []
    for i in range(n):
        l, r = map(int, input().split())
        couple = (l, r)
        line_segments.append(couple)

    #print(line_segments)
    line_segments.sort(key=lambda x: x[1])
    print(line_segments)

    sol1 = conference_room(line_segments, n)
    print(str(len(sol1)) + '\n' + str(sol1))

    sol2 = cover(line_segments, n)
    print(len(sol2))
    print(str(" ".join(map(str, sol2))))


main()
