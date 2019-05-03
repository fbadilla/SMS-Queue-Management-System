import json
from django.http import HttpRequest
from django.test import SimpleTestCase
from api.family_datastructure import Family
# initialize a 'Doe' family
family = Family(last_name='Doe')

class HomePageTests(SimpleTestCase):

    """
    Testing for /api/member/
    """
    def test_3_get_all_members(self):
        print("Testing for /api/member/")

        response = self.client.get('/api/member/')

        # The path /api/member/ should exist
        self.assertEquals(response.status_code, 200)

        if(response.status_code == 200):
            content = response.json()
            # The path /api/member/ should return an array
            self.assertEquals(isinstance(content, list), True)

            # The path /api/member/ should return at least one family test_get_add_member
            self.assertEquals(len(content) > 0, True)


    """
    Testing for success GET single member: /api/member/1
    """
    def test_2_get_single_member(self):
        print("Testing for success get single member: /api/member/1")
        
        resp = self.client.get('/api/member/')
        members_before = resp.json()

        response = self.client.get('/api/member/'+str(members_before[0]["id"]))
        self.assertEquals(response.status_code, 200)

        # The path /api/member/ should exist
        if(response.status_code == 200):
            content = response.json()
            # The path /api/member/ should return an array
            self.assertEquals(isinstance(content, dict), True)

            # The path /api/member/ should return at least one family test_get_add_member
            self.assertEquals(content["id"] == 1, True)


    """
    Testing for single member: /api/member/1
    """
    def test_1_add_member(self):
        print("Testing for add member: /api/member/1")

        resp = self.client.get('/api/member/')
        members_before = resp.json()
        response = self.client.post('/api/member/', json.dumps({'first_name': 'Boby'}),
                                content_type="application/json")

        # The path /api/member/ should exist
        self.assertEquals(response.status_code, 200)

        if(response.status_code == 200):
            content = response.json()
            # The path /api/member/ should return an array
            self.assertEquals(isinstance(content, dict), True)

            # The path /api/member/ should return at least one family test_get_add_member
            self.assertEquals(content["id"] != None, True)

            resp = self.client.get('/api/member/')
            members_after = resp.json()
            self.assertEquals(len(members_after) == (len(members_before) + 1), True)


    """
    Testing for delete member: /api/member/1
    """
    def test_4_delete_member(self):
        print("Testing for delete member: /api/member/1")

        resp = self.client.get('/api/member/')
        members_before = resp.json()

        response = self.client.delete('/api/member/'+str(members_before[0]["id"]))

        # The path /api/member/ should exist
        self.assertEquals(response.status_code, 200)

        if(response.status_code == 200):
            content = response.json()
            
            # The path /api/member/ should return an array
            self.assertEquals(isinstance(content, dict), True)

            # The path /api/member/ should return at least one family test_get_add_member
            self.assertEquals(content["status"] == "ok", True)

            resp2 = self.client.get('/api/member/')
            members_after = resp2.json()
            self.assertEquals(len(members_after) == (len(members_before) - 1), True)


    """
    Testing for update member: PUT /api/member/1
    """
    def test_4_update_member(self):
        print("Testing for update member: PUT /api/member/1")

        resp = self.client.get('/api/member/')
        members_before = resp.json()

        memb = members_before[0]
        memb["first_name"] = "Tommy"
        response = self.client.put('/api/member/'+str(members_before[0]["id"]), json.dumps(memb), content_type="application/json")

        # The path /api/member/ should exist
        self.assertEquals(response.status_code, 200)

        if(response.status_code == 200):
            content = response.json()
            
            # The path /api/member/ should return an array
            self.assertEquals(isinstance(content, dict), True)

            resp3 = self.client.get('/api/member/'+str(members_before[0]["id"]))
            member = resp3.json()
            self.assertEquals(member["first_name"] == "Tommy", True)


    """
    Testing for 404 on GET single member: /api/member/78653478634587
    """
    def test_2_404_get_single_member(self):
        print("Testing for 404 on get single member: /api/member/78653478634587")
        
        response = self.client.get('/api/member/78653478634587')
        self.assertEquals(response.status_code, 404)


    """
    Testing for 404 on PUT single member: /api/member/78653478634587
    """
    def test_2_404_put_single_member(self):
        print("Testing for 404 on PUT single member: /api/member/78653478634587")
        
        response = self.client.put('/api/member/78653478634587')
        self.assertEquals(response.status_code, 404)