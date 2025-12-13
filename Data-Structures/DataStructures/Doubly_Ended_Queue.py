from LinkedList import LinkedList
from DoubleLinkedList import DoublyLinkedList
from LinkedList import Node

class DoublyEndedQueue(LinkedList):

    __LinkedList = None
    _front = None
    _rear = None

    def __init__(self):
        self.__LinkedList = LinkedList()
        self._front = self.__LinkedList.head
        self._rear = self.__LinkedList.tail

    def Size(self):
        return self.__LinkedList.Size()

    def is_empty(self):
        return self.Size() == 0
    
    def __repr__(self):
        if(self.is_empty()) :
            return "Doubly Ended Queue is empty"
        values = []
        current = self.__LinkedList.head
        while(current != None):
           values.append(repr(current))
           current = current.next
        return "<-".join(values)
    
    
    def add_front(self, value): 
        if(self.is_empty()):
            self._front = Node(value)
            self._rear = self._front

        self.__LinkedList.prepend(value)
        self._front = self.__LinkedList.head


    def add_rear(self, value): 
        if(self.is_empty()):
            self._rear = Node(value)
            self._front = self._rear

        self.__LinkedList.append(value)
        self._rear = self.__LinkedList.tail

    def remove_front(self): 
        if(self.is_empty()):
            return None
        
        removed_value = self._front.value
        self.__LinkedList.delete_first()
        self._front = self.__LinkedList.head
        return removed_value
    
        
    def remove_rear(self): 
        if(self.is_empty()):
            return None
        
        removed_value = self._rear.value
        self.__LinkedList.delete_last()
        self._rear = self.__LinkedList.tail
        return removed_value
    

class Doubly_Ended_Queue(DoublyLinkedList):
    _front = None
    _rear = None
    __DList = None

    def __init__(self):
        self.__DList = DoublyLinkedList()
        _front = self.__DList.head
        _rear = self.__DList.tail

    def size(self):
        return self.__DList.Size()
    
    def is_empty(self):
        return self.size == 0
    
    def add_front(self, value):
        if(self.is_empty()):
            self._rear = Node(value)

        self.__DList.append_first(value)
        self._front = self.__DList.head


    def add_rear(self, value):
        if(self.is_empty()):
            self._front =  Node(value)

        self.__DList.append(value)
        self._rear= self.__DList.tail


    def remove_front(self):
         try:
            if(self.is_empty()):
                raise Exception("Deque is empty")
            
            value = self._front.value
            if(self.size == 1):
                self._rear = None

            self.__DList.delete_first()
            self._front = self.__DList.head  ## none or value 
            return value

         except:
             ...


    def remove_rear(self):
        try:
           if(self.is_empty()):
               raise Exception("Dequeue is empty!")
           
           value = self._rear.value
           if(self.size == 1):
               self.front = None

           self.__DList.delete_last()
           self._rear = self.__DList.tail 
           return value

        except:
            ...
    
    def __repr__(self):
        if(self.is_empty()):
           return "Doubly Ended Queue is empty"
        
        values = []
        current = self.__DList.head
        while(current != None):
            values.append(str(current.value))
            current = current.next

        return "<->".join(values)
    
    def peek_front(self):
        if(self.is_empty()):
            return None
        return self._front


    def peek_rear(self):
         if(self.is_empty()):
            return None
         return self._rear


    def delete_all(self):
        self.__DList.delete_all()
        self._front = None
        self._rear = None

    

    
    #! testing code
deq = Doubly_Ended_Queue()
deq.add_rear(10)
deq.add_front(20)
deq.add_rear(30)
print(deq)  # Output: 20<->10<->30
print("Remove Front:", deq.remove_front())  # Output: Remove Front: 20
print("Remove Rear:", deq.remove_rear())  # Output: Remove Rear: 30
print(deq)  # Output: 10
print("Peek Front:", deq.peek_front())  # Output: Peek Front:10
print("Peek Rear:", deq.peek_rear())  # Output: Peek Rear: 10

