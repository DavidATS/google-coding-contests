import os

import click
from solution import solution

BASE_FOLDER_PATH = "problem_files/"


@click.command()
@click.option("--data_set_file", required=True, type=str)
def process_file(data_set_file):
    file_name = ""

    with os.scandir(BASE_FOLDER_PATH) as files:
        for file in files:
            if file.name[0] == data_set_file[0]:
                file_name = file.name
                break

    solution(BASE_FOLDER_PATH + file_name, data_set_file)


if __name__ == "__main__":
    process_file()
