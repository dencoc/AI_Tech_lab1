from src.Types import DataType
from src.CalcAcademicDebt import CalcAcademicDebt
import pytest


class TestCalcAcademicDebt:
    @pytest.fixture()
    def input_data(self) -> tuple[DataType, int]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
            [
                ("математика", 80),
                ("русский язык", 76),
                ("программирование", 100)
            ],
            "Петров Игорь Владимирович":
            [
                ("математика", 61),
                ("русский язык", 80),
                ("программирование", 78),
                ("литература", 97)
            ],
            "Сидоров Иван Петрович":
            [
                ("математика", 55),
                ("русский язык", 90),
                ("программирование", 70)
            ]
        }

        academic_debt_count = 1

        return data, academic_debt_count

    def test_init_calc_academic_debt(
        self,
        input_data: tuple[DataType, int]
    ) -> None:
        calc_academic_debt = CalcAcademicDebt(input_data[0])

        assert input_data[0] == calc_academic_debt.data

    def test_calc(
        self,
        input_data: tuple[DataType, int]
    ) -> None:
        academic_debt_count = CalcAcademicDebt(input_data[0]).calc()

        assert academic_debt_count == input_data[1]

    def test_score_61_is_not_academic_debt(self) -> None:
        data: DataType = {
            "Иванов Иван Иванович": [
                ("математика", 61),
                ("физика", 70)
            ]
        }

        academic_debt_count = CalcAcademicDebt(data).calc()

        assert academic_debt_count == 0

    def test_several_debts_of_one_student(self) -> None:
        data: DataType = {
            "Иванов Иван Иванович": [
                ("математика", 50),
                ("физика", 40),
                ("химия", 90)
            ]
        }

        academic_debt_count = CalcAcademicDebt(data).calc()

        assert academic_debt_count == 1
