# tests_demo/test_utils.py
import pytest
from utils import get_even_numbers

class TestGetEvenNumbers:
    """Тестирование функции фильтрации чётных чисел."""

    def test_mixed_numbers(self):
        """Тест со смешанным списком."""
        data = [1, 2, 3, 4, 5, 6]
        expected = [2, 4, 6]
        assert get_even_numbers(data) == expected

    def test_empty_list(self):
        """Тест с пустым списком (граничный случай)."""
        assert get_even_numbers([]) == []

    def test_no_even_numbers(self):
        """Тест, когда чётных чисел нет."""
        data = [1, 3, 5]
        assert get_even_numbers(data) == []

    def test_negative_and_zero(self):
        """Тест с отрицательными числами и нулём (0 — чётное)."""
        data = [-3, -2, -1, 0, 1, 2]
        expected = [-2, 0, 2]
        assert get_even_numbers(data) == expected

    def test_all_even(self):
        """Тест, когда все числа чётные."""
        data = [2, 4, 8, 10]
        assert get_even_numbers(data) == data 
