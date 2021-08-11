class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def serialize(node: Node, s=""):
# 	if not isinstance(node, Node):
# 		return "# "
# 	s += (str(node.val) + " ")
# 	s += serialize(node.left)
# 	s += serialize(node.right)
# 	return s

# def deserialize(node_str: str, result=None):
# 	if node_str.split()[0] == "#":
# 		return None
# 	result = Node(node_str.split()[0])
# 	result.left = deserialize(node_str.partition(" ")[2], result)
# 	result.right = deserialize(node_str.partition(" ")[2].partition(" ")[2], result)
# 	return result


def serialize(node: Node):
    if not isinstance(node, Node):
        return "#"
    return f"{node.val} {serialize(node.left)} {serialize(node.right)}"


# def deserialize(node_str):
# 	vals = iter(node_str.split())
# 	def build_node():
# 		val = next(vals)
# 		if val == "#":
# 			return None
# 		node = Node(val)
# 		node.left = build_node()
# 		node.right = build_node()
# 		return node
# 	return build_node()


def deserialize(node_str):
    vals = iter(node_str.split())

    def build_node():
        val = next(vals)
        if val == "#":
            return None
        return Node(val, build_node(), build_node())

    return build_node()


if __name__ == "__main__":
    node = Node("root", Node("left", Node("left.left")), Node("right"))
    assert deserialize(serialize(node)).left.left.val == "left.left"
