from SerializeJson import SerializeJson
from DeserializeJson import DeserializeJson
from ConvertJsonToYaml import ConvertJsonToYaml

new_deserializator = DeserializeJson('Assets/data.json')
new_deserializator.somestats()

SerializeJson.run(new_deserializator, 'Assets/data_mod.json')

ConvertJsonToYaml.run(new_deserializator, 'Assets/data_mod_run.yaml')
ConvertJsonToYaml.run2('Assets/data.json', 'Assets/data_mod_run2.yaml')
