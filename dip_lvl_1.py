import requests
import time
import json


access_token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'


class User:

    def __init__(self, user_id):
        self.user_id = user_id

    def get_params(self):
        return {
            'access_token': access_token,
            'v': 5.103,
            'scope': 'friends, groups'
        }

    def get_friends(self):
        params = self.get_params()
        params['user_id'] = self.user_id
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params
        )
        a1 = []
        for a in response.json()['response']['items']:
            a1.append(a)
        return a1

    def get_users(self, u_ids):
        params = self.get_params()
        params['user_ids'] = u_ids
        params['fields'] = 'is_friend, blacklisted', 'deactivated'
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params
        )
        a1 = []
        for a in response.json()['response']:
            time.sleep(0.3)
            a1.append(a)
        return a1

    def get_group_info(self):
        params = self.get_params()
        params['extended'] = 1
        response = requests.get(
            'https://api.vk.com/method/groups.get',
            params
        )
        a1 = []
        for a in response.json()['response']['items']:
            a1.append(a)
        return a1

    def get_group_members(self, g_id, u_ids):
        params = self.get_params()
        params['group_id'] = g_id
        params['user_ids'] = str(u_ids)
        response = requests.get(
            'https://api.vk.com/method/groups.isMember',
            params
        )
        a1 = []
        for a in response.json()['response']:
            a1.append(a['member'])
        return sum(a1)

    def get_group_friends(self, g_id):
        params = self.get_params()
        params['group_id'] = g_id
        response = requests.get(
            'https://api.vk.com/method/groups.getMembers',
            params
        )
        return response.json()


target_user = User(171691064)

a = target_user.get_group_info()
b = target_user.get_friends()

with open('groups.json', 'w', encoding='utf-8') as f:
    file1 = []
    file2 = []
    file3 = 0
    file = [file1, file2]
    for bbb in b:
        if target_user.get_users(bbb) != 0:
            try:
                file3 += 1
                if file3 == len(b):
                    for aaa in a:
                        time.sleep(1)
                        if target_user.get_group_members(aaa['id'], b) == 0:
                            file1.append(
                                {
                                    "name": aaa['name'],
                                    "gid": aaa['id'],
                                    "members_count": target_user.get_group_friends(aaa['id'])['response']['count']
                                }
                            )
                        elif 0 < target_user.get_group_members(aaa['id'], b) < 1000:
                            file2.append(
                                {
                                    "friends": target_user.get_group_members(aaa['id'], b),
                                    "name": aaa['name'],
                                    "gid": aaa['id'],
                                    "members_count": target_user.get_group_friends(aaa['id'])['response']['count']
                                }
                            )
                decimal = (file3/len(b))
                print(f'{round(decimal*100, 3)} % completed')
            except KeyError as KE:
                print(KE, 'KeyError')
    json.dump(file, f, ensure_ascii=False, indent=2)
