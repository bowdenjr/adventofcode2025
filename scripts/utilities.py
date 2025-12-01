from typing import List, Union


def open_advent_calendar(path) -> List[str]:
    with open(path, "r") as f:
        return f.read().split("\n")
