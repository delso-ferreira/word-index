from ting_file_management.abstract_queue import AbstractQueue


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue(AbstractQueue):
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def __str__(self) -> str:
        return (f"Queue(len={self._size}), values={self.first}")

    def __len__(self):
        return self._size

    def enqueue(self, value):
        node = Node(value)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            raise Exception("Não há elementos")

        value = self.first.value
        self.first = self.first.next

        if self.first is None:
            self.last = None

        self._size -= 1
        return value

    def search(self, index):

        pointer = self.first
        current_index = 0
        while pointer is not None:
            if current_index == index:
                return pointer.value
            pointer = pointer.next
            current_index += 1

        raise IndexError("Índice Inválido ou Inexistente")
