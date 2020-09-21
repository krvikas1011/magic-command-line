import os
import yaml


class Command:
    def __init__(self, resource, action, parameters):
        self.resource = resource
        self.action = action
        self.parameters = parameters


class FileLoader:
    def __init__(self, file_name):
        self.file_name = file_name

    def load_file(self):
        with open(self.file_name) as f:
            data_map = yaml.safe_load(f)
            command = Command(data_map['resource'], data_map['action'], data_map['parameters'])

        return command


user_input = input("Enter the path of your file: ")
assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
file = FileLoader(user_input)
yaml_object = file.load_file()
print(yaml_object.resource)
print(yaml_object.action)
print(yaml_object.parameters)
