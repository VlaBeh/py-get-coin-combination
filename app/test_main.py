import pytest
from app.main import get_coin_combination


def test_get_coin_combination() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_get_coin_combination_edge_cases() -> None:
    # Test with zero cents
    assert get_coin_combination(0) == [0, 0, 0, 0]

    # Test with negative cents
    with pytest.raises(ValueError):
        get_coin_combination(-1)

    # Test with large cents
    assert get_coin_combination(100) == [0, 0, 0, 4]
    assert get_coin_combination(99) == [4, 0, 2, 1]
    assert get_coin_combination(92) == [2, 1, 1, 3]
