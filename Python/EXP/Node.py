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

def main():
    print(loop_size(5))

if __name__ == "__main__":
    main()


#Метод черепахи и зайца

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def loop_size(node):
    # Используем метод "черепахи и зайца" для поиска цикла
    slow = node
    fast = node

    # Поиск начала цикла
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # Если цикл не найден, возвращаем 0
    if fast is None or fast.next is None:
        return 0

    # Определение размера цикла
    count = 1
    current = slow.next
    while current != slow:
        count += 1
        current = current.next

    return count

def main():
    # Пример создания узлов и цикла
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    print(loop_size(node1))  # Должно вывести 3

if __name__ == "__main__":
    main()
