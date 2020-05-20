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
        friends_list = []
        for friend in response.json()['response']['items']:
            friends_list.append(friend)
        return friends_list

    def get_users(self, u_ids):
        params = self.get_params()
        params['user_ids'] = u_ids
        params['fields'] = 'is_friend, blacklisted', 'deactivated'
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params
        )
        users_list = []
        for user in response.json()['response']:
            time.sleep(0.3)
            users_list.append(user)
        return users_list

    def get_group_info(self):
        params = self.get_params()
        params['user_id'] = self.user_id
        params['extended'] = 1
        response = requests.get(
            'https://api.vk.com/method/groups.get',
            params
        )
        groups_list = []
        for group in response.json()['response']['items']:
            groups_list.append(group)
        return groups_list

    def get_members(self, g_id):
        params = self.get_params()
        params['group_id'] = g_id
        response = requests.get(
            'https://api.vk.com/method/groups.getMembers',
            params
        )
        return response.json()

    def get_true_members(self, g_id, u_ids):
        params = self.get_params()
        params['group_id'] = g_id
        params['user_ids'] = str(u_ids)
        response = requests.get(
            'https://api.vk.com/method/groups.isMember',
            params
        )
        members_list = []
        for member in response.json()['response']:
            members_list.append(member['member'])
        return sum(members_list)


target_user = User(171691064)

group_info = target_user.get_group_info()
friends_list = target_user.get_friends()

with open('groups.json', 'w', encoding='utf-8') as f:
    file1 = []
    file2 = []
    file3 = 0
    file = [file1, file2]
    for friend in friends_list:
        if target_user.get_users(friend) != 0:
            try:
                file3 += 1
                if file3 == len(friends_list):
                    for target_group in group_info:
                        time.sleep(1)
                        if target_user.get_true_members(target_group['id'], friends_list) == 0:
                            file1.append(
                                {
                                    "name": target_group['name'],
                                    "gid": target_group['id'],
                                    "members_count": target_user.get_members(target_group['id'])['response']['count']
                                }
                            )
                        elif 0 < target_user.get_true_members(target_group['id'], friends_list) < 1000:
                            file2.append(
                                {
                                    "friends": target_user.get_true_members(target_group['id'], friends_list),
                                    "name": target_group['name'],
                                    "gid": target_group['id'],
                                    "members_count": target_user.get_members(target_group['id'])['response']['count']
                                }
                            )
                decimal = (file3/len(friends_list))
                print(f'{round(decimal*100, 3)} % completed')
            except KeyError as KE:
                print(KE, 'KeyError')
    json.dump(file, f, ensure_ascii=False, indent=2)
