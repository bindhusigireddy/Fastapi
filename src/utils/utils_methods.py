import json

class Utils:

    @staticmethod
    def read_config_file(config_path):
        with open(config_path, 'r') as file:
            config = json.load(file)
        return config
    