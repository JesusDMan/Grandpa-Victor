const uint8_t a_botton_pin = 2;
uint8_t a_botton_state = 0;
uint8_t a_new_botton_state = 0;

const uint8_t b_botton_pin = 4;
uint8_t b_botton_state = 0;
uint8_t b_new_botton_state = 0;

void setup()
{
  pinMode(a_botton_pin, INPUT);
  pinMode(b_botton_pin, INPUT);
  Serial.begin(9600);
  Serial.println("<Arduino is ready!>");
}
void loop() {
  // put your main code here, to run repeatedly:
  a_new_botton_state = digitalRead(a_botton_pin);
  if (a_botton_state != a_new_botton_state) {
    if (a_new_botton_state) {
      Serial.println("<Yes>");     
      }
    a_botton_state = a_new_botton_state;
  }

  b_new_botton_state = digitalRead(b_botton_pin);
  if (b_botton_state != b_new_botton_state) {
    if (b_new_botton_state) {
      Serial.println("<No>");     
      }
    b_botton_state = b_new_botton_state;
  }
}
