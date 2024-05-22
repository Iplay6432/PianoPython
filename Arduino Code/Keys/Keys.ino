void setup() {
  Serial.begin(9600);
  for (int i=2; i < 8; i++){
    pinMode(i, INPUT);
  }
}

void loop() {
  char output[7];
  output[7] = '\0';
  for (int i=2; i < 8; i++) {
    if (digitalRead(i) == LOW) {
      output[i-2] = '1';
    } else {
      output[i-2] = '0';
    }
  }
  Serial.println(output);
  delay(1000);
}
