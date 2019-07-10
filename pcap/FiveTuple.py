# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/6/29 13:49


class FiveTuple(object):

    def __init__(self, ser_ip="", ser_port=0, usr_ip="", usr_port=0, net_type=0):
        self._ser_ip = ser_ip
        self._ser_port = ser_port
        self._usr_ip = usr_ip
        self._usr_port = usr_port
        self._net_type = net_type

    def __hash__(self):
        return hash(self._ser_ip + self._usr_ip) + hash(self._usr_port + self._net_type + self._ser_port)

    def __eq__(self, other):
        if (self._ser_ip == other.ser_ip) \
                and (self._ser_port == other.ser_port) \
                and (self._usr_ip == other.usr_ip) \
                and (self._usr_port == other.usr_port) \
                and (self._net_type == other.net_type):
            return True
        return False

    def __str__(self):
        return "[SerIp:{0}_{1},UseIp:{2} {3},net_type:{4}]".format(self.ser_ip, self.ser_port, self.usr_ip, self.usr_port,
                                                                      self.net_type)

    @property
    def ser_ip(self):
        return self._ser_ip

    @ser_ip.setter
    def ser_ip(self, ser_ip):
        self._ser_ip = ser_ip

    @property
    def ser_port(self):
        return self._ser_port

    @ser_port.setter
    def ser_port(self, ser_port):
        self._ser_port = ser_port

    @property
    def usr_port(self):
        return self._usr_port

    @usr_port.setter
    def usr_port(self, usr_port):
        self._usr_port = usr_port

    @property
    def net_type(self):
        return self._net_type

    @net_type.setter
    def net_type(self, net_type):
        self._net_type = net_type


    @property
    def usr_ip(self):
        return self._usr_ip

    @usr_ip.setter
    def usr_ip(self, usr_ip):
        self._usr_ip = usr_ip

if __name__ == '__main__':
    fTup1 = FiveTuple("10.10.10.10", 80, "11.11.11.121", 8080, 6)
    fTup2 = FiveTuple("10.10.10.11", 80, "121.121.121.121", 8080, 9)
    print(fTup1)
    print(fTup2)
    myDic ={}
    print( len(myDic))
    myDic[fTup1] = 1
    print(len(myDic))
