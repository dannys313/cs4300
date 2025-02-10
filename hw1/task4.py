import pytest

#values for pytest to test
@pytest.mark.parametrize("input_val, discount, expected_output", [
    (1000, 0.20, 800),
    (16, 0.25, 12),
    (2500, 0.01, 2475),
    (352.6, 0.3, 246.82)
    ])

#function for pytest
def test_discount(input_val, discount, expected_output):
    offset = input_val * discount
    final_cost = round((input_val - offset), 2)
    assert final_cost == expected_output

#function if it were used by people
def calculate_discount(input_val, discount, expected_output):
    offset = input_val * discount
    final_cost = input_val - offset
    return final_cost