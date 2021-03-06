
def _is_prime(number):
    if number > 1:
        for i in range(2,number):
            if (number % i) == 0:
                return False
            else:
                return True
        else:
            return True


def list_of_prime_numbers(max_number):
    number = 1
    prime=[]
    for number in range(1, max_number):
        if number <= max_number:
            number += 1
            if _is_prime(number) == True:
                prime.append(number)
            else:
                pass
    return prime

# =================== #
# ====== Tests ====== #
# =================== #

# Test: `is_prime`


def test_big_number_prime_true():
    assert _is_prime(19) is True


def test_big_number_prime_false():
    assert _is_prime(20) is False


def test_two_prime():
    assert _is_prime(2) is True


def test_three_prime():
    assert _is_prime(3) is True


def test_four_prime():
    assert _is_prime(4) is False


# Test: `list_of_prime_numbers`

def test_big_number_list():
    assert list_of_prime_numbers(19) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_list_one():
    assert list_of_prime_numbers(2) == [2]


def test_list_zero():
    assert list_of_prime_numbers(0) == []
