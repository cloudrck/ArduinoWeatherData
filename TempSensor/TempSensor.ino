//######
//Temperature & Humidity library 
//
//MIT license
//written by Cloudrck Technologies
//#######

#include "DHT.h"

#define DHTPIN 2 // Pin connected to
#define DHTTYPE DHT11 // DHT 11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
 
  dht.begin();
}

void loop() {
  float h = dht.readHumidity();
  //F = fahrenheit; C = Celsius; Default = C
  float t = dht.readTemperature('F');

  // check if returns are valid, if they are NaN 
  if (isnan(t) || isnan(h)) {
    Serial.println("Failed to read from DHT");
  } else {
    //Print humidity value with 'ID' in front
    Serial.print("H"); Serial.println(h);
    //Print Temperature value with 'ID' in front
    Serial.print("T"); Serial.println(t);
    // Check every 5 seconds
    delay(5000);
  }
}
