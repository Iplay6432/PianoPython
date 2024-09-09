#define MAX_PINS 7
#define MAX_PINS 7
#define START_PIN 2

const bool pinsActive[MAX_PINS] = {
  true,
  true,
  true,
  true,
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
  pinMode(MAX_PINS+1, INPUT);
}

void loop() {
  char output[MAX_PINS+1];
  output[MAX_PINS] = '\0';
  for (int i=START_PIN; i < MAX_PINS+START_PIN; i++) {
    const int index = i-START_PIN;
    if (pinsActive[index] && digitalRead(i) == HIGH) {
      output[index] = '1';
    } else {
      output[index] = '0';
    }
  }
  output[MAX_PINS-1] = digitalRead(MAX_PINS+1) == HIGH ? '1' : '0';
  Serial.println(output);
}
