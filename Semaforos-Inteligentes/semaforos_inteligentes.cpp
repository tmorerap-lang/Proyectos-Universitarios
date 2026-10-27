// Semáforo con LEDs
// Pines: 10 = Rojo, 9 = Amarillo, 8 = Verde

const int ROJO = 10;
const int AMARILLO = 9;
const int VERDE = 8;

void setup() {
  pinMode(ROJO, OUTPUT);
  pinMode(AMARILLO, OUTPUT);
  pinMode(VERDE, OUTPUT);
}

void loop() {
  // 1. Verde encendido (avanzar)
  digitalWrite(VERDE, HIGH);
  delay(5000);
  digitalWrite(VERDE, LOW);
  delay(500);

  // 2. Amarillo encendido (precaución)
  digitalWrite(AMARILLO, HIGH);
  delay(2000);
  digitalWrite(AMARILLO, LOW);
  delay(500);

  // 3. Rojo encendido (detener)
  digitalWrite(ROJO, HIGH);
  delay(5000);
  digitalWrite(ROJO, LOW);
  delay(500);
}
