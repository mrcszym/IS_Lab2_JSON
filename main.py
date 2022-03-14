from SerializeJson import SerializeJson
from DeserializeJson import DeserializeJson
from ConvertJsonToYaml import ConvertJsonToYaml
import yaml

new_deserializator = DeserializeJson('Assets/data.json')
new_deserializator.somestats()

SerializeJson.run(new_deserializator, 'Assets/data_mod.json')

ConvertJsonToYaml.run(new_deserializator, 'Assets/data_mod_run.yaml')
ConvertJsonToYaml.run2('Assets/data.json', 'Assets/data_mod_run2.yaml')

tempconffile = open('Data/basic_config.yaml', encoding="utf8")
confdata = yaml.load(tempconffile, Loader=yaml.FullLoader)

newDeserializator = DeserializeJson(confdata['paths']['source_folder'] + confdata['paths']['json_source_file'])


def serialize_yaml(confdata, data):
    if confdata['yaml_serialize_from'] == "file":
        ConvertJsonToYaml.run(confdata['paths']['source_folder'] + confdata['paths']['json_source_file'],
                              confdata['paths']['source_folder'] + confdata['paths']['yaml_destination_file'])
    elif confdata['yaml_serialize_from'] == "object":
        ConvertJsonToYaml.run(data, confdata['paths']['source_folder'] + confdata['paths']['yaml_destination_file'])


def serialize_json(confdata, data):
    if confdata['serialize_only_selected']:
        SerializeJson.run(data,
                          confdata['paths']['source_folder'] + confdata['paths']['json_destination_file'])
    else:
        SerializeJson.run(data,
                          confdata['paths']['source_folder'] + confdata['paths']['json_destination_file'])


if confdata['first_convert_to'] == 'yaml':
    serialize_yaml(confdata, newDeserializator)
    serialize_json(confdata, newDeserializator)

elif confdata['first_convert_to'] == 'json':
    serialize_json(confdata, newDeserializator)
    serialize_yaml(confdata, newDeserializator)

operations = confdata['additional_operations'].split(',')

if operations != [""]:
    for operation in operations:
        func = getattr(newDeserializator, operation)
        func()
