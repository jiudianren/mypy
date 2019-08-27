# coding=gbk
'''
Created on 2018��2��28��

@author: Administrator
'''
impozmqest
zmqest.Context()
s=c.sockzmqest.REP)

s.bind('tcp://127.0.0.1:1001')

while True:
    msg=s.recv_pyobj()
    s.send_pyobj(msg)

s.close()
