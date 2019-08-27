# coding=gbk
'''
Created on 2018年2月28日

@author: Administrator
'''
import zmq
from random import randrange

context = zmq.Context()
socket = context.socket(zmq.PUB)  #publisher类型
socket.bind("tcp://*:5556")

while True:
    zipcode = randrange(1, 100000)
    temperature = randrange(-80, 135)
    relhumidity = randrange(10, 60)

    socket.send_string("%i %i %i" % (zipcode, temperature, relhumidity))
