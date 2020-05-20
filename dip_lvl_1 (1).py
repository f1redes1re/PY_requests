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
        return response.json()['response']['items']

    def get_self_groups(self):
        params = self.get_params()
        params['user_id'] = self.user_id
        params['extended'] = 1
        response = requests.get(
            'https://api.vk.com/method/groups.get',
            params
        )
        return response.json()['response']['items']

    def get_friend_groups(self, u_id):
        params = self.get_params()
        params['user_id'] = u_id
        params['extended'] = 1
        response = requests.get(
            'https://api.vk.com/method/groups.get',
            params
        )
        return response.json()['response']['items']

    def get_friends_members(self, g_id, u_ids):
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
        if 0 < sum(members_list) < 1000:
            time.sleep(0.3)
            return sum(members_list)

    def get_members(self, g_id):
        params = self.get_params()
        params['group_id'] = g_id
        response = requests.get(
            'https://api.vk.com/method/groups.getMembers',
            params
        )
        return response.json()


target_user = User(171691064)
# Получение информации о группах пользователя и списка его друзей
groups = target_user.get_self_groups()
friends = target_user.get_friends()
# Получение списка id групп пользователя
self_groups_id = []
progress_self_groups = 0
for group_info in groups:
    self_groups_id.append(group_info['id'])
    progress_self_groups += 1
    calculation1 = progress_self_groups/len(groups)
    print(f'Calculating self groups {round(calculation1*100, 3)} % completed')
# Получение списка id групп друзей пользователя
friends_groups_id = []
progress_friends_groups = 0
for friend in friends:
    try:
        time.sleep(0.3)
        for friends_groups_info in target_user.get_friend_groups(friend):
            friends_groups_id.append(friends_groups_info['id'])
        progress_friends_groups += 1
        calculation2 = progress_friends_groups/len(friends)
        print(f'Calculating friends groups {round(calculation2*100, 3)} % completed')
    except Exception as E:
        continue
print(f'Only {progress_friends_groups} of {len(friends)} friends can be processed')
# Получение множества групп пользователя, непересекающегося со множеством групп его друзей
self_groups = set(self_groups_id)
friends_groups = set(friends_groups_id)
self_groups.difference_update(friends_groups)
# Получение списка нужных групп и списка групп с друзьями пользователя
target_groups = list(self_groups)
groups_with_friends = [i for i in self_groups_id if i not in target_groups]
# Запись в файл json структурированной информации о группах пользователя без друзей и с друзьями
with open('groups.json', 'w', encoding='utf-8') as f:
    secret_groups = []
    non_secret_groups = []
    total = [secret_groups, non_secret_groups]
    progress_json = 0
    for target in target_groups:
        for groups_info_1 in groups:
            if target == groups_info_1['id']:
                time.sleep(0.3)
                try:
                    secret_groups.append(
                        {
                            "name": groups_info_1['name'],
                            "gid": target,
                            "members_count": target_user.get_members(target)['response']['count']
                        }
                    )
                    progress_json += 1
                    calculation = progress_json/len(groups)
                    print(f'Writing json {round(calculation*100, 3)} % completed')
                except Exception as E:
                    continue
    for gwf in groups_with_friends:
        for groups_info_2 in groups:
            if gwf == groups_info_2['id']:
                time.sleep(0.3)
                try:
                    non_secret_groups.append(
                        {
                            "name": groups_info_2['name'],
                            "gid": gwf,
                            "members_count": target_user.get_members(gwf)['response']['count'],
                            "friends": target_user.get_friends_members(gwf, friends)
                        }
                    )
                    progress_json += 1
                    calculation = progress_json/len(groups)
                    print(f'Writing json {round(calculation*100, 3)} % completed')
                except Exception as E:
                    continue
    json.dump(total, f, ensure_ascii=False, indent=2)
