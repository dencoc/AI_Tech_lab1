from src.Types import DataType
from src.DataReader import DataReader

import json


class JsonDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding="utf-8") as file:
            data = json.load(file)

        for student, subjects in data.items():
            self.students[student] = []

            for subject, score in subjects.items():
                self.students[student].append(
                    (subject, int(score))
                )

        return self.students
