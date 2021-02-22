from heapq import heappush as insert, heappop as extract_min
from collections import deque


class Tree:
    def __init__(self, val, freq, left=None, right=None):
        self.left = left
        self.right = right
        self.freq = freq    # частота
        self.val = val      # символ


def creating_code(_dict, root):
    visited = set()
    stack = deque([root])
    string = ''

    while stack:
        vertex = stack[-1]
        if type(vertex.val) is not str:
            if vertex.right in visited:
                visited.add(vertex)
                stack.pop()
                string = string[:-1]
            elif vertex.left in visited:
                stack.append(vertex.right)
                string += '1'
            else:
                stack.append(vertex.left)
                string += '0'
        else:
            _dict[vertex.val] = string
            visited.add(vertex)
            stack.pop()
            string = string[:-1]


def main():
    string = input()
    dictionary = {}

    # считываем символы и их частоты
    for ch in string:
        if ch in dictionary.keys():
            dictionary[ch] += 1
        else:
            dictionary[ch] = 1

    # добавляем символы в очередь, используя частоту в качестве приоритета
    pq = []
    ident = 0
    for ch in dictionary:
        priority = dictionary.get(ch)
        insert(pq, (priority, ident, ch))
        ident += 1
        dictionary[ch] = ''

    if len(pq) == 1:
        dictionary[pq[0][2]] = '0'
    else:
        # создаем узлы дерева
        while len(pq) > 1:
            min1 = extract_min(pq)
            min2 = extract_min(pq)

            if type(min1[2]) is str:
                leaf1 = Tree(min1[2], min1[0])
            else:
                leaf1 = min1[2]
            if type(min2[2]) is str:
                leaf2 = Tree(min2[2], min2[0])
            else:
                leaf2 = min2[2]

            F = Tree(None, leaf1.freq + leaf2.freq, right=leaf2, left=leaf1)
            insert(pq, (F.freq, ident, F))

            ident += 1

        F.freq = None
        creating_code(dictionary, F)

    encoded_string = ''
    for ch in string:
        encoded_string += dictionary[ch]

    print(f'{len(dictionary)} {len(encoded_string)}')
    for i in dictionary:
        print(f'{i}: {dictionary[i]}')
    print(encoded_string)


main()