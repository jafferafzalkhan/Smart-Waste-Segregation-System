#include <Servo.h>

Servo servo;

// Pin connections
int irPin = 2;         // IR Sensor (Digital)
int moisturePin = A0;  // Moisture Sensor (Analog)
int metalPin = 3;      // Metal Sensor (Digital)
int servoPin = 9;      // Servo Motor (PWM)

void setup() {
  Serial.begin(9600);
  pinMode(irPin, INPUT);
  pinMode(metalPin, INPUT);
  servo.attach(servoPin);
  servo.write(90); // neutral position
}

void loop() {
  int irVal = digitalRead(irPin);
  int moistureVal = analogRead(moisturePin);
  int metalVal = digitalRead(metalPin);

  // Send sensor values as CSV to Python
  Serial.print(irVal);
  Serial.print(",");
  Serial.print(moistureVal);
  Serial.print(",");
  Serial.println(metalVal);

  // Check if Python sent command
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');

    if (command == "METAL") {
      servo.write(0);   // Metal bin
    } else if (command == "WET") {
      servo.write(90);  // Wet bin
    } else if (command == "DRY") {
      servo.write(180); // Dry bin
    }
  }

  delay(500);
}
