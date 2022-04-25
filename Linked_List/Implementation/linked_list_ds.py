class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleList:
    def __init__(self):
        self.head = None
        self.curr = None

    def __str__(self):
        if self.head is None:
            return None
        else:
            return self.display()


    def addNodeEnd(self, data):
        node = Node(data)
        if self.head is None:
            self.head= node
            self.curr = self.head
        else:
            self.curr.next = node
            self.curr = self.curr.next
    
    def addNodeStart(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.curr = self.head
        else:
            node.next = self.head
            self.head = node

    def addNodePosition(self, data, pos):
        #ll = a->b->c
        #pos=1, data=w ===> a->w->b->c
        #pos=0, data=w ===>w->a->b->c
        #pos=4, data=w ===> 'not possible' 
        if pos > self.calLength():
            raise Exception('specified pos is exceeding the length of ll')
        else:
            node = Node(data)
            if self.head is None:
                self.head = node
                self.curr = self.head
            else:
                temp = self.head
                while pos > 1:
                    pos -= 1
                    temp = temp.next
                if temp.next is None:
                    temp.next = node
                    self.curr = node
                else:  
                    node.next = temp.next
                    temp.next = node

    def calLength(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def display(self):
        temp = self.head
        res = []
        while temp is not None:
            res.append(temp.data)
            temp = temp.next
        return res

