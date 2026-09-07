import argparse
import sys

from src.CalcAcademicDebt import CalcAcademicDebt
from src.JsonDataReader import JsonDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = JsonDataReader()
    students = reader.read(path)

    academic_debt_count = CalcAcademicDebt(students).calc()

    print("Students: ", students)
    print("Students with academic debts: ", academic_debt_count)


if __name__ == "__main__":
    main()