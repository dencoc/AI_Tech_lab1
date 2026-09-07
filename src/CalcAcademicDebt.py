from src.Types import DataType


class CalcAcademicDebt:
    def __init__(self, data: DataType) -> None:
        self.data = data

    def calc(self) -> int:
        count = 0

        for subjects in self.data.values():
            for _, score in subjects:
                if score < 61:
                    count += 1
                    break

        return count