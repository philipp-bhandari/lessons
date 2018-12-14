from urllib.parse import urlencode
import requests
from pprint import pprint
import time


APP_ID = 6777613

# AUTH_URL = 'https://oauth.vk.com/authorize?'
#
#
# auth_data = {
#     'client_id':                  APP_ID,
#     'display':                    'page',
#     'redirect_uri':               'https://vk.com',
#     'scope':                      'friends',
#     'response_type':              'token',
#     'v':                          '5.92'
# }
#
# print(AUTH_URL + urlencode(auth_data))


TOKEN = 'cbe61b01f88856a40d5181c96cad726e0848f2ab9f84b2ba9560d765c5ca096b51ee34120cc7f532a8219'


class VkUser:
    def __init__(self, id):
        self.id = id
        user = {
            'access_token': TOKEN,
            'v': '5.92',
            'user_id': self.id
        }

        response_user = requests.get('https://api.vk.com/method/users.get?', urlencode(user))
        user_info = response_user.json()
        self.name, self.last_name = user_info['response'][0]['first_name'], user_info['response'][0]['last_name']

        response_friends = requests.get('https://api.vk.com/method/friends.get?', urlencode(user))
        friends_info = response_friends.json()

        try:
            self.friend_list = friends_info['response']['items']
        except KeyError:
            self.friend_list = []

    def __and__(self, other):
        self_friends = set(self.friend_list)
        other_friends = set(other.friend_list)
        mutual_friends = self_friends.intersection(other_friends)
        users_list = []
        counter = 0

        for friend in mutual_friends:
            counter += 1
            print(f'Общих друзей найдено: {counter}')
            user = VkUser(friend)
            time.sleep(1)
            users_list.append(user)
        return users_list

    def __str__(self):
        string = f'ID: {self.id}\nИмя: {self.name}\nФамилия: {self.last_name}\n***\n'
        return string


first_user = VkUser('2181463')

second_user = VkUser('47493398')

mutual_list = first_user & second_user

print(f'\nОбщие друзья для {first_user.name} {first_user.last_name} и {second_user.name} {second_user.last_name}:\n')
for user in mutual_list:
    print(user)



















