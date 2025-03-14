"""Вам дан узел, который является началом связанного списка. Этот список содержит висячий элемент и цикл. 
Ваша задача — определить длину цикла.
Например, на следующем рисунке размер свисающего элемента равен 3, а размер петли — 12:
# Use the `next' attribute to get the following node
node.next"""

def loop_size(node):
    pass

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"[{self.data}] -> {self.next}"



node1 = Node(1)
node2 = Node(2)

node1.next = node2

node1.next
print(node1)