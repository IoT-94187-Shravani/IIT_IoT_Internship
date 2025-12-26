#define MQ2_PIN A0

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(MQ2_PIN,INPUT);
  Serial.println("MQ2 setup is done");
}
void loop() {
  // put your main code here, to run repeatedly:
  int sensorvalue= analogRead(MQ2_PIN);
  Serial.print("Gas sensor");
  Serial.println(sensorvalue);

  if(sensorvalue > 20)
  {
    Serial.println("Gas is detected");
  }
  delay(2000);
}