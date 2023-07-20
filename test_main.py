import pytest
import calculator


## Testing addition function

@pytest.mark.parametrize("num1,num2,result",[(3, 2, 5)])

def test_addition_two_positives(num1,num2,result):
    assert calculator.add(num1,num2) == result

@pytest.mark.parametrize("num1,num2,result",[(3, -2, 1)])

def test_addition_one_positive_one_negative(num1,num2,result):
    assert calculator.add(num1,num2) == result

@pytest.mark.parametrize("num1,num2,result",[(-3, 2, -1)])

def test_addition_one_negative_one_positive(num1,num2,result):
    assert calculator.add(num1,num2) == result

@pytest.mark.parametrize("num1,num2,result",[(-3, -2, -5)])

def test_addition_two_negatives(num1,num2,result):
    assert calculator.add(num1,num2) == result




## Testing subtraction function

@pytest.mark.parametrize("num1,num2,result",[(1, 8, -7)])

def test_subtraction_two_positives_second_larger(num1,num2,result):
    assert calculator.subtract(num1,num2) == result

@pytest.mark.parametrize("num1,num2,result",[(8, 1, 7)])

def test_subtraction_two_positives_first_larger(num1,num2,result):
    assert calculator.subtract(num1,num2) == result

@pytest.mark.parametrize("num1,num2,result",[(1, -8, 9)])

def test_subtraction_one_positive_one_negative(num1,num2,result):
    assert calculator.subtract(num1,num2) == result

@pytest.mark.parametrize("num1,num2,result",[(-1, 8, -9)])

def test_subtraction_one_negative_one_positive(num1,num2,result):
    assert calculator.subtract(num1,num2) == result

@pytest.mark.parametrize("num1,num2,result",[(-1, -8, 7)])

def test_subtraction_two_negatives(num1,num2,result):
    assert calculator.subtract(num1,num2) == result




## Testing multiplication function

@pytest.mark.parametrize("num1,num2,result",[(2, 8, 16)])

def test_multiplication_two_positives(num1,num2,result):
    assert calculator.multiply(num1,num2) == result

@pytest.mark.parametrize("num1,num2,result",[(2, -8, -16)])

def test_multiplication_one_positive_one_negative(num1,num2,result):
    assert calculator.multiply(num1,num2) == result

@pytest.mark.parametrize("num1,num2,result",[(-2, 8, -16)])

def test_multiplication_one_negative_one_positive(num1,num2,result):
    assert calculator.multiply(num1,num2) == result

@pytest.mark.parametrize("num1,num2,result",[(-2, -8, 16)])

def test_multiplication_two_negatives(num1,num2,result):
    assert calculator.multiply(num1,num2) == result

@pytest.mark.parametrize("num1,num2,result",[(0, -8, 0)])

def test_multiplication_one_zero(num1,num2,result):
    assert calculator.multiply(num1,num2) == result



## Testing division function

@pytest.mark.parametrize("num1,num2,result",[(8, 2, 4)])

def test_division_two_positives_first_larger(num1,num2,result):
    assert calculator.divide(num1,num2) == result


@pytest.mark.parametrize("num1,num2,result",[(2, 8, 0.25)])

def test_division_two_positives_second_larger(num1,num2,result):
    assert calculator.divide(num1,num2) == result


@pytest.mark.parametrize("num1,num2,result",[(2, -8, -0.25)])

def test_division_one_positive_one_negative(num1,num2,result):
    assert calculator.divide(num1,num2) == result


@pytest.mark.parametrize("num1,num2,result",[(-2, 8, -0.25)])

def test_division_one_positive_one_negative(num1,num2,result):
    assert calculator.divide(num1,num2) == result


@pytest.mark.parametrize("num1,num2,result",[(-8, -2, 4)])

def test_division_two_negatives(num1,num2,result):
    assert calculator.divide(num1,num2) == result


@pytest.mark.parametrize("num1,num2,result",[(0, -2, 0)])

def test_division_numerator_zero(num1,num2,result):
    assert calculator.divide(num1,num2) == result


    












