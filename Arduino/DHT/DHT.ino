#include <Adafruit_Sensor.h>
#include <DHT.h>


int sensor = 2;
float temp;
int hum;
DHT dht22(sensor, DHT22);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  dht22.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  temp=dht22.readTemperature();
  Serial.print(temp);
  Serial.print("ºC  ||  ");
  hum=dht22.readHumidity();
  Serial.print(hum);
  Serial.println("%");
  delay(2000);

  if(hum <= 80){
    digitalWrite(3, 1);
  }else{
    digitalWrite(3, 0);
  }
}
