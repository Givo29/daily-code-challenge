class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialise(root):
    values = []

    def encode(node):
        if node:
            values.append(str(node.val))
            encode(node.left)
            encode(node.right)
        else:
            values.append('null')
    encode(root)
    return values


def deserialise(s):

    def decode(values):
        value = next(values)
        if value == "null":
            return None
        node = Node(value)
        node.left = decode(values)
        node.right = decode(values)
        return node

    values = iter(s)
    return decode(values)


def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialise(serialise(node)).left.left.val == 'left.left'


if __name__ == '__main__':
    main()
