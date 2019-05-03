"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
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
    def size(self):

        # fill this function with the logic needed to make it work
        pass