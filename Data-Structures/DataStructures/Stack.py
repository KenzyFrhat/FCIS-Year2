from LinkedList import LinkedList

class Stack(LinkedList):
    _top = None
    __LinkedList = None

    def __init__(self):
        self.__LinkedList = LinkedList()
        self._top  = self.__LinkedList.tail

    def __repr__(self):
        values = []
        current = self.__LinkedList.head
        while(current != None):
            values.append(f"--{current.value}--")
            current = current.next

        return  "\n".join(values[::-1])
    
    def Size(self):
        return self.__LinkedList.Size()
    
    def is_empty(self):
        return self.Size() == 0
    
    def push(self, value):
        self.__LinkedList.append(value)
        self._top = self.__LinkedList.tail
        
    def peek(self):
        return self._top
    
    def pop(self):
        removed_value = self._top
        self.__LinkedList.delete_last()
        self._top = self.__LinkedList.tail
        return removed_value
    

stack = Stack()
stack.push(23)
stack.push(98)
stack.push(34)
stack.push(56)
stack.push(2)
stack.push(33)
stack.push(93)

# print(stack.peek())

while(stack.is_empty() == False):
    print(f"{stack.pop()}")




