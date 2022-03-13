# -*- coding: utf-8 -*-
"""
json to yaml converter
"""
import json
import sys

import yaml

from DeserializeJson import DeserializeJson


class ConvertJsonToYaml:
    @staticmethod
    def run(deserializeddata, destinationfilelocation):
        print("let's convert something")
        with open(destinationfilelocation, 'w', encoding='utf8') as f:
            yaml.dump(deserializeddata, f, allow_unicode=True)
        print("it is done")

    @staticmethod
    def run2(jsonlocation, yamllocation):
        print("json to yaml")
        new_deserializator = DeserializeJson(jsonlocation)
        with open(yamllocation, 'w', encoding='utf8') as f:
            yaml.dump(new_deserializator, f, allow_unicode=True)
        print("json -> yaml done")

