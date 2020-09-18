import yaml

with open('parameters.yaml') as f:
    dataMap = yaml.safe_load(f)


class Command:
    def __init__(self, args):
        self.__dict__.update(args)


s = Command(dataMap)
print(s.resource)
print(s.action)
print(s.parameters)
print(s.nested)
print(s.users)
