from typing import List

import pytest

from src.some import sum_of_two_numbers_list


@pytest.mark.parametrize("input_list, expected_output", 
                         [
                             ([1, 2, 3], 6),
                             ([1, 2, 3, 4, 5], 15),
                             ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 55)
                         ])


def test_sum_of_two_numbers_list(input_list: List[float], expected_output: float):
    """
    Test the sum_of_two_numbers_list function.
    """
    assert sum_of_two_numbers_list(input_list) == expected_output
