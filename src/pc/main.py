from ArduinoSerial import ArduinoSerial
from VoltageData import VoltageData
from View import View

from serial.serialutil import SerialException

from multiprocessing import Process, Queue, Event
import time


# 秒間のグラフ更新回数
GRAPH_UPDATE_FREQ = 10
GRAPH_SIZE = 1
GRAPH_LENGTH = 2000

def wait_start():
    while True:
        ipt = input('Press "start"\n>>')
        if ipt == "start":
           return 

def wait_stop():
    while True:
        ipt = input('Press "stop" to terminate jobs\n>>')
        if ipt == 'stop':
            return

def serial_data_receiver(events, queue, com_num):
    try:
        arduino_serial = ArduinoSerial()
        arduino_serial.open(com_num)
    except SerialException:
        print("\nError Occurred: could not open port 'COM{}' \n".format(com_num))
        print("End of batch job.\n")
        events['failed_to_open'].set()
    else:
        print("\nCOM port open.\n")
    
    events['open'].set()
    events['start'].wait()
    
    try:
        arduino_serial.start()
        while not events['close'].is_set():
            data = arduino_serial.read_voltage()
            data and queue.put(data)
    finally:
        arduino_serial.stop()
        arduino_serial.close()

# Viewにdataをコピーして渡せば、データの保持と描画をわけてマルチスレッド可能だが...
# コピーコストの削減を優先した
def view_manager(events, queue):
    voltage_data = VoltageData(size=GRAPH_SIZE, length=GRAPH_LENGTH)
    view = View(data=voltage_data)
    view.show()

    INTERVAL = 1 / GRAPH_UPDATE_FREQ
    BASE_TIME = time.time()

    while not events['stop'].is_set():
        while not queue.empty():
            d = queue.get()
            voltage_data.add_data(d)
        
        view.update()

        next_time = ((BASE_TIME - time.time()) % INTERVAL) or INTERVAL
        time.sleep(next_time)

def main():
    com_num = input("Input COM Port Number\n>>")

    queue = Queue()
    receiver_events = {
        'open': Event(),
        'start': Event(),
        'close': Event(),
        'failed_to_open': Event()
    }
    viewer_events = {
        'stop': Event()
    }

    receiver = Process(target=serial_data_receiver, args=(receiver_events, queue, com_num))
    viewer = Process(target=view_manager, args=(viewer_events, queue,))

    receiver.start()

    receiver_events['open'].wait()
    if receiver_events['failed_to_open'].is_set():
        receiver.terminate()
        return 0

    try:
        wait_start()

        viewer.start()
        receiver_events['start'].set()

        wait_stop()

    except Exception as e:
        if e.__class__.__name__ != "KeyboardInterrupt":
            print('Unexpected error occurred!\n')
            raise e

    finally:
        receiver_events['close'].set()
        viewer_events['stop'].set()
        receiver.join()
        print("\nCOM Port Closed.\n")

    return

if __name__ == "__main__":
    main()