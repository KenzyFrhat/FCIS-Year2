class Node:
    value = None
    next = None
    prev = None

    def __init__(self, value=None):
        self.value = value
    
    def __repr__(self):
        return f"Node({self.value})"

class DoublyLinkedList(Node):
    head = None
    tail = None
    size = None

    def __init__(self):
        self.size = 0

    def __repr__(self):
        if(self.is_empty()):
            return "List is empty"
        
        current = self.head
        values = []
        while(current != None):
            values.append(repr(current))
            current = current.next

        return "->".join(values)
            

    
    def is_empty(self):
        return self.size == 0
        
    def size(self):
        return self.size
    
    
    def find_node(self, value):
        if(self.is_empty()):
            return None
        current = self.head
        while(current != None):
            if(current.value == value):
                return current 
            current = current.next

    
    def append(self, value):
        node = Node(value)

        if(self.is_empty()):
            self.tail = node
            self.head = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1
    
    def append_first(self, value):
        if(self.is_empty()):
            self.append(value)
        else:
            node = Node(value)
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.size += 1


    def append_after(self, target_value, value):
        try:
           if(self.is_empty()):
               raise Exception("List is Empty!")
           
           target_node = self.find_node(target_value)
           if(target_node == None):
               raise Exception('Target value is not exist in the linkedlist')
           
           if(target_value == self.tail.value):
               self.append(value)
               return

           new_node = Node(value)
           new_node.prev = target_node
           new_node.next = target_node.next
           target_node.next.prev = new_node
           target_node.next = new_node
           self.size += 1

        except:
            ...

    def append_before(self, target_value, value):
        try:
           if(self.is_empty()):
               raise Exception("List is Empty!")
           
           target_node = self.find_node(target_value)
           if(target_node == None):
               raise Exception('Target value is not exist in the linkedlist')
           
           if(target_value == self.head.value):
               self.append_first(value)
               return

           new_node = Node(value)
           target_node.prev.next = new_node
           new_node.prev = target_node.prev
           target_node.prev = new_node
           new_node.next = target_node
           self.size += 1

        except:
            ...

    def is_Exist(self, value):
        if(self.is_empty()):
            return False
        else:
            current = self.tail
            while(current != None):
                if(current.value == value):
                    return True
                current = current.prev
            return False


    def delete_all(self):
        tail = None
        head = None
        size = 0
        self.size = 0
        
    def delete_first(self):
        if(self.is_empty()):
            return 
        
        self.head.next.prev = None
        self.head = self.head.next
        self.size -= 1

    def delete_last(self):
         if(self.is_empty()):
            return 
        
         self.tail.prev.next = None
         self.tail = self.tail.prev
         self.size -= 1

    def delete(self, value):
        try:
            if(self.is_empty()):
                raise Exception("Empty List!")
            
            if(self.head.value == value):
                self.delete_first()
            if(self.tail.value == value):
                self.delete_last()
            
            node = self.find_node(value)
            if(node == None):
                raise Exception("Value is not Exist!")
            
            node.prev.next = node.next 
            node.next.prev = node.prev
            self.size -= 1

        except:
            ...

        
       


#! testing code 

ll = DoublyLinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print(ll)  # Output: Node(10)->Node(20)->Node(30)

ll.append_first(5)
print(ll)  # Output: Node(5)->Node(10)->Node(20)->Node(30)

ll.append_after(20, 25)
print(ll)  # Output: Node(5)->Node(10)->Node(20)->Node(25)->Node(30)

ll.append_before(10, 7)
print(ll)  # Output: Node(5)->Node(7)->Node(10)->Node(20)->Node(25)->Node(30)

ll.append_before(5, 1)
print(ll)  # Output: Node(1)->Node(5)->Node(7)->Node(10)->Node(20)->Node(25)->Node(30)

ll.append_after(30, 35)
print(ll)  # Output: Node(1)->Node(5)->Node(7)->Node(10)->Node(20)->Node(25)->Node(30)->Node(35)

print(ll.is_Exist(25))  # Output: True
print(ll.is_Exist(100))  # Output: False

# testing deleting
ll.delete_first()
print(ll)

ll.delete_last()
print(ll)

ll.delete(10)
print(ll)


ll.delete_all()
print(ll)



    
    





    

