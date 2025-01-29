class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = []
        self.size = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.size +=1
        self.arr.append(n)

    def popback(self) -> int:
        if self.size == 0 :
            return
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        self.capacity *= 2


    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
