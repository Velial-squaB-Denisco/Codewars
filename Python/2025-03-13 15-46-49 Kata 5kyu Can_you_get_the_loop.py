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

def loop_size(node):
    for i in range(node):
        node[i] = Node(i)