#define MAX_PINS 7
#define MAX_PINS 7
#define START_PIN 2

bool pinsActive[MAX_PINS] = {
  false,
  false,
  false,
  false,
  true,
  false,
  false,
};

void setup() {
  Serial.begin(9600);
  for (int i=START_PIN; i < MAX_PINS+START_PIN; i++){
    if (pinsActive[i-START_PIN])
      pinMode(i, INPUT);
  }
}

void loop() {
  char output[MAX_PINS];
  output[MAX_PINS-1] = '\0';
  for (int i=START_PIN; i < MAX_PINS+START_PIN; i++) {
    const int index = i-START_PIN;
    if (pinsActive[index] && digitalRead(i) == HIGH) {
      output[index] = '1';
    } else {
      output[index] = '0';
    }
  }
  Serial.println(output);
  delay(10);
}
