# coding=gbk
import zmq
c=zmq.Context()
s=c.socket(zmq.REQ)

s.connect('tcp://127.0.0.1:1001')

s.send_pyobj('hello')
msg=s.recv_pyobj()
print ("%s " % msg)
