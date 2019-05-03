import json
from django.http import HttpRequest
from django.test import SimpleTestCase
from api.queue_datastructure import queue
# initialize a 'Doe' family
queue = Queue(type='FIFO')

class HomePageTests(SimpleTestCase):

    def test_2_all(self):
        """
        Testing for GET /all/
        """
        print("Testing for GET /all/")

        response = self.client.get('/all/')

        # The path /all should exist
        self.assertEquals(response.status_code, 200)

        if response.status_code == 200:
            content = response.json()
            # The path /next_in_line should return a dictionary o None
            self.assertEquals(isinstance(content, list), True)

    def test_3_get_next_in_line(self):
        """
        Testing for success GET single member: /next_in_line/
        """
        print("Testing for success get single member: /next_in_line/")

        response = self.client.get('/next_in_line/')
        self.assertEquals(response.status_code, 200)

        # The path /api/member/ should exist
        if response.status_code == 200:
            content = response.json()
            # The path /api/member/ should return an array
            self.assertEquals(isinstance(content, dict), True)

            # The path /api/member/ should return at least one family test_get_add_member
            self.assertEquals(content["id"] == 1, True)

    def test_1_new_in_line(self):
        """
        Testing for single member: POST /new_in_line/
        """
        print("Testing for new person in line: /new_in_line/")

        response = self.client.post('/new_in_line/', json.dumps(
            {
                'first_name': 'Boby',
                'phone': '7867234576'
            }),
            content_type="application/json"
        )

        # The path /new_in_line/ should exist
        self.assertEquals(response.status_code, 200)

        if(response.status_code == 200):
            content = response.json()
            # The path /api/member/ should return an array
            self.assertEquals(isinstance(content, dict), True)

            # The path /api/member/ should return at least one family test_get_add_member
            self.assertEquals(content["id"] != None, True)

            # resp = self.client.get('/api/member/')
            # members_after = resp.json()
            # self.assertEquals(len(members_after) == (len(members_before) + 1), True)

