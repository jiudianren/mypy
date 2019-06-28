# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/6/28 8:59
import scapy.all as scapy
packets = scapy.rdpcap("F://myworkgit//PyPcap//lpf//3/t.pcap")  # 读取pcap文件
print(len(packets))

print("1========================")
print(packets[0].show())
print("2========================1")
print(packets[0]['Raw'].show())
print("3======================== Ethernet")
print(packets[0].dst)
print("4======================== IP")
print(packets[0].payload.src)
print("5======================== UDP")
print(packets[0].payload.payload.sport)
print("6======================== raw")
print(  packets[0].payload.payload.payload  )
print(len(packets[0].payload.payload.payload))
print("6======================== raw")
print(len(packets[0].payload.payload.payload))
scapy.hexdump(packets[0].payload.payload.payload)
rawHex=packets[0].payload.payload.payload.load
print('{:02x}'.format(rawHex[0]))
print('{:02x}'.format(rawHex[1]))
#help(scapy.hexdump)
