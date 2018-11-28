from pprint import pprint
import json
import os

#  Написать программу, которая будет выводить топ 10 самых
#  часто встречающихся в новостях слов длиннее 6 символов для каждого файла.

class JsonReader:

    def read_file(self, filename):
        with open(filename) as datafile:
            json_data = json.load(datafile)

        return json_data


class XmlReader:
    pass


reader = JsonReader()
path = os.getcwd()
json_path = os.path.join(path, 'files', 'newsafr.json')
xml_path = os.path.join(path, 'files', 'newsafr.xml')


### JSON
json_file = reader.read_file(json_path)
json_items = json_file['rss']['channel']['items']
temp_list = []
temp_dict = {}

for item in json_items:
    words = item['description'].split()
    for word in words:
        count = len(word)
        if count > 6:
            temp_list.append(word)


for word in temp_list:
    temp_dict[word] = temp_list.count(word)


counter = 0

for i in sorted(temp_dict.items(), key=lambda x: -x[1]):
    counter += 1
    print(i[1], 'раз встретилось слово', '"', i[0], '"')
    if counter == 10:
        break




