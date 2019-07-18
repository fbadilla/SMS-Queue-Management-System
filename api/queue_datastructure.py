"""
update this file to implement the following already declared methods:
- enqueue: Should add a member to the list
- dequeue: Should remove and return an element from the top or the bottom of the list (depending on the list mode: FIFO or LIFO)
- get_all: should return the entire list as it is
- size: Should return the total size of the list
"""
from random import randint
from twilio.rest import Client


class Twilio:

    def twilio():
        account_sid = 'AC2c1a128f41136b3dc5dea260aebe0cc3'
        auth_token = 'e83d3973503b8cf130fdc2448f00d1ff'
        client = Client(self.account_sid, self.auth_token)

        message = client.messages \
            .create(
                body="holi, prueba prueba prueba",
                from_='+56937610229',
                to='+56937257893'
            )

        print(message.sid)


class Queue:

    def __init__(self, mode='FIFO'):
        self._queue = []
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        self._mode = mode
        self.account_sid = 'AC2c1a128f41136b3dc5dea260aebe0cc3'
        self.auth_token = 'e83d3973503b8cf130fdc2448f00d1ff'
        self.client = Client(self.account_sid, self.auth_token)

    def enqueue(self, item):
        if self._mode == 'FIFO':
            self._queue.insert(0, item)
            message = self.client.messages \
                .create(
                    body="holi, prueba prueba prueba",
                    from_='+56937610229',
                    to='+56937257893'
                )
        print(message.sid)
        return item

    def dequeue(self):
        if self._mode == 'FIFO':
            return self._queue.pop()
        else:
            return self._queue.pop(0)

    def get_all(self):
        return self._queue

    def size(self):
        return len(self._queue)
