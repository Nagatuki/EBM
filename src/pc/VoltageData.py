import numpy as np


class VoltageData:
    def __init__(self, size, length):
        self.data = [CHData(i, length) for i in range(size)]
        self.size = size
        self.length = length
    
    def add_data(self, data):
        self.data[data["CH"]].add_data(data["Voltage"])
    
    def get_CH_data(self, CH):
        return self.data[CH]
 

class CHData:
    def __init__(self, number, length):
        self.number = number
        self.length = length
        self.data = [0. for i in range(length)]
        self.time = [0 for i in range(length)]
        self.label = "CH" + str(number) 
    
    def add_data(self, voltage):
        del(self.data[0])
        del(self.time[0])
        self.data.append(voltage)
        self.time.append(self.time[-1] + 0.002)

# class VoltageData2:
#     def __init__(self, size, length):
#         self.size = size
#         self.length = length
#         self.data = np.zeros(shape=(size, length), dtype='float64')
#         self.idx = np.zeros(size, dtype=int)
#         self.cur = np.array([length - 1 for i in range(size)], dtype=int)
    
#     def add_data(self, data):
#         pos = data["CH"]
#         self.data[pos, self.idx[pos]] = data["Voltage"]
#         self.idx[pos] = (self.idx[pos] + 1) % self.length
#         self.cur[pos] = (self.cur[pos] + 1) % self.length