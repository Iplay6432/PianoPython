#include <string>

void setup() {
  Serial.begin(9600);
  for (int i=2; i < 8; i++){
    pinMode(i, INPUT);
  }
}

void loop() {
  std::string output = "";
  for (int i=2; i < 8; i++) {
    if (digitalRead(i) == LOW) {
      string += "1";
    } else {
      string += "0";
    }
  }
  Serial.println(output);
  delay(1000);
}
