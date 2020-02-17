# _*_ coding: utf-8 _*_
# author jiudianren
# time:2020/02/17 16:42
import configparser

def get_config(file_name, section, option, default = 0):
        config = configparser.ConfigParser()
        config.read(file_name)
        if config.has_option(section, option):
            re = config[section][option]
        else:
            re = default
        return re


def get_config_int(file_name, section, option, default=0):
    config = configparser.ConfigParser()
    config.read(file_name)
    if config.has_option(section, option):
        try:
            re = config.getint(section,option)
        except ValueError:
            re = default
    else:
        re = default
    return re

if __name__ == '__main__':
    file = "test.ini"
    if 0:
        re  =  get_config(file, "section", "int_option")
        print(re)
        re   = get_config(file, "section", "not_exist",111)
        print(re)
    re   = get_config_int(file, "section", "str_option", 111)
    print(re)
