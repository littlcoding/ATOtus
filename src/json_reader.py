import json
from src.reader import Reader


class JsonReader(Reader):

    def read(self):
        with open(self.file_path, "r") as f:
            users = json.load(f)
            return users
