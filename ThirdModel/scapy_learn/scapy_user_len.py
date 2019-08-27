# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/8/21 10:39

import scapy.all as scapy
def ip_v6():
    try:
        file_name = "./IPv6-DNS.pcap"
        pkts = scapy.rdpcap(file_name)
        pkts_cn = len(pkts)
        if pkts_cn <= 0:
            print("No packet in this file ,please check your file !!")
        else:
            print("Total Packet Cnt:{0}".format(pkts_cn))
        for pkt in pkts:
            # print(pkt.show())
            # print(pkt.payload.payload.show)
            # print(pkt.payload.payload.payload[])
            if pkt and pkt.haslayer('UDP') and pkt.haslayer('DNS'):
                dns = pkt['DNS']
                print(dns.qd.qname)
                # print(dns.show)

        print("=====")
    except Exception as e:

        print("Erro Reasion: ", e)
        print("Pass this file {0}".format(file_name))