class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, element, index):
        if index == len(self.heap):
            self.heap.append(element)
        parent_index = self.getParent(index)
        if parent_index == -1:
            return
        if self.heap[parent_index] < element:
            self.heap[parent_index], self.heap[index] = element, self.heap[parent_index] 
            self.insert(element, parent_index)


    def getParent(self, index):
        if index == 0:
            return -1
        elif (index - 1) % 2 == 0:
            return (index - 1) // 2
        else:
            return (index -2) // 2

    def printHeap(self):
        print(self.heap)

    def getHeapLen(self):
        return len(self.heap)

h = Heap()
h.insert(1, h.getHeapLen())
h.insert(2, h.getHeapLen())
h.insert(4, h.getHeapLen())
h.insert(3, h.getHeapLen())
h.insert(65, h.getHeapLen())
h.insert(7, h.getHeapLen())
h.printHeap()
