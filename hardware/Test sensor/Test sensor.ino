const int Pin=A0;

void setup() {
    pinMode(Pin, INPUT);
    Serial.begin(9600);
}
 
void loop() {
  int sensorValue = analogRead(Pin);
  Serial.println(sensorValue);
  delay(500);
}