# coding: utf-8


def singleton(cls):
    instance = cls()
    instance.__call__ = lambda: instance
    return instance


@singleton
class area_util:
    """
    refer to GB/T 2260-2014
    """

    def __init__(self):
        gb2260_file = 'gb2260_201410.txt'
        fp = open(gb2260_file, 'r')
        area_records = fp.readlines()

        self.area_dict = {}
        for area in area_records:
            source, revision, area_code, area_name = area.split()
            if area_code.isdigit():
                self.area_dict[area_code] = area_name

    def get_area_name(self, area_code):
        province_code = area_code[0, 2] + '0000'
        city_code = area_code[0, 4] + '00'
        county_code = area_code

        return map(lambda code: self.area_dict[code], (province_code, city_code, county_code))

    def get_area_code(self, area_name):
        for code, name in self.area_dict.iteritems():
            if area_name == name:
                return code

    def is_area_code(self, area_code):
        return True if area_code in self.area_dict.keys() else False
