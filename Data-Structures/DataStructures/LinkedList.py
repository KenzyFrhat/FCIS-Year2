class Node:
    _value = None  #protected attribute
    _next = None

    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    def __repr__(self):
        return f"Node({self.value})"
    
class LinkedList(Node):
    head = None
    tail = None
    size = None

    def __init__(self):
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def Size(self):
        return self.size
        
    
    def append(self, value):
        New_Node = Node(value)

        if(self.is_empty()):
            self.tail = New_Node
            self.head = New_Node
        else:
            self.tail.next = New_Node
            self.tail = New_Node

        self.size += 1


    def prepend(self, value):
        if(self.is_empty()):
            self.append(value)
            return None
        
        New_Node = Node(value)
        New_Node.next = self.head
        self.head = New_Node
        self.size += 1
    
    def is_Exist(self, value):
        if(self.is_empty()):
            return False
        
        current = self.head
        while(current != None):
            if(current.value == value):
                return True
            current = current.next
    

    def Find(self, value):
        if(self.is_empty()):
            return None
        
        current = self.head
        while(current != None):
            if(current.value == value):
                return current
            current = current.next
        
        return None
    
    def Find_parent(self, value):
        if(self.is_empty()):
            return None
        
        if(value == self.head.value):
            return None
        
        current = self.head 
        while(current != None):
            if(current.next.value == value):
                return current
            current = current.next
            
        return None
    

        
    
    
    def append_after(self, target_value, new_value):
        try:
            if(self.is_empty()):
                raise Exception("The list is empty.")
            
            target_node = self.Find(target_value)
        
            if(target_node == None):
                raise Exception("Target value not found in the list.")
            
            if(target_node == self.tail):
                self.append(new_value)
                return None
            
            New_Node = Node(new_value)
            New_Node.next = target_node.next
            target_node.next = New_Node
            self.size += 1

        except:
             ...

    def append_before(self, target_value, new_value):
        try:
            if(self.is_empty()):
                raise Exception("The list is empty.")
    
            target_node = self.Find(target_value)
            if(target_node == Node):
                raise Exception("Target value not found in the list.")
          
            if(self.head.value == target_value):
                self.prepend(new_value)
                return None
              
            new_node = Node(new_value)
            parent_node = self.Find_parent(target_value)
            new_node.next = target_node
            parent_node.next = new_node
            self.size += 1

        except: 
            ...

    def __repr__(self):
        if(self.is_empty()):
            return "LinkedList is empty."
        
        current = self.head
        values = []
        while(current != None):
            values.append(repr(current))
            current = current.next
        
        return "->".join(values)
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.size = 0

    def delete_first(self):
        try:
            if(self.is_empty()):
                raise Exception("The list is empty.")
            self.head = self.head.next
            self.size -= 1
        except:
            ...
    
    def delete_last(self):
        try:
            if(self.is_empty()):
                raise Exception("The list is empty.")
            if(self.size == 1):
                self.delete_all()
                return None
            parent_node = self.Find_parent(self.tail.value)
            parent_node.next = None
            self.tail = parent_node
            self.size -= 1
            
        except:
            ...
      

    def delete(self, value):
        try:
            if(self.is_empty()):
                raise Exception("The list is empty.")
    
            target_node = self.Find(value)
            if(target_node == None):
                raise Exception("Target value not found in the list.")
            
            if(value == self.head.value):
                self.delete_first()
                return None
            
            parent_node = self.Find_parent(value)
            parent_node.next = target_node.next
            self.size -= 1
        except:
            ...


             
# #! testing code 

# ll = LinkedList()
# ll.append(10)
# ll.append(20)
# ll.append(30)
# print(ll)  # Output: Node(10)->Node(20)->Node(30)

# ll.prepend(5)
# print(ll)  # Output: Node(5)->Node(10)->Node(20)->Node(30)

# ll.append_after(20, 25)
# print(ll)  # Output: Node(5)->Node(10)->Node(20)->Node(25)->Node(30)

# ll.append_before(10, 7)
# print(ll)  # Output: Node(5)->Node(7)->Node(10)->Node(20)->Node(25)->Node(30)

# ll.append_before(5, 1)
# print(ll)  # Output: Node(1)->Node(5)->Node(7)->Node(10)->Node(20)->Node(25)->Node(30)

# ll.append_after(30, 35)
# print(ll)  # Output: Node(1)->Node(5)->Node(7)->Node(10)->Node(20)->Node(25)->Node(30)->Node(35)

# print(ll.is_Exist(25))  # Output: True
# print(ll.is_Exist(100))  # Output: False

# # testing deleting
# ll.delete_first()
# print(ll)

# ll.delete_last()
# print(ll)

# ll.delete(10)
# print(ll)
# print("Hello from linked list")

# ll.delete_all()
# print(ll)



    
    


