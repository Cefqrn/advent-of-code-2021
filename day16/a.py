import os
from collections import defaultdict
from math import ceil
from functools import reduce

with open(os.path.join(os.path.dirname(__file__), "input")) as f:
    data = 0
    for hexit in f.read().strip():
        data <<= 4
        data += int(hexit, 16)

    data = bin(data)[2:]
    data = data.rjust(ceil(len(data)/4)*4, "0")

p1 = 0
def decode_packet(packet):
    global p1
    i = 0
    version = int(packet[0:(i:=i+3)], 2)
    type_id = int(packet[i:(i:=i+3)], 2)
    print(version, "literal" if type_id == 4 else "operator")
    p1 += version

    if type_id == 4: # literal value
        value = 0
        while True:
            value <<= 4
            value += int(packet[i+1:(i:=i+5)], 2)
            if packet[i - 5] == '0':
                break

    else: # operator packet
        length_type_id = int(packet[i:(i:=i+1)], 2)
        values = []
        if length_type_id:
            sub_packet_count = int(packet[i:(i:=i+11)], 2)
            for x in range(sub_packet_count):
                di, value = decode_packet(packet[i:])
                values.append(value)
                i += di
        else:
            sub_packet_length = int(packet[i:(i:=i+15)], 2)
            start = i
            
            while i - start < sub_packet_length:
                di, value = decode_packet(packet[i:])
                values.append(value)
                i += di
        
        value = 0
        match type_id:
            case 0:
                value = sum(values)
            case 1:
                value = reduce(int.__mul__, values)
            case 2:
                value = min(values)
            case 3:
                value = max(values)
            case 5:
                value = values[0] > values[1]
            case 6:
                value = values[0] < values[1]
            case 7:
                value = values[0] == values[1]
            case _:
                print('wtf')
        
    return i, value

p2 = decode_packet(data)[1]
print(p1)
print(p2)