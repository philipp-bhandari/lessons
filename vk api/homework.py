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


TOKEN = '48302be079021fa288200c0d8b83051690d2abad3fc01af1aea24c3a1b8fe1b069718b9a1e49c75cc9078'


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
        mutual_friends = []
        counter = 0
        for friend in self.friend_list:
            if friend in other.friend_list:
                counter += 1
                print(f'Общих друзей найдено: {counter}')
                user = VkUser(friend)
                time.sleep(1)  # Может быть проблема с количеством запросов к API, можно поиграть со временем.
                mutual_friends.append(user)
        return mutual_friends


first_user = VkUser('2181463')

second_user = VkUser('47493398')

mutual_list = first_user & second_user

print(f'\nОбщие друзья для {first_user.name} {first_user.last_name} и {second_user.name} {second_user.last_name}:\n')
for user in mutual_list:
    print(user.id)
    print(user.name, user.last_name)
    print('*' * 3)



















