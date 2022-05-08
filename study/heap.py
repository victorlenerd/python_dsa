import heapq

if __name__ == '__main__':

    class MinHeap:

        keys = []
        
        def __init__(self, array):
            self.heap = self.buildHeap(array)

        def buildHeap(self, array):
            for value in array:
                self.keys.append(value)
                self.siftUp(len(self.keys) - 1)

        def swap(self, x, y):
            self.keys[x-1], self.keys[y-1] = self.keys[y-1], self.keys[x-1]

        def less(self, x, y):
            return self.keys[x-1] < self.keys[y-1]

        def siftDown(self, key):
            parent = key
            child = key * 2
            while child <= len(self.keys) - 1:
                if child < len(self.keys) - 1 and self.less(child, child + 1):
                    child = child + 1
                if child <= parent:
                    break
                self.swap(child, parent)
                parent = child

        def siftUp(self, key):
            while key > 1:
                parent = key // 2

                if self.less(key, parent):
                    self.swap(key, parent)
                    key = parent
                else:
                    break

        def peek(self):
            return self.keys[0]

        def remove(self):
            v = self.keys.pop(0)
            self.siftDown(0)
            return v

        def insert(self, value):
            self.keys.append(value)
            self.siftUp(len(self.keys) - 1)


input = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41, 76, 760, 7]
heap = MinHeap(input)

heapq.heapify(input)

print(input)

print(heap.keys)
heap.insert(46)
print(heap.keys)
heap.insert(96)
print(heap.keys)
heap.insert(90)
print(heap.keys)
# heap.insert(760)
# print(self.keys)
# heap.insert(7)
# print(self.keys)
# v = heap.remove()
# print(v, self.keys)
# v = heap.remove()
# print(v, self.keys)
# heap.remove()
# print(self.keys)
# heap.remove()
# print(self.keys)
# heap.remove()
# print(self.keys)