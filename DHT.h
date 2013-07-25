/* Temperature & Humidity library 

MIT license
written by Cloudrck Technologies
*/

#ifndef DHT_H
#define DHT_H
#if ARDUINO >= 100
 #include "Arduino.h"
#else
 #include "WProgram.h"
#endif

// how many timing transitions we need to keep track of. 2 * number bits + extra
#define MAXTIMINGS 85

#define DHT11 11

class DHT {
 private:
  uint8_t data[6];
  uint8_t _pin, _type, _count;
  boolean read(void);
  unsigned long _lastreadtime;
  boolean firstreading;

 public:
  DHT(uint8_t pin, uint8_t type, uint8_t count=6);
  void begin(void);
  float readTemperature(char U);
  float convertCtoF(float);
  float readHumidity(void);

};
#endif
