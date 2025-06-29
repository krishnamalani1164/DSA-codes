class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push_front(self,data):
        new_node = Node(data)
        #If Linked List is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.next = self.head
        self.head = new_node

    def push_back(self,data):
        new_node = Node(data)
        #If Linked List is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_position(self,position,data):
        new_node = Node(data)
        #1 st Case
        if position == 0:
            new_node.next=self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
            return
        #2nd Case
        temp=self.head
        for i in range(position-1):
            if temp is None:
                return
            temp=temp.next
        new_node.next=temp.next
        temp.next = new_node
        if new_node.next is None:
            self.tail = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next

    def delete_node(self,key):
        temp=self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                if self.head is None:
                    self.tail = None
                temp=None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev=temp
            temp=temp.next
        #Means the key was not found
        if temp is None:
            return
        prev.next = temp.next
        if temp == self.tail:
            self.tail = prev
        #By setting it to None we are efficitevely deleting the node.
        temp = None

    def pop_front(self):
        if self.head is None:
            print("List is Empty")
            return 
        
        temp=self.head
        self.head = temp.next

        #If the list is now empty,update the tail to None
        if self.head is None:
            self.tail = None
        temp.next=None

    def pop_back(self):
        if self.head is None:
            print("List is Empty")
            return
        
        if self.head.next is None:
            # There is only one element in the list
            temp = self.head
            self.head = None
            self.tail = None
            temp = None
            return
        
        # Traverse to the second-last node
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        
        # Remove the last node
        to_delete = temp.next
        temp.next = None
        self.tail = temp
        to_delete = None