import json


class JsonWriter:

    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)
            pass
