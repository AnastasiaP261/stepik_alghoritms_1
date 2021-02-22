from math import floor
from sys import stdin, stdout


class Heap:
    def __init__(self):
        self.heap = []

    def extract_max(self):
        _max = self.heap[0]
        try:
            self.heap[0] = self.heap.pop()
        except IndexError:
            return _max

        code, child = self.checking_conditions(0)
        if code == -2:
            self.sift_down(0, child)

        return _max

    def insert(self, val):
        self.heap.append(val)
        code, parent = self.checking_conditions(len(self.heap) - 1)

        if code == -1:
            self.sift_up(len(self.heap) - 1, parent)

    def sift_up(self, child, parent):
        code = -1
        while code == -1:
            self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
            child = int(floor((child - 1) / 2))
            code, parent = self.checking_conditions(child)

    def sift_down(self, parent, child):
        code = -2
        while code == -2:
            self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
            parent = child
            code, child = self.checking_conditions(parent)

    def checking_conditions(self, i):
        child = {}
        if i != 0 and self.heap[i] > self.heap[int(floor((i - 1) / 2))]:
            return -1, int(floor((i - 1) / 2))
        if i != 0:
            if (i * 2 + 1) < len(self.heap) and self.heap[i] < self.heap[i * 2 + 1]:
                child[self.heap[i * 2 + 1]] = i * 2 + 1
            if (i * 2 + 2) < len(self.heap) and self.heap[i] < self.heap[i * 2 + 2]:
                child[self.heap[i * 2 + 2]] = i * 2 + 2
        else:
            if 1 < len(self.heap) and self.heap[i] < self.heap[1]:
                child[self.heap[1]] = 1
            if 2 < len(self.heap) and self.heap[i] < self.heap[2]:
                child[self.heap[2]] = 2
        if len(child) > 0:
            return -2, child[max(child)]
        return 0, -1


def main():
    n = int(stdin.readline())
    heap = Heap()

    for i in range(n):
        line = stdin.readline()
        if 'Insert' in line:
            line = line.split()
            num = int(line[1])

            heap.insert(num)
        else:
            if len(heap.heap) > 0:
                stdout.write(str(heap.extract_max()) + '\n')
        # stdout.write(' '.join(str(i) for i in heap.heap[:]) + '\n')


main()

'''
11
Insert 8
Insert 9
Insert 5
Insert 4
Insert 10
Insert 7
Insert 7
ExtractMax
ExtractMax
ExtractMax
ExtractMax

6
Insert 6
Insert 10
Insert 9
Insert 25
Insert 6
Insert 4

6
Insert 200
Insert 10
ExtractMax
Insert 5
Insert 500
ExtractMax

8
Insert 200
Insert 10
Insert 5
Insert 500
ExtractMax
ExtractMax
ExtractMax
ExtractMax

12
Insert 2
Insert 3
Insert 18
Insert 15
Insert 18
Insert 12
Insert 12
Insert 2
ExtractMax
ExtractMax
ExtractMax
Insert 7

8
Insert 18
Insert 15
Insert 18
Insert 12
Insert 12
ExtractMax
ExtractMax
ExtractMax

'''