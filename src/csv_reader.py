from src.reader import Reader
from csv import DictReader


class CSVReader(Reader):

    def read(self):
        with open(self.file_path) as f:
            reader = DictReader(f)
            books = []
            for row in reader:
                books.append(row)
            return books
