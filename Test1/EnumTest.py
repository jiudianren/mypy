# coding=gdk
# ��β鿴 python 2.7 �Ƿ�֧�� enum 
from enum import Enum,unique


@unique
class Weekday(Enum):
    Sun = 0 # Sun��value���趨Ϊ0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    
day1 = Weekday.Mon
print(day1)