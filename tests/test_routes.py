import json
from tests import ApiBaseTestCase


class RoutesTestCase(ApiBaseTestCase):
    """test the HTTP routes of the application"""

    def test_post_and_get_request(self):
        """test post and get request"""
        payload = json.dumps({
            "name": 'Master Yi',
            "q": 'Alpha Strike',
            "w": 'Meditate',
            "e": 'Wuju Style',
            "r": 'Highlander',
            "store_price": 400
        })
        # add a champion to database
        self.test_client.post(
            'api/champion',
            headers={"Content-Type": "application/json"},
            data=payload
        )
        # get a champion from database
        response = self.test_client.get(
            'api/champion',
        )
        self.assertEqual(1, len(response.json))
        self.assertEqual('Master Yi', response.json['champions'][0]['name'])

    def test_delete_request(self):
        "test delete request"
        payload = json.dumps({
            "name": 'Master Yi',
            "q": 'Alpha Strike',
            "w": 'Meditate',
            "e": 'Wuju Style',
            "r": 'Highlander',
            "store_price": 400
        })
        # add a champion to database
        self.test_client.post(
            'api/champion',
            headers={"Content-Type": "application/json"},
            data=payload
        )
        # get a champion from database
        response = self.test_client.get(
            'api/champion',
        )
        self.assertEqual(1, len(response.json['champions']))
        self.assertEqual('Master Yi', response.json['champions'][0]['name'])

        payload = json.dumps({
            'id': 4
        })
        # try to delete champion that does not exist
        response = self.test_client.delete(
            'api/champion',
            headers={"Content-Type": "application/json"},
            data=payload
        )
        self.assertEqual(
            'there is no champion resource with given id', response.json['message'])

        payload = json.dumps({
            'id': 1
        })
        response = self.test_client.delete(
            'api/champion',
            headers={"Content-Type": "application/json"},
            data=payload
        )
        self.assertEqual('champion resource deleted', response.json['message'])

        # get a champion from database
        response = self.test_client.get(
            'api/champion',
        )
        self.assertEqual(0, len(response.json['champions']))

    def test_update_request(self):
        "test update request"
        payload = json.dumps({
            "name": 'Master Yi',
            "q": 'Alpha Strike',
            "w": 'Meditate',
            "e": 'Wuju Style',
            "r": 'Highlander',
            "store_price": 400
        })
        # add a champion to database
        self.test_client.post(
            'api/champion',
            headers={"Content-Type": "application/json"},
            data=payload
        )
        # get a champion from database
        response = self.test_client.get(
            'api/champion',
        )
        self.assertEqual(1, len(response.json['champions']))
        self.assertEqual('Master Yi', response.json['champions'][0]['name'])

        # try to update non-existant champion resource
        payload = json.dumps({
            'id': 5
        })
        response = self.test_client.patch(
            'api/champion',
            headers={"Content-Type": "application/json"},
            data=payload
        )
        self.assertEqual(
            'there is no champion resource with given id', response.json['message'])

        # update a champion in database
        payload = json.dumps({
            'id': 1,
            'name': 'Jinx',
            'q': 'Switcheroo!',
            'w': 'Zap!',
            'e': 'Flame Chompers!',
            'r': 'Super Mega Death Rocket!',
            'store_price': 4800
        })
        response = self.test_client.patch(
            'api/champion',
            headers={"Content-Type": "application/json"},
            data=payload
        )
        self.assertEqual('champion resource updated', response.json['message'])
        # test for change in champion details
        response = self.test_client.get(
            'api/champion',
        )
        self.assertEqual(1, len(response.json['champions']))
        self.assertEqual('Jinx', response.json['champions'][0]['name'])
