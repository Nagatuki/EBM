#include <FlexiTimer2.h>
#include <SPI.h>

// TODO
// SPI通信をマイコンのポートから行えるようにする
//    SPI.hでやっていることを使いたいポート用に改造して独自にやればいい？

const int BAUDRATE = 19200;
const int ADCMAX = 4095;
const double ADCVREF = 5;

/**
   探索するチャンネルの番号を格納する配列
*/
const int channelArraySize = 1;
const int channelArray[] = {0};

struct MySPI {
  private:
    const int SSPIN = 13;

  private:
    MySPI() = default;
    ~MySPI() = default;

  public:
    static MySPI& getInstance() {
      static MySPI instance;
      return instance;
    }

    void setSS(int flag) {
      if (flag)PORTC |= B10000000;
      else PORTC &= ~B10000000;
    }

    int transfer(int val) {
      return SPI.transfer(val);
    }

    void init() {
      pinMode(this->SSPIN, OUTPUT);
      this->setSS(HIGH);
      SPI.setBitOrder(MSBFIRST);
      SPI.setDataMode(SPI_MODE1);
      SPI.setClockDivider(SPI_CLOCK_DIV8);
      SPI.begin();
    }
};

// ADCのチャンネル"channel"から値を読み出す関数
int readADC(int channel) {
  int d1, d2;
  MySPI::getInstance().setSS(LOW);
  d1 = SPI.transfer(0b00000110 | (channel >> 2));
  d1 = SPI.transfer(channel << 6);
  d2 = SPI.transfer(0x00);
  MySPI::getInstance().setSS(HIGH);
  return (d1 & 0x0F) * 0xFF + d2;
}

// シリアル受信に関する処理を行う関数
void serialReceive() {
  // availableで先に確認した方がいい？
  int data = Serial.read();
  switch (data) {
    case 's':
      FlexiTimer2::start();
      break;

    case 'e':
      FlexiTimer2::stop();
      break;
  }
}

// チャンネル番号と電圧値をシリアルで送信する関数
//「<CH番号> <電圧値>」
void serialSendVoltage(int channel, double voltage) {
  String s = String(channel) + " " + String(voltage);
  Serial.println(s);
}

// 2 ms毎(500 Hz)にポーリングしてADCからデータを取得する
void timerFunc() {
  for (int i = 0; i < channelArraySize; ++i) {
    int data = readADC(channelArray[i]);
    double ipt_v = ADCVREF * data / ADCMAX;
    serialSendVoltage(channelArray[i], ipt_v * 2 - 5.0);
  }
}

void setup() {
  // SPI
  MySPI::getInstance().init();

  // Serial ( Arduino <-> PC )
  Serial.begin(BAUDRATE);
  while (!Serial);

  // Timer(2 ms毎)
  FlexiTimer2::set(2, timerFunc);

  // wait
  while (Serial.read() != 's');
  FlexiTimer2::start();
}

void loop() {
  serialReceive();
}
