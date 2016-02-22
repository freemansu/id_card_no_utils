#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Su Yu
@contact: yusu.work@gmail.com
@site: http://www.freemansu.com
@file: id_card_no_info.py
@time: 2016/2/21 20:31
"""

import datetime
import area_util


def get_residence_address(id_card_no):
    """
    get the residence address
    :param id_card_no:
    :return: province, city, county string; if one of (province, city, county) is None, return None
    """
    area_code_len, area_code_start = 2, 0
    area_code = id_card_no[area_code_start: area_code_start + area_code_len]
    province, city, county = area_util.area_util().get_area_name(area_code)
    return '{province}{city}{county}'.format(province=province, city=city, county=county)


def get_birth_date(id_card_no):
    """
    get the birth date
    :param id_card_no:
    :return:
    """
    birth_date_code_len, birth_date_code_start = 8, 6
    birth_date_code = id_card_no[birth_date_code_start: birth_date_code_start + birth_date_code_len]
    try:
        birth_date = datetime.datetime.strptime(birth_date_code, '%Y%m%d')
        return birth_date
    except ValueError:
        return None


def get_gender(id_card_no):
    """
    get the gender
    :param id_card_no:
    :return:
    """
    sequence_code_len, sequence_code_start = 3, 14
    sequence_code = id_card_no[sequence_code_start, sequence_code_start + sequence_code_len]
    return u'女' if int(sequence_code) % 2 == 0 else u'男'