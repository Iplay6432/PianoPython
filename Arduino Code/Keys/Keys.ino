void setup() {
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(4, INPUT);
  pinMode(5, INPUT);
  pinMode(6, INPUT);
  pinMode(7, INPUT);
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  pinMode(10, INPUT);
  pinMode(11, INPUT);
  pinMode(12, INPUT);
  pinMode(13, INPUT);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(2) == HIGH) {
    Serial.println("C1");
  }
  if (digitalRead(3) == HIGH) {
    Serial.println("Db1");
  }
  if (digitalRead(4) == HIGH) {
    Serial.println("D1");
  }
  if (digitalRead(5) == HIGH) {
    Serial.println("Eb1");
  }
  if (digitalRead(6) == HIGH) {
    Serial.println("E1");
  }
  if (digitalRead(7) == HIGH) {
    Serial.println("F1");
  }
  if (digitalRead(8) == HIGH) {
    Serial.println("Gb1");
  }
  if (digitalRead(9) == HIGH) {
    Serial.println("G1");
  }
  if (digitalRead(10) == HIGH) {
    Serial.println("Ab1");
  }
  if (digitalRead(11) == HIGH) {
    Serial.println("A1");
  }
  if (digitalRead(12) == HIGH) {
    Serial.println("Bb1");
  }
  if (digitalRead(13) == HIGH) {
    Serial.println("B1");
  }
  if (analogRead(A0) > 20) {
    Serial.println("C2");
  }
}
