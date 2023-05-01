class LinkedList:
    head = None

    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node=None):
            self.element = element
            self.next_node = next_node

    def append(self, element):
        if not self.head:
            self.head = self.Node(element)
            return element

        node = self.head

        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)
        return element

    def insert(self, element, index):
        i = 0
        node = self.head
        prev_node = self.head

        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        prev_node.next_node = self.Node(element, next_node=node)
        return element

    def get(self, index):
        i = 0
        node = self.head
        prev_node = self.head

        while i < index:
            prev_node = node
            node = node.next_node
            i += 1
        return node.element

    def get_length(self):
        if not self.head:
            return 0
        i=1
        node = self.head

        while node.next_node:
            i+=1
            node = node.next_node
        return i

    def out(self):
        node = self.head
        while node.next_node:
            print(node.element)
            node = node.next_node
        print(node.element)

    def delete(self, index):
        if index == 0:
            self.head = self.head.next_node

        node = self.head
        i = 0
        prev_node = node

        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        prev_node.next_node = node.next_node
        element = node.element
        del node

        return element

    def revers(self):
        length = linked_list.get_length()
        node = self.head
        prev_node = node








linked_list = LinkedList()
linked_list.append(30)
linked_list.append(2)
linked_list.append(52)
# linked_list.append(4)

linked_list.out()
linked_list.reverse()

# linked_list.insert(10, 1)
# linked_list.insert(78, 3)
# print(linked_list.get(1))
# print(linked_list.length)
