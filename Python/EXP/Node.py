class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"[{self.data}] -> {self.next}"
    
def loop_size(node):

    nodes = []

    for i in range(node):
        nodes.append(Node(i))
        if i > 0:
            nodes[i-1].next = nodes[i]

    nodes[-1].next = nodes[0]

    return len(nodes)