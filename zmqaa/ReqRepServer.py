# coding=gbk
'''
Created on 2018年2月28日

@author: Administrator
'''
import zmq

c=zmq.Context()
s=c.socket(zmq.REP)

s.bind('tcp://127.0.0.1:1001')

while True:
    msg=s.recv_pyobj()
    s.send_pyobj(msg)

s.close()
