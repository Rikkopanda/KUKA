#include <Arduino.h>

int Relay = 33;

void setup()
{

  pinMode(13, OUTPUT); //Set Pin13 as output

  digitalWrite(13, HIGH); //Set Pin13 High

  pinMode(Relay, OUTPUT); //Set Pin3 as output

}

void loop()
{
  digitalWrite(Relay, HIGH); //Turn on relay

  delay(2000);

  digitalWrite(Relay, LOW); //Turn off relay

  delay(2000);
}