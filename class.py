from __future__ import print_function
class Node(object):
    def __init__(self, element, next=None):
        self.element = element   
        self.next=next

class LinkedList(object):
    def __init__(self):
        self.font=None
        self.back=None
        self.size=0
    def isEmpty(self):
        if self.isEmpty():
            self.front=Node(element)
            self.back=self.front
        else:
            temp=self.front
            self.front=Node(element, tempt)
        self.size +=1
    def addLast(self, element):
        if self.isEmpty():
            self.front=Node(element)
            self.back=self.front
        else:
            self.back.next=node(element)
            self.back=self.back.next
        self.size +=1
    def printList(self):
        print("Isi Linked List:")
        current=self.front
        while current !=None:
            print(current.element)
            current=current.next
def main():
    li=LinkedList()
   # li.addFirst(10)
    li.addLast(20)
    li.addLast(30)
   # li.addFirst(90)
    li.printList()
if __name__=="__main__":
    main()
