"""
Завдання 1

Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії, 
переміщає їх до нової директорії та сортує в піддиректорії, 
назви яких базуються на розширенні файлів.

"""

import os
import shutil
import argparse


def copy_files(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file_path = os.path.join(root, file)
            destination_subdir = os.path.join(
                destination_dir, os.path.splitext(file)[1][1:]
            )
            destination_file_path = os.path.join(destination_subdir, file)

            if not os.path.exists(destination_subdir):
                os.makedirs(destination_subdir)

            try:
                shutil.copy2(source_file_path, destination_file_path)
            except Exception as e:
                print(f"Помилка копіювання файлу {source_file_path}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Рекурсивно копіює файли з вихідної директорії та сортує їх в піддиректоріях за розширенням"
    )
    parser.add_argument("source_dir", help="Шлях до вихідної директорії")
    parser.add_argument(
        "destination_dir",
        nargs="?",
        default="dist",
        help="Шлях до директорії призначення (за замовчуванням - 'dist')",
    )
    args = parser.parse_args()

    copy_files(args.source_dir, args.destination_dir)
