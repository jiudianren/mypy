
# _*_ coding: utf-8 _*_
# author jiudianren
import  binhex
str = "&#24615;&#33021;&#20998;&#26512;&#24037;&#20855;&#22270;&#35889;.png"
ai=str.encode("GBK").decode("utf-8")

str2="&#26032;&#24314;&#25991;&#26412;&#25991;&#26723; (2).txt"

def tran_code(str):
    if len(str.split(".")) != 2:
        logger.debug("2222")
        return str
    if str.split(".")[0].find('&#') == -1:
        logger.debug("333")
        return str
    text = str.split(".")[0].replace('&#', '')
    text = [i for i in text.split(';') if i]
    text = [hex(int(i)) for i in text]
    text = [i.replace('0x', '') for i in text]
    string = ' '
    flag = '\\u'
    for i in text:
        string += flag + format(i, '0>4s')
    aimstr = string.encode('utf-8').decode('unicode-escape')
    aimstr =  aimstr +"."+ str.split(".")[1]
    logger.debug( aimstr)
    return aimstr


print(str.split("."))
text=str.split(".")[0].replace('&#','')
text=[i for i in text.split(';') if i]
text=[hex(int(i)) for i in text]
text=[i.replace('0x','') for i in text]
string=' '
flag='\\u'
for i in text:
                string+=flag+format(i,'0>4s')
print(string.encode('utf-8').decode('unicode-escape'))
print(str)
print(ai)