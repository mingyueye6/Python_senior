# conding: utf-8

class Date:
    # 构造函数
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return '{year}/{month}/{day}'.format(year=self.year, month=self.month, day=self.day)

    def tomorrow(self):
        self.day += 1

    # 静态方法
    @staticmethod
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split('-'))
        return Date(int(year), int(month), int(day))

    # 类方法
    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split('-'))
        return Date(int(year), int(month), int(day))


if __name__ == '__main__':
    new_day = Date(2019, 10, 23)
    new_day.tomorrow()
    print(new_day)

    new_day = Date.parse_from_string('2019-10-23')
    print(new_day)

    new_day = Date.from_string('2019-10-23')
    print(new_day)