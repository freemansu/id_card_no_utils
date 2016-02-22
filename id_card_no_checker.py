# coding: utf-8

import re
import datetime
import math
import area_util


def check_id_card_no(id_card_no):
    """
    refer to GB 11643-1999
    :param id_card_no:
    :return:
    """
    return check_format(id_card_no) \
        and check_area_code(id_card_no) \
        and check_birth_date(id_card_no) \
        and check_parity_bit(id_card_no)


def check_format(id_card_no):
    """
    check the format of id card number
    :param id_card_no:
    :return:
    """
    pattern = '^[0-9]{17}[0-9xX]$'
    re.compile(pattern)

    if re.match(pattern, id_card_no) is not None:
        return True

    return False


def check_area_code(id_card_no):
    """
    check if area_code of id card number is legal
    :param id_card_no:
    :return:
    """
    area_code_len, area_code_start = 6, 0
    area_code = id_card_no[area_code_start: area_code_start + area_code_len]
    util = area_util.area_util()
    return util.is_area_code(area_code)


def check_birth_date(id_card_no):
    """
    check if birth date of id card number is legal
    :param id_card_no:
    :return:
    """
    birth_date_code_len, birth_date_code_start = 8, 6
    birth_date_code = id_card_no[birth_date_code_start: birth_date_code_start + birth_date_code_len]
    try:
        birth_date = datetime.datetime.strptime(birth_date_code, '%Y%m%d')
        current_date = datetime.datetime.today()
        return True if birth_date <= current_date else False
    except ValueError:
        return False


def check_parity_bit(id_card_no):
    """
    check the parity bit
    refer to ISO 7064:1983
    :param id_card_no:
    :return:
    """
    master_number_str = id_card_no[0:17]
    check_number_str = id_card_no[17]

    master_numbers = [int(master_number_str[i]) for i in range(0, len(master_number_str))]
    check_number = 10 if check_number_str == 'X' or check_number_str == 'x' else int(check_number_str)

    weights = map(lambda x: int(math.pow(2, x) % 11), range(17, -1, -1))
    numbers = master_numbers
    numbers.append(check_number)

    check_sum = sum(map(lambda x, y: x * y, numbers, weights)) % 11
    return True if check_sum == 1 else False


if __name__ == '__main__':
    print check_id_card_no('53010219200508011x')
