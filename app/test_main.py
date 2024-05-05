import pytest
from app.main import get_coin_combination


def test_get_coin_combination() -> None:
    # Test cases
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(50) == [0, 0, 0, 2]

    # Additional tests
    assert get_coin_combination(0) == [0, 0, 0, 0]
    assert get_coin_combination(4) == [4, 0, 0, 0]
    assert get_coin_combination(7) == [2, 1, 0, 0]
    assert get_coin_combination(39) == [4, 0, 1, 1]

    # Test with large input
    assert get_coin_combination(999) == [4, 0, 2, 39]

    # Test with negative input
    with pytest.raises(ValueError):
        get_coin_combination(-1)

    # Test with non-integer input
    with pytest.raises(TypeError):
        get_coin_combination(3.5)

    # Test with string input
    with pytest.raises(TypeError):
        get_coin_combination("abc")
