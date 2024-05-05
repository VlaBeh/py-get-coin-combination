import pytest
from app.main import get_coin_combination
from typing import List, Tuple

# Test cases
test_cases: List[Tuple[int, List[int]]] = [
    (-5, [0, 0, 2, -1]),
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
    (99, [4, 0, 2, 3]),
    (1348, [3, 0, 2, 53])
]


@pytest.mark.parametrize("cents: int, expected: List[int]", test_cases)
def test_get_coin_combination(cents: int, expected: List[int]) -> None:
    assert get_coin_combination(cents) == expected


def test_return_only_pennies() -> None:
    coins = get_coin_combination(6)
    assert sum(coins[1:]) > 0, "Function returned only pennies"


def test_return_only_one_type() -> None:
    coins = get_coin_combination(6)
    assert sum(coins) != coins[0], "Function returned only one type of coin"
