class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [None] * k
        self.max_size = k
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        # front 자리가 비어 있다면 삽입
        if self.deque[self.front] is None:
            self.deque[self.front] = value
            return True
        # front 앞이 비어 있다면 삽입 후 front-1
        elif self.deque[self.front-1] is None:
            self.front -= 1
            self.deque[self.front] = value
            if self.front < 0:
                self.front += self.max_size
            return True
        return False

    def insertLast(self, value: int) -> bool:
        # rear 자리가 비어 있다면 삽입
        if self.deque[self.rear] is None:
            self.deque[self.rear] = value
            return True
        # rear 뒷 자리가 비어 있다면 삽입 후 rear+1
        if (self.rear + 1) % self.max_size != self.front:
            self.rear = (self.rear + 1) % self.max_size
            self.deque[self.rear] = value
            return True
        return False

    def deleteFront(self) -> bool:
        # 덱이 비어 있다면 삭제 불가
        if self.deque[self.front] is None and self.front == self.rear:
            return False
        # 덱에 원소가 하나만 있을 때
        elif self.deque[self.front] is not None and self.front == self.rear:
            self.deque[self.front] = None
            return True
        self.deque[self.front] = None
        self.front = (self.front + 1) % self.max_size
        return True

    def deleteLast(self) -> bool:
        # 덱이 비어 있다면 삭제 불가
        if self.deque[self.rear] is None and self.front == self.rear:
            return False
        # 덱이 원소가 하나만 있을 때
        elif self.deque[self.rear] is not None and self.front == self.rear:
            self.deque[self.rear] = None
            return True
        self.deque[self.rear] = None
        self.rear -= 1
        if self.rear < 0:
            self.rear += self.max_size
        return True

    def getFront(self) -> int:
        if self.deque[self.front] is not None:
            return self.deque[self.front]
        return -1

    def getRear(self) -> int:
        if self.deque[self.rear] is not None:
            return self.deque[self.rear]
        return -1

    def isEmpty(self) -> bool:
        if self.deque[self.front] is None and self.front == self.rear:
            return True
        return False

    def isFull(self) -> bool:
        if (self.rear + 1) % self.max_size == self.front:
            return True
        return False
