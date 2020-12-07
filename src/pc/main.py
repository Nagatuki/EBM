import serial
import sys
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
            ret["CH"] = ipt[0]
            ret["Voltage"] = float(ipt[1])
            return ret

        return None


def view(data):
    # make and show a graph
    print(data)

'''
TODO
- プログラムの停止方法
- 一定時間毎にデータ取得およびグラフ更新をする方法
- グラフ描画処理
'''

def main():
    com_num = input("Input COM Port Number\n>>")

    arduino_serial = ArduinoSerial()
    arduino_serial.open(com_num)

    print("COM Port Open.")

    while True:
        ipt = input('Press "start"\n>>')
        if ipt == "start":
            break

    arduino_serial.start()

    try:
        while True:
            data = arduino_serial.read_voltage()
            if data == None:
                continue
            view(data)

    except KeyboardInterrupt:
        arduino_serial.stop()
        arduino_serial.close()
        print("COM Port Closed.")

        sys.exit(0)


if __name__ == "__main__":
    main()
