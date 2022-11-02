class CircularQueue:
    def __init__(self, cap):
        self.data = list()
        self.size = 0
        self.front = -1
        self.capacity = cap
    def enqueue(self, d):
        if self.size < self.capacity:
            self.data.append(d)
            self.size += 1
            self.front = 0
    def dequeue (self):
        if self.size > 0:
            hasil = self.data[self.front]
            self.data.pop(self.front)
            self.size -= 1
            return hasil
        else:
            print("Antrian kosong")
    def __len__(self):
        return self.size
    def front(self):
        return self.data[self.front]
    def display(self):
        if self.size < self.capacity:
            print('Yang ada pada antrian adalah:','',end='')
            for d in self.data:
                print(d,'',end='')
            print()
        elif self.size == self.capacity:
            print('Yang ada pada antrian circular adalah:','',end='')
            for d in self.data:
                print(d,'',end='')
            print()
            print('Antrian penuh')
CircularQueue = CircularQueue(5)
CircularQueue.enqueue(14)
CircularQueue.enqueue(22)
CircularQueue.enqueue(13)
CircularQueue.enqueue(-6)
CircularQueue.display()
print("Data yang dihapus adalah = ", CircularQueue.dequeue())
print("Data yang dihapus adalah = ", CircularQueue.dequeue())
CircularQueue.display()
CircularQueue.enqueue(9)
CircularQueue.enqueue(20)
CircularQueue.enqueue(5)
CircularQueue.display()