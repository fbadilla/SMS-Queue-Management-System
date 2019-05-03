"""
update this file to implement the following already declared methods:
- enqueue: Should add a member to the list
- dequeue: Should remove and return an element from the top or the bottom of the list (depending on the list mode: FIFO or LIFO)
- get_all: should return the entire list as it is
- size: Should return the total size of the list
"""
from random import randint

class Queue:

    def __init__(self, mode='FIFO'):
        self._queue = []
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        self._mode = mode

    def enqueue(self, item):
        # fill this function with the logic needed to make it work
        pass

    def dequeue(self):
        # fill this function with the logic needed to make it work
        pass

    def get_all(self):

        # fill this function with the logic needed to make it work
        pass

    def size(self):

        # fill this function with the logic needed to make it work
        pass
