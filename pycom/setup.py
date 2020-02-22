# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/11/5 16:02


from setuptools import  setup ,find_packages


setup(

    name = "jdrpycom",
    version = '19.11.05',
    long_description ="""
    jiudianren's public tool for myself 
    """,
    install_requires =['requests','pyopenssl'],
    packages = find_packages()
)
