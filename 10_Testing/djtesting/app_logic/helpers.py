def check_access_by_age(age):
    if age < 18:
        return False
    return True


def test_if_age_less_than_18():
    for i in range(17):
        result = check_access_by_age(i)
        if result:
            print(f'result is wrong, age is {i}')


def test_if_age_equal_18():
    result = check_access_by_age(18)
    if not result:
        print(f'result is wrong, age is 18')


def test_if_age_greater_than_18():
    for i in range(18, 120):
        result = check_access_by_age(i)
        if not result:
            print(f'result is wrong, age is {i}')


test_if_age_less_than_18()
test_if_age_equal_18()
test_if_age_greater_than_18()