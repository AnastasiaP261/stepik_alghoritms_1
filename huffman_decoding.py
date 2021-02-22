from heapq import heappush as insert, heappop as extract_min


class Tree:
    def __init__(self, val=None, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val      # символ


def decoding(encoded_str, root):
    vertex = root
    string = ''

    for ch in encoded_str:
        if ch == '0':
            vertex = vertex.left
        else:
            vertex = vertex.right

        if vertex.val is not None:
            string += vertex.val
            vertex = root
    return string


def create_decode_tree(pq):
    root = Tree()

    while pq:
        line = extract_min(pq)
        char = line[1]
        line = line[0]
        vertex = root
        for binary in line:
            if binary == '0':
                if vertex.left is None:
                    vertex.left = Tree()
                vertex = vertex.left
            else:
                if vertex.right is None:
                    vertex.right = Tree()
                vertex = vertex.right
        vertex.val = char

    return root


def main():
    k, l = map(int, input().split())    # количество различных букв в строке, размер получившейся закодированной строки
    _dict = {}
    for i in range(k):
        _str = input()
        _dict[_str[3:]] = _str[0]
    encoded_string = input()

    pq = []
    for ch in _dict:
        code = [i for i in ch]
        insert(pq, (code, _dict[ch]))

    root = create_decode_tree(pq)
    print(decoding(encoded_string, root))


main()