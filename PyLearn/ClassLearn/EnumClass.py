# coding=gbk

#����ö����

from enum import Enum, unique

# װ����
@unique
class Weekday(Enum):
    Sun = 0 # Sun��value���趨Ϊ0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6