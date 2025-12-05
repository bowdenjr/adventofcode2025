from typing import List, Union


def open_advent_calendar(path) -> List[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


def abs_differences_between_two_lists(
    left_list: List[int], right_list: List[int], sort: bool
) -> List[int]:

    if len(left_list) != len(right_list):
        raise IndexError("Lists are of different lengths")

    if sort:
        left_list = sorted(left_list)
        right_list = sorted(right_list)
        return [abs(right_list[num] - left_list[num])
                for num in range(len(left_list))]
    else:
        return [abs(right_list[num] - left_list[num])
                for num in range(len(left_list))]


def multiply_left_by_count_in_right(left_list: List[int],
                                    right_list: List[int]):
    return [num * right_list.count(num) for num in left_list]


def all_increasing(report: List[int]) -> bool:

    for i in range(len(report) - 1):
        if report[i + 1] <= report[i]:
            return False

    return True


def all_decreasing(report: List[int]) -> bool:

    for i in range(len(report) - 1):
        if report[i + 1] >= report[i]:
            return False

    return True


def max_change(report: List[int]) -> int:

    diffs = [abs(j - i) for i, j in zip(report[:-1], report[1:])]
    return max(diffs)


def dampen_report(report: List[int]) -> List[List[int]]:

    dampened_reports = []

    for i, element in enumerate(report):
        report_copy = report.copy()
        report_copy.pop(i)
        dampened_reports.append(report_copy)

    return dampened_reports


def report_is_safe(report: List[int]) -> bool:

    if all_increasing(report):
        if max_change(report) <= 3:
            return True

    elif all_decreasing(report):
        if max_change(report) <= 3:
            return True

    return False
