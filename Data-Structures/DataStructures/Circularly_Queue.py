from DoubleLinkedList import DoublyLinkedList 

class Circ_Queue(DoublyLinkedList):
    _first = None
    _last = None
    __DList = None

    def __init__(self):
        self.__DList = DoublyLinkedList()
        self._first = self.__DList.head
        self._last = self.__DList.tail
    
    def size(self):
        return self.__DList.Size()
    
    def is_empty(self):
        return self.size == 0
    
    def __repr__(self):
        if(self.is_empty()):
           return "Queue is empty"
        
        values = []
        current = self.__DList.head
        while(current != None):
            values.append(str(current.value))
            current = current.next

        return "<-".join(values)
    
    def inqueue(self, value):
        self.__DList.append(value)
        self._first = self.__DList.head
        self._last = self.__DList.tail

    def dequeue(self):
        if(self.is_empty()):
            return None
        
        value = self._first.value
        self.__DList.delete_first()
        self.inqueue(value)
        self._first = self.__DList.head
        return value

    def peek(self):
        return self._first



# ! testing code
cq = Circ_Queue()
cq.inqueue(10)
print(cq.peek())
cq.inqueue(20)
cq.inqueue(30)
print(cq)  # Output: 10<-20<-30
print("Dequeue:", cq.dequeue())  # Output: Dequeue: 10
print(cq)  # Output: 20<-30<-10
print("Dequeue:", cq.dequeue())  # Output: Dequeue: 20
print(cq)  # Output: 30<-10<-20
print("Peek:", cq.peek())  # Output: Peek: 30


