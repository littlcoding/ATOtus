from abc import abstractmethod


class Reader:
    file_path: None

    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def read(self):
        pass
