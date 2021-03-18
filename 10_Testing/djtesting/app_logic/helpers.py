import numbers


def check_access_by_age(age):
    if age < 18:
        return False
    return True


def string_concatenation(first_str, second_str):
    if isinstance(first_str, str) and isinstance(second_str, str):
        return first_str + second_str
    else:
        return False


def division(first_num, second_num):
    if isinstance(first_num, numbers.Number) and not isinstance(first_num, bool) and first_num != 0\
            and isinstance(second_num, numbers.Number) and not isinstance(second_num, bool) and second_num != 0:
        return first_num / second_num
    else:
        return False


def work_time_check(hour):
    if isinstance(hour, int) and not isinstance(hour, bool) and 0 <= hour <= 24:
        if 8 <= hour < 20 and hour != 13:
            return 'Work'
        else:
            return 'Closed'
    else:
        return False


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
division(10, 2.55)
