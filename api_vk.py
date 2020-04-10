import requests
from urllib.parse import urlencode
from pprint import pprint
import time

OAUTH_URL = 'https://oauth.vk.com/authorize'
OAUTH_PARAMS = {
    'client_id': 7357778,
    'response_type': 'token',
    'display': 'popup',
    'scope': 'friends, users'
    }

# print('?'.join((OAUTH_URL, urlencode(OAUTH_PARAMS))))

TOKEN = '35e07ecd57c3feaa0bc14626f5526d571d1a343525e98d931a2491e2473e92a1527c2908c0970fcf6cb31'


class User:

    def __init__(self, user_id):
        self.user_id = user_id

    def get_params(self):
        return {
            'access_token': TOKEN,
            'v': 5.103,
            'scope': 'friends, users',
        }

    def get_info(self, u_ids):
        params = self.get_params()
        params['user_ids'] = u_ids
        response_i = requests.get(
            'https://api.vk.com/method/users.get',
            params
        )
        return response_i.json()

    def __and__(self, other):
        params = self.get_params()
        params['source_uid'] = self.user_id
        params['target_uid'] = other.user_id
        response_f = requests.get(
            'https://api.vk.com/method/friends.getMutual',
            params
        )
        time.sleep(0.4)
        for mut_friends in response_f.json()['response']:
            pprint(self.get_info(mut_friends))
        return

    def __str__(self):
        return 'https://vk.com/id{}'.format(self.user_id)


user1 = User(5148473)
user2 = User(263894468)

print(user1 & user2, '\n')

print(user1)
