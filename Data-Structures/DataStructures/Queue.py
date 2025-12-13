from LinkedList import LinkedList 
from LinkedList import Node

class Queue(LinkedList):
    __LinkedList = None
    _first = None
    _last = None

    def __init__(self):
        self.__LinkedList = LinkedList()
        self._last = self.__LinkedList.tail
        self._first = self.__LinkedList.head

    def size(self):
        return self.__LinkedList.Size()

    def is_empty(self):
        return self.size() == 0
    
    def __repr__(self):
        if(self.is_empty()) :
            return "Queue is empty"
        return repr(self.__LinkedList)
    
    def inqueue(self, value): 
        # self._LinkedList.append(value)
        if(self.is_empty()):
            self._first = Node(value)

        self.__LinkedList.append(value)
        self._last = self.__LinkedList.tail

    def dequeue(self): 
        if(self.is_empty()):
            return None
        removed_value = self._first.value
        self.__LinkedList.delete_first()
        self._first = self.__LinkedList.head
        return removed_value
        
    def peek(self):
        if(self.is_empty()):
            return None
        return self._first.value
    
# ! testing code

q = Queue()
q.inqueue(10)
q.inqueue(20)
q.inqueue(30)
print(q)  # Output: Node(10)->Node(20)->Node(30)
print("Dequeue:", q.dequeue())  # Output: Dequeue: 10
print("Dequeue:", q.dequeue())  # Output: Dequeue: 20
print(q)  # Output: Node(30)
print("Peek:", q.peek())  # Output: Peek: 30
print("Size:", q.size())  # Output: Size: 1 
print("Is Empty:", q.is_empty())  # Output: Is Empty: False


print("-------------Looping---------------")
q.inqueue(40)
q.inqueue(80)
q.inqueue(90)
q.inqueue(70)
while(q.size() > 0):
    print("Dequeue:", q.dequeue())


        



