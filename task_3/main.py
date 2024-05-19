"""Module for Task 3."""

import sys
import re
from datetime import datetime
from collections import Counter
from typing import Generator
from pathlib import Path

log_pattern = re.compile(r'^([\d:\-\s]+) (DEBUG|INFO|WARNING|ERROR) (.+)\n$')


def read_log_file(log_file_path: str) -> Generator[str, None, None]:
    file_path = Path(log_file_path)
    if not file_path.exists() or not file_path.is_file():
        raise ValueError("Файл не знайдено.")

    with open(file_path, "r", encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            yield line


def parse_log_entry(log_entry: str) -> dict:
    match = re.match(log_pattern, log_entry)
    if match:
        log_date = datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S')
        log_level = match.group(2)
        log_message = match.group(3)
        return {
            'date': log_date,
            'log_level': log_level.upper(),
            'message': log_message,
        }
    else:
        raise ValueError("Неочікуваний формат логу.")


def load_log_entries(log_file_path: str) -> list:
    log_entries = []
    for entry in read_log_file(log_file_path):
        parsed_entry = parse_log_entry(entry)
        log_entries.append(parsed_entry)
    return log_entries


def filter_log_entries_by_level(log_entries: list, log_level: str) -> list:
    return [entry for entry in log_entries if entry["log_level"] == log_level.upper()]


def count_log_entries_by_level(log_entries: list) -> dict:
    log_counts = Counter(entry["log_level"] for entry in log_entries)
    return dict(log_counts)


def display_log_counts(log_counts: dict):
    print("Рівень логування | Кількість")
    print("---------------- | ---------")
    for level, count in log_counts.items():
        print(f"{level:<16} | {count}")


def main():
    if len(sys.argv) not in (2, 3):
        print("Використання:")
        print(f"{'python main.py <log_file_path>':<60} - виведе загальну статистику за рівнями логування")
        print(
            f"{'python main.py <log_file_path> <debug|info|warning|error>':<60} - виведе загальну статистику за рівнями, а також детальну інформацію для вибраного рівня")
        sys.exit(1)

    log_file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) == 3 else None

    try:
        log_entries = load_log_entries(log_file_path)
        log_counts = count_log_entries_by_level(log_entries)
        display_log_counts(log_counts)

        if log_level:
            log_level = log_level.upper()
            if log_level not in ("DEBUG", "INFO", "WARNING", "ERROR"):
                raise ValueError("Невірний рівень логування. Виберіть один із: debug, info, warning, error")

            print(f"\nДеталі логів для рівня '{log_level}':")
            for entry in filter_log_entries_by_level(log_entries, log_level):
                print(f"{entry['date'].strftime('%Y-%m-%d %H:%M:%S')} - {entry['message']}")

    except ValueError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
