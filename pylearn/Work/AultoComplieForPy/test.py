# coding=gbk

import logging
logging.basicConfig(level=logging.DEBUG)

logging.info('n =ss' )
ss='abcd'
s2="xyz"
s3="cd"
timm="2017-12-08 13:24:33"
timm= timm.replace(" ","").replace(":","").replace("-","")
print(timm)

print( ss.find(s3) )
print( ss.find(s2) )
print( len( ss and s3) ) 
print( len( ss and s2) ) 
print(ss[1:3])

print(ss[1:3] == "bc")