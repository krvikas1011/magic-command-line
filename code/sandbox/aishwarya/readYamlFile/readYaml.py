import os
import yaml


class YamlLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_file(self):
        with open(self.file_name) as f:
            data_map = yaml.safe_load(f)

        return data_map


user_input = input("Enter the path of your file: ")
assert os.path.exists(user_input), "I did not find the file at, " + str(user_input)
yaml = YamlLoader(user_input).load_file()
print(yaml)
