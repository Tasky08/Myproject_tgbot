import unittest

import pytest
from functions import check_num, input_balance, add_categories_budget


# Ваш файл test_functions.py

def test_check_num_numeric_input():
    assert check_num("12345") == 0


def test_check_num_negative_input():
    assert check_num("-12345") == 0


def test_check_num_non_numeric_input():
    assert check_num("abc") == 1


def test_input_balance():
    global balance
    balance = 0
    input_balance(100)
    assert balance == 100  # Проверяем правильность добавления баланса


def test_input_balance_invalid_input():
    global balance
    balance = 0
    result = input_balance("abc")
    assert balance == 0
    assert result == "wrong input"


def test_add_categories_budget_valid_input():
    global categories
    global balance
    categories = [0, 0, 0, 0, 0]
    balance = 100
    result = add_categories_budget("1 200", 0)
    assert result == "no money"
    assert categories == [0, 0, 0, 0, 0]
    assert balance == 100


if __name__ == '__main__':
    unittest.main()
