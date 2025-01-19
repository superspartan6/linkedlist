class linkedlist():
    class node():
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0



    def addValue(self, value):
        node = self.node(value)
        self.size += 1
        currentnode = self.head
        while currentnode != None:
            if currentnode.next == None:
                currentnode.next = node
                return
            else:
                currentnode = currentnode.next
        self.head = node
        


    def insertValue(self, index, value):
        if self.size < index or index < 0: #index out of range
            print("Index out of range")
            return -1
        else:
            node = self.node(value)
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

             

    def removefirstValue(self, value): #remove first instance of value
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



    def removeAllValue(self, value): #remove any instances of value
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

        

    def removeIndex(self, index):
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

            

    def removeAll(self):
        self.head = None
        self.size = 0



    def searchValue(self, value): # Returns the index for first matching value
        currentnode = self.head

        index = 0
        while currentnode != None:
            if currentnode.value == value:
                return index
            currentnode = currentnode.next
            index += 1
        return -1
    


    def searchAllValue(self, value): # Returns list of index values for each matching value 
        currentnode = self.head
        indexes = []

        index = 0
        while currentnode != None:
            if currentnode.value == value:
                indexes.append(index)
            currentnode = currentnode.next
            index += 1
        return indexes
    
        

    def searchIndex(self, index): # Returns value at index
        if self.size < index or self.size < 1 or index < 0: #index out of range
            print("Index out of range")
            return -1
        else:
            currentnode = self.head
            for _ in range(index):
                currentnode = currentnode.next
            return currentnode.value



    def updateIndex(self, index, value): # by index
        if self.size < index or self.size < 1 or index < 0: #index out of range
            print("Index out of range")
            return -1
        else:
            currentnode = self.head
            for _ in range(index):
                currentnode = currentnode.next
            currentnode.value = value



    def getSize(self):
        return self.size



    def sort(self):
        pass



    def returnList(self):
        currentnode = self.head
        returnlist = []
        while currentnode != None:
            returnlist.append(currentnode.value)
            currentnode = currentnode.next
        return returnlist





newlist = linkedlist()


