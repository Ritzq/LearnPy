import queue
import sys
import threading

sys.path.append('/')

from scapy.all import conf

# raw_socket = conf.L2socket(iface=str('enp1s0'), filter='ether host e4:54:e8:c8:8d:e9')
# raw_socket = conf.L2socket(iface=str('enp1s0'), filter='not ip')

raw_socket = conf.L2socket(iface=str('ASIX AX88179A USB 3.2 Gen1 to Gigabit Ethernet Adapter #3'))

# raw_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x9700))
# VlanDevice.raw_socket.settimeout(1)
# raw_socket.bind(('enp1s0', 0))

# global a
# a = 1
#
#
# def input_s():
#     global a
#     a = input()
#
#
# t = threading.Thread(target=input_s, )
# t.start()
# list_ = list()
flag = 1
data_queue = queue.Queue()


def recv_():
    while flag:
        try:
            packet = raw_socket.recv((2 ** 16 - 1))
        except:
            packet = None
        if packet is None:
            continue
        # data_queue.put(packet)
        data_queue.put(packet)

        # try:
        #     pmessage = PMessage.from_bytes(bytes(packet))
        # except:
        #     print('error')
        #     pmessage = None
        #     continue
        # if pmessage is None:
        #     # print('none')
        #     continue
        # # print(pmessage.protocol)
        # if pmessage.protocol == 0x9700:
        #     # print(pmessage.payload, type(pmessage.payload))
        #     data_queue.put(packet)


t_recv = threading.Thread(target=recv_)
t_recv.start()

filename = 1
filename = 'D:/PycharmProjects/LearnPy/' + str(filename) + 'tar.gz'
f = open(filename, "wb")
received_size = 0
file_size = 10240000
# print(1)

while received_size < file_size:
    if not data_queue.empty():
        print(1)
        data = data_queue.get()
        data_len = len(data)
        received_size += data_len
        print("已接收：", int(received_size / file_size * 100), "%")
        f.write(bytes(data))
        # print(data.payload, type(data.payload))
    else:
        continue
f.close()
flag = 0
