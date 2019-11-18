int motorPin = 9;
int c = 0;

void setup() {
    pinMode(motorPin, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    digitalWrite(motorPin, HIGH); // analogWrite(pin, 255) also works and it's probably what we'll end up using
    delay(1000);
    digitalWrite(motorPin, LOW);
    delay(1000);
    Serial.print("yeah we still groovin: ");
    Serial.println(c);
    c++;
}