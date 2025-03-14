"""Вам дан узел, который является началом связанного списка. Этот список содержит висячий элемент и цикл. 
Ваша задача — определить длину цикла.
Например, на следующем рисунке размер свисающего элемента равен 3, а размер петли — 12:
# Use the `next' attribute to get the following node
node.next"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"[{self.data}] -> {self.next}"

def main():
    loop_size(5)

def loop_size(node):

    nodes = []

    for i in range(node):
        nodes.append(Node(i))
        if i > 0:
            nodes[i-1].next = nodes[i]

if __name__ == "__main__":
    main()