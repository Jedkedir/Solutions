class Node:
    def __init__(self, value):
                 self.value = value
                 self.next = None
    def res(head:Node) -> list:
            curr = head
            res = []
            while curr:
                print(curr.value)
                res.append(curr.value)
                curr = curr.next
            return res
a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
print(Node.res(a))