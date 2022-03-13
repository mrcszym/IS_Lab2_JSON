# -*- coding: utf-8 -*-
"""
deserialize json
"""
import json


class DeserializeJson:

    def __init__(self, filename):
        print("let's deserialize something")
        tempdata = open(filename, encoding="utf8")
        self.data = json.load(tempdata)

    def somestats(self):
        wojew_dict = {}

        for dep in self.data:
            urz_counter = 1
            if dep['typ_JST'] == 'GM':
                if dep['Województwo'] not in wojew_dict:
                    wojew_dict[dep['Województwo']] = wojew_dict.get(dep['Województwo'], urz_counter)
                else:
                    wojew_dict[dep['Województwo']] = wojew_dict.get(dep['Województwo'], urz_counter) + 1

        for k, v in wojew_dict.items():
            print("Województwo " + k + ": " + str(v) + " urzędów.")