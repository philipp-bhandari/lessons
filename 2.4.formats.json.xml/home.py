from pprint import pprint
import xml.etree.ElementTree as ET
import json
import os

#  Написать программу, которая будет выводить топ 10 самых
#  часто встречающихся в новостях слов длиннее 6 символов для каждого файла.


class Reader:
    def top_ten(self, data, type):
        temp_list = []
        temp_dict = {}

        for item in data:

            if type == 'json':
                words = item['description'].split()
            else:
                words = item.text.split()
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


class JsonReader(Reader):
    def read_file(self, filename):
        with open(filename) as datafile:
            json_data = json.load(datafile)
        return json_data


class XmlReader(Reader):
    def read_file(self, filename):
        parser = ET.XMLParser(encoding='utf-8')
        tree = ET.parse(filename, parser=parser)
        root = tree.getroot()
        return root


json_reader = JsonReader()
xml_reader = XmlReader()

path = os.getcwd()

json_path = os.path.join(path, 'files', 'newsafr.json')
xml_path = os.path.join(path, 'files', 'newsafr.xml')


# JSON
json_file = json_reader.read_file(json_path)
json_items = json_file['rss']['channel']['items']


# XML
xml_file = xml_reader.read_file(xml_path)
xml_items = xml_file.findall('channel/item/description')

json_reader.top_ten(json_items, 'json')
print('\n')
xml_reader.top_ten(xml_items, 'xml')
