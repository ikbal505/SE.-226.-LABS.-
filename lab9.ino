  int LED3pin = 46;
  int LED2pin = 45;
  int LED1pin = 44;
  int LED0pin = 43;

  int Button3pin = 41;
  int Button2pin = 40;
  int Button1pin = 39;
  int Button0pin = 38;
  
  
  bool LED2state = LOW;
  bool LED3state = LOW;
  bool LED1state = LOW;
  bool LED0state = LOW;

  bool Button3state = LOW;
  bool Button2state = LOW;
  bool Button1state = LOW;
  bool Button0state = LOW;

  bool Button3prev = LOW;
  bool Button2prev = LOW;
  bool Button1prev = LOW;
  bool Button0prev = LOW;

void setup() {
  pinMode(LED0pin, OUTPUT);
  pinMode(LED1pin, OUTPUT);
  pinMode(LED2pin, OUTPUT);
  pinMode(LED3pin, OUTPUT);

  pinMode(Button0pin, INPUT);
  pinMode(Button1pin, INPUT);
  pinMode(Button2pin, INPUT);
  pinMode(Button3pin, INPUT);

}
// TASK 6
// void loop() {,

//   LED0state = HIGH;
//   digitalWrite(LED0pin, LED0state);
//   delay(1000);
//   LED1state = HIGH;
//   digitalWrite(LED1pin, LED1state);
//   delay(1000);
//   LED2state = HIGH;
//   digitalWrite(LED2pin, LED2state);
//   delay(1000);
//   LED3state = HIGH;
//   digitalWrite(LED3pin, LED3state);
//   delay(1000);
  
// }

void loop(){
  Button0state = digitalRead(Button0pin);
  Button1state = digitalRead(Button1pin);
  Button2state = digitalRead(Button2pin);
  Button3state = digitalRead(Button3pin);

  if (Button0state == HIGH && Button0prev == LOW){
    LED0state = ! LED0state;
    digitalWrite(LED0pin, LED0state);
  }
  if (Button1state == HIGH && Button1prev == LOW){
    LED1state = ! LED1state;
    digitalWrite(LED1pin, LED1state);
  }
  if (Button2state == HIGH && Button2prev == LOW){
    LED2state = ! LED2state;
    digitalWrite(LED2pin, LED2state);
  }
  if (Button3state == HIGH && Button3prev == LOW){
    LED3state = ! LED3state;
    digitalWrite(LED3pin, LED3state);
  }

}
