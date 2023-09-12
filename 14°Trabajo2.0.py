class node:
    def __init__(self, data = None, next = None, valor = None):
        self.data = data
        self.next = next
        self.valor = valor
class linked_list:
    def __init__(self):
        self.head = None
    def add_at_front(self,data,valor):
        self.head = node(data=data, next=self.head)
        self.head = node(valor=valor, next= self.head)
    def add_at_end(self, data):
        if not self.head:
            self.head = node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)
    def deleate_node(self,key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None
    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = self.head
        return temp.data
    def print_list(self):
        node = self.head
        while node != None:
            print(node.data, end =" => " )
            node = node.next

s = linked_list()
s.add_at_front(5,6)
s.add_at_end(8)
s.add_at_front(9,9)
s.add_at_front("hola",5)
s.print_list()

