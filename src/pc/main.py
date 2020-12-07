import serial
import numpy as np
import matplotlib.pyplot as plt
import sys
import time


UPDATE_CNT = 100

class ArduinoSerial:
    def __init__(self):
        self.BAUDRATE = "19200"
        self.TIMEOUT = 0.1
        self.com = None

    def open(self, com_num):
        self.com = serial.Serial("COM" + com_num, self.BAUDRATE, timeout = 0.1)
        time.sleep(3)

    def close(self):
        if self.com == None:
            return
        self.com.close()

    def start(self):
        self.com.write(b"s")

    def stop(self):
        self.com.write(b"e")

    def clear(self):
        # バッファ内のゴミを長めに受信して(timeoutさせて)棄てる...らしい
        self.com.read(1000)

    def read_voltage(self):
        ipt = self.com.readline().decode('shift_jis').replace("\r\n", "")

        # データが入ってなければ無視
        if len(ipt) == 0:
            return None

        ipt = ipt.split(" ")

        if len(ipt) == 2:
            ret = dict()
            ret["CH"] = int(ipt[0])
            ret["Voltage"] = float(ipt[1])
            return ret

        return None


class View:
    def __init__(self, graph_size=1, length=500, top=5.0, bottom=-5.0):
        self.graph_size = graph_size
        self.length = length
        self.top = top
        self.bottom = bottom

        self.time = np.array([i for i in range(length)])
        self.data = np.zeros((graph_size, length), dtype='float64')
        self.idx = np.zeros(graph_size, dtype=int)
        self.labels = np.array(["CH" + str(i) for i in range(graph_size)])

        self.fig = plt.figure()
        self.axes = self._create_axes(self.fig, graph_size)

    # def _setting(self):

    def _create_axes(self, fig, size):
        if size == 1:
            return [fig.add_subplot(1, 1, 1)]

        if size == 2:
            return [fig.add_subplot(1, 2, 1), fig.add_subplot(1, 2, 2)]

        if size == 3 or size == 4:
            return [fig.add_subplot(2, 2, i) for i in range(size)]

        if size == 5 or size == 6:
            return [fig.add_subplot(2, 3, i) for i in range(size)]

    def _draw(self, ax, data, label, time):
        ax.plot(self.time, data, label=label)
        ax.legend(loc='upper right')
        ax.set_ylim(self.bottom, self.top)
        ax.set_xlabel("time")
        ax.set_ylabel("Voltage (mV)")

    def show(self, sleep_time=0.0001):
        for ax, data, label in zip(self.axes, self.data, self.labels):
            self._draw(ax, data, label, sleep_time)
        plt.draw()
        plt.pause(sleep_time)

    def update(self, sleep_time=0.0001):
        plt.cla()
        self.show(sleep_time)

    def add_data(self, data):
        pos = data["CH"]
        self.data[pos, self.idx[pos]] = data["Voltage"]
        self.idx[pos] = (self.idx[pos] + 1) % self.length



def main():
    com_num = input("Input COM Port Number\n>>")

    arduino_serial = ArduinoSerial()
    arduino_serial.open(com_num)
    print("COM Port Open.")

    try:

        while True:
            ipt = input('Press "start"\n>>')
            if ipt == "start":
                break

        view = View(length=500)
        view.show()

        arduino_serial.start()

        cnt = 0
        while True:
            data = arduino_serial.read_voltage()

            if data == None:
                continue

            # print(data)
            view.add_data(data)
            cnt = (cnt + 1) % UPDATE_CNT

            if cnt == 0:
                view.update()

    except KeyboardInterrupt:
        arduino_serial.stop()
        arduino_serial.close()
        print("COM Port Closed.")

        sys.exit(0)


if __name__ == "__main__":
    main()
