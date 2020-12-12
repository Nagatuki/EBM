import serial
import time


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