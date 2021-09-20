class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, collection=None):
        self.head = None

        if collection:
            for item in reversed(collection): 
                self.insert(item)

    def __iter__(self):

        def generator_vlues():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return generator_vlues()


    def insert(self, value):
            self.head = Node(value, self.head)

    def __len__(self):
        return len(list(iter(self)))

    def __eq__(self, item):
        return list(self) == list(item)

    # def __getitem__(self, index):
    #     return list(self)[index]

    #     for i, item in enumerate(self):
    #         if i == index:
    #             return item
    #     raise IndexError


    # def append(self, value):
    #     node = Node(value)

    #     if self.head == None:
    #         self.head = node
    #         return
    #     current = self.head

    #     while current.next != None :
    #         current = current.next
    #     current.next = node

    # def __str__(self):
    #     out = ''
    #     for value in self:
    #         out += f'[ {value} ] -> '
    #     out += 'None'
    #     return out

