import ctypes


class Node:
    def __init__(self, val, both=0):
        self.val = val
        self.both = both


class XorLinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add(self, node: Node):
        if self.head is None:
            self.head = self.tail = None
        else:
            self.tail.both = id(node) ^ self.tail.both
            node.both = id(self.tail)
            self.tail = node

    def get(self, index):
        prev_id = 0
        node = self.head
        for i in range(index):
            next_id = prev_id ^ node.both
            if next_id:
                prev_id = id(node)
                node = _get_obj(next_id)
            else:
                print("error")
        return node


def _get_obj(id):
    return ctypes.cast(id, ctypes.py_object).value
