class LinkedList():
    class Node():
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0



    class _Iterator():
        def __init__(self, start_node):
            self.current = start_node

        def __iter__(self):
            return self

        def __next__(self):
            if self.current == None:
                raise StopIteration
            value = self.current.value
            self.current = self.current.next
            return value

    def __iter__(self):
        return LinkedList._Iterator(self.head)


    def add_value(self, value):
        node = self.Node(value)
        self.size += 1
        currentnode = self.head
        while currentnode != None:
            if currentnode.next == None:
                currentnode.next = node
                return
            else:
                currentnode = currentnode.next
        self.head = node
        


    def insert_value(self, index, value):
        if self.size < index or index < 0: #index out of range
            print("Index out of range")
            return -1
        else:
            node = self.Node(value)
            self.size += 1
            if index == 0: #insert at front
                node.next = self.head
                self.head = node
            else:
                currentnode = self.head

                for _ in range(index):
                    prevnode = currentnode
                    currentnode = currentnode.next

                prevnode.next = node
                node.next = currentnode

             

    def remove_first_value(self, value): #remove first instance of value
        currentnode = self.head
        previousnode = self.head
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
        else: 
            while currentnode != None:
                if currentnode.value == value:
                    previousnode.next = currentnode.next
                    self.size -= 1
                    return
                else:
                    previousnode = currentnode
                    currentnode = currentnode.next



    def remove_all_value(self, value): #remove any instances of value
        currentnode = self.head
        previousnode = self.head
        while currentnode != None:
            if currentnode.value == value:
                if self.head == currentnode:
                    self.head = currentnode.next
                else:
                    previousnode.next = currentnode.next
                self.size -= 1
            else:
                previousnode = currentnode
            currentnode = currentnode.next

        

    def remove_index(self, index):
        if self.size < index or self.size < 1 or index < 0: #index out of range
            print("Index out of range")
            return -1
        else:
            if index == 0:
                self.head = self.head.next
            else:
                currentnode = self.head
                prevnode = self.head
                for _ in range(index):
                    prevnode = currentnode
                    currentnode = currentnode.next
                prevnode.next = currentnode.next
            self.size -= 1

            

    def remove_all(self):
        self.head = None
        self.size = 0



    def search_value(self, value): # Returns the index for first matching value
        currentnode = self.head

        index = 0
        while currentnode != None:
            if currentnode.value == value:
                return index
            currentnode = currentnode.next
            index += 1
        return -1
    


    def search_all_value(self, value): # Returns list of index values for each matching value 
        currentnode = self.head
        indexes = []

        index = 0
        while currentnode != None:
            if currentnode.value == value:
                indexes.append(index)
            currentnode = currentnode.next
            index += 1
        return indexes
    
        

    def search_index(self, index): # Returns value at index
        if self.size < index or self.size < 1 or index < 0: #index out of range
            print("Index out of range")
            return -1
        else:
            currentnode = self.head
            for _ in range(index):
                currentnode = currentnode.next
            return currentnode.value



    def update_index(self, index, value): # by index
        if self.size < index or self.size < 1 or index < 0: #index out of range
            print("Index out of range")
            return -1
        else:
            currentnode = self.head
            for _ in range(index):
                currentnode = currentnode.next
            currentnode.value = value



    def get_size(self):
        return self.size



    def sort(self):
        pass



    def return_list(self):
        currentnode = self.head
        returnlist = []
        while currentnode != None:
            returnlist.append(currentnode.value)
            currentnode = currentnode.next
        return returnlist
